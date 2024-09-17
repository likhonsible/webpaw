import telebot
import requests

API_TOKEN = '7041160117:AAEUZIlYBEjFoJzZgVyElg8EOehAm9aofbE'
bot = telebot.TeleBot(API_TOKEN)

# Start command handler
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome to Tap Pizza! Tap the button below to earn pizza slices 🍕. Use /leaderboard to see the top players.")

# Tap command handler
@bot.message_handler(commands=['tap'])
def send_pizza(message):
    user_id = message.from_user.id
    username = message.from_user.username
    url = f"https://clicker.toshkentinvest.uz/backend/tap.php?user_id={user_id}&username={username}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises HTTPError for bad responses
        data = response.json()
        earnings = data.get('earnings', 0)
        bot.reply_to(message, f"🍕 You earned more slices! Total pizza slices: {earnings}")
    except requests.RequestException as e:
        bot.reply_to(message, f"Something went wrong: {str(e)}")

# Leaderboard command handler
@bot.message_handler(commands=['leaderboard'])
def leaderboard(message):
    url = "https://clicker.toshkentinvest.uz/backend/leaderboard.php"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raises HTTPError for bad responses
        leaderboard_data = response.json()
        leaderboard_text = "\n".join([f"{i+1}. {user['username']}: {user['earnings']} 🍕" for i, user in enumerate(leaderboard_data)])
        bot.reply_to(message, f"🏆 Pizza Tap Leaderboard 🏆\n\n{leaderboard_text}")
    except requests.RequestException as e:
        bot.reply_to(message, f"Error fetching leaderboard: {str(e)}")

bot.polling()