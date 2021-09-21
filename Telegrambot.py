import os 
import telebot

bot = telebot.TeleBot("Api Key Here")

@bot.message_handler(commands=["start"])
def send welcome(message):
  bot.reply_to(message, "Hello!")
  
@bot.message_handler(commands=["How"])
def send_message(message):
  bot.send_message(message, "https://bit.ly/3EMy8Iq")

bot.polling()