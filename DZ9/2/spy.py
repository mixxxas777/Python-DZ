
from telegram import Update
from telegram.ext import ContextTypes
from bot_commands import *



def log(update: Update, context: ContextTypes):
    file = open('db.csv', 'a', encoding='UTF-8')
    file.write(f'{update.effective_user.first_name}, {update.effective_user.id}, {update.message.text})')
    file.close()