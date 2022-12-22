from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from config import TOKEN
from spy import *
from telegram import Update
from telegram.ext import ContextTypes
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
import logging


bot = Bot(token=TOKEN)
dp = Dispatcher(bot)
dp = Dispatcher(bot, storage=MemoryStorage())
dp.middleware.setup(LoggingMiddleware())

@dp.message_handler(commands=['start'])
async def process_start_command (message: types.Message):
    # log(Update, message)
    await message.reply("Привет!\n Напиши мне что-нибудь!\n")

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Напиши мне что-нибудь, и я отпрпавлю этот текст тебе в ответ!")

@dp.message_handler()
async def echo_message(messege: types.Message):
    await bot.send_message(messege.from_user.id, messege.text)


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

logger = logging.getLogger(__name__)