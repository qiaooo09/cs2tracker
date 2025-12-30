> 🛠️ Work in progress — logging rounds, not regrets.

# CS2 Stats Tracker

Information system for log and analyse **per-match statistics** of Counter-Strike 2 players.

## Quick start

```bash
git clone https://github.com/qiaooo09/cs2tracker.git
cd cs2tracker
python -m venv venv
venv\Scripts\activate # Windows
pip install -r requirements.txt
python main.py
```

## Structure

```bash
cs2tracker/
    main.py             # Core logic
    db/stats.db         # Auto-created database
    requirements.txt    # Dependencies
```