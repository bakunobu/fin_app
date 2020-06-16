"""
testing telegrambots
thanks to mastergroosha.github.io
"""

import telebot
import os
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())

TOKEN = os.environ.get('TEL_TOKEN')

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(content_types=['text'])
def repeat_all_messages(message):
    '''
    return user's input as a message
    
    Args:
    message: 
    an input from telegram service
    '''
    bot.send_message(message.chat.id, message.text)
    

if __name__ == '__main__':
    bot.infinity_polling()