import os
import openai
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()


# Replace 'your_openai_api_key' with your actual OpenAI API key
openai.api_key = os.environ.get("OPEN_AI_TOKEN")
# Replace 'your_bot_token' with your Discord bot token
DISCORD_BOT_TOKEN = os.environ.get("DISCORD_BOT_TOKEN")

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
intents.guilds = True
intents.members = True


# Initialize the Discord bot with the specified intents
bot = commands.Bot(command_prefix="!", intents=intents)


async def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )

    message = response.choices[0].text.strip()
    return message

@bot.command(name="ask")
async def ask(ctx, *, question):
    prompt = f"{question}"
    response = await generate_response(prompt)
    await ctx.send(response)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        return
    raise error

if __name__ == "__main__":
    bot.run(DISCORD_BOT_TOKEN)
