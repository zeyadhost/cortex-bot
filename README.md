# cortex-bot
A Python-powered Discord bot that automates server setup, API testing and reverse-engineering workflows behind a single command interface.

## Project structure
```
├── main.py
├── cogs/
│   ├── ping.py
│   ├── hash.py
│   └── fileinfo.py
├── services/            # (empty for now; planned)
├── .env
├── .env.example
├── requirements.txt
└── requirements-windows.txt
```

## Setup
```bash
git clone https://github.com/zeyadhost/cortex-bot
cd cortex-bot
python -m venv .venv
.venv\Scripts\Activate.ps1 # (source .venv/bin/activate for Linux/macOS)
pip install -r requirements.txt # (pip install -r requirements-windows.txt for Windows)
cp .env.example .env # (Copy-Item .env.example .env on Windows)
nano .env # or use your preferred editor to edit .env
python main.py
```