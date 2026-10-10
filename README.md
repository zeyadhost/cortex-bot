# cortex-bot
A Python-powered Discord bot that automates server setup, API testing and reverse-engineering workflows behind a single command interface.

## Project structure
```
.
├── main.py # entry point: config, logging, bot, cog discovery
├── cogs/ # one module per command category
│ └── ping.py
├── services/ # shared helpers (HTTP session, etc.)
│ └── http.py
├── .env # secrets (not committed)
└── requirements.txt
```

## Setup
```bash
git clone https://github.com/zeyadhost/cortex-bot
cd cortex-bot
python -m venv .venv
.venv\Scripts\Activate.ps1 # (source .venv/bin/activate for Linux/macOS)
pip install -r requirements.txt
cp .env.example .env
nano .env # or use your preferred editor to edit .env
python main.py
```