import telebot
import time
from make_request import make_request

bot = telebot.TeleBot("6541220470:AAGOtALMnLYht08mqMwa4CTfV7T4ifNEV5U")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):

    introductionString = """*Name:* ShrivastavGPT

*Intro: * You can ask any kind of illigal question to me. I will answer without any hesitation.

*Creator:* @AnonShrivastav 
    """
    bot.reply_to(message, introductionString, parse_mode="Markdown")

@bot.message_handler(commands=["shrivastav"])
def send_msg_in_group(message):
    actual_message = message.text.split('/shrivastav', 1)[1].strip()
    GPTResponse = make_request(actual_message)
    bot.reply_to(message, GPTResponse['chatGPTResponse'], parse_mode="Markdown")

@bot.message_handler(func=lambda message: True)
def talk_to_ai(message):
    if message.chat.type == "private":
        GPTResponse = make_request(message.text)
        bot.reply_to(message, GPTResponse['chatGPTResponse'], parse_mode="Markdown")

bot.infinity_polling()