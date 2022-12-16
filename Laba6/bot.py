import config
import logging 
#import dbworker
import os
import telebot
import time
#import SQLighter
#mport utils
import random
from aiogram import Bot, Dispatcher, executor, types


logging.basicConfig(level=logging.INFO)
bot = Dispatcher(Bot(token=config.token))

@bot.message_handler(content_types=["new_chat_members"])
async def in_user_joined(message: types.Message):
    await message.delete()
# remove new user joined messages
@bot.message_handler(content_types=["new_chat_members"])
async def in_user_joined(message: types.Message):
    await message.delete()

# Приветсвие
@bot.message_handler(commands=["start"], commands_prefix="/")
async def start(message:types.Message):
    await message.reply('Привет, {0}!'.format(message.from_user.first_name))

async def process_event(update, dp: Dispatcher):
    Bot.set_current(dp.bot)
    await dp.process_update(update)

@bot.message_handler(commands=["help"], commands_prefix="/")
async def help(message:types.Message):
    await message.reply('Мои возможности на данный момент\n\tПовторюшка\n\tКоманда /help'.format(message.from_user.first_name))

#echo
@bot.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)

async def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start, commands=["starts"])
    dp.register_message_handler(echo)


# run long-polling
if __name__ == "__main__":
    #utils.count_rows()
    #random.seed()
    #bot.infinity_polling()
   executor.start_polling(bot, skip_updates=True)