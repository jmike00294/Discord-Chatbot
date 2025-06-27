# ChatGPT Discord Bot

This is a simple Discord bot that integrates with OpenAI's GPT model (text-davinci-002) to respond to user questions. It uses the `discord.py` and `openai` libraries, and reads API keys from environment variables using a `.env` file.

## Features

- Responds to prompts using the `!ask` command.
- Powered by OpenAI's `text-davinci-002` model.
- Loads secrets securely from a `.env` file.
- Basic error handling for invalid commands.

---

## Requirements

- Python 3.7+
- `discord.py`
- `openai`
- `python-dotenv`

## Installation

1. **Clone the repo:**

```bash
git clone https://github.com/your-username/chatgpt-discord-bot.git
cd chatgpt-discord-bot
```
2. Install dependencies:
```bash
pip install -r requirements.txt
```
3. Create a .env file in the root directory:
```bash
DISCORD_BOT_TOKEN=your_discord_bot_token
OPEN_AI_TOKEN=your_openai_api_key
```

## Usage
1. Run the bot
```bash
python chatgpt_discord_bot.py
```
2. In your Discord server, use the command:
 ```bash
!ask What is the capital of France?
```
The bot will reply using OpenAI’s GPT model.

## Notes
Make sure the bot has the appropriate permissions (message read/send) and MESSAGE CONTENT INTENT is enabled in the Discord Developer Portal.

You can update the OpenAI model or engine in the generate_response() function as needed.
