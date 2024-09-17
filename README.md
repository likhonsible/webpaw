# Pizza Tap Game

This is a simple pizza tap game using SQLite, a Telegram bot, and a Vue.js frontend. Users tap a pizza to earn slices, and a leaderboard shows the top users.

## Setup

### Backend
1. Run `db_setup.php` to auto-create the SQLite database and tables.
2. Ensure `backend/` folder has write permissions for the SQLite database file.
3. You can then access the tap game via the frontend and bot.

### Telegram Bot
1. Replace the `API_TOKEN` in `bot/telebot_bot.py` with your Telegram bot token.
2. Run the bot with `python bot/telebot_bot.py`.

### Frontend
1. Open `frontend/index.html` to play the game.
2. Tap the pizza and view the leaderboard.
