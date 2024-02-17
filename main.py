import telebot

bot = telebot.TeleBot("6979604150:AAGeP3GuIn_t0Y_2Pv3zor_BkSpk306XQT4")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Anon Shrivastav Here?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.infinity_polling()