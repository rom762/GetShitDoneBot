### Install uv

On macOs/Linux:
```
curl -LsSf https://astral.sh/uv/install.sh | sh
```

on Windows using PowerShell:
```
irm https://astral.sh/uv/install.ps1 | iex
```

Clone repo:

```
git clone https://github.com/rom762/GetShitDoneBot.git
```

edit .dev file - use your own keys for TelegramBot, OpenAI API and base url

rename .dev file to .env file:

Run Project:
```
uv run main.py
```
