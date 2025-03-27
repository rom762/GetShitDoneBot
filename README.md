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

edit .env.sample file - use your own keys for TelegramBot, OpenAI API and base url

rename .env.sample to .env:

Run Project:
```
uv run main.py
```
