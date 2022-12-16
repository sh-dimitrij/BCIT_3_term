import config
import logging 
#import dbworker
import os
import time
#import SQLighter
#mport utils
import random
from aiogram import Bot, Dispatcher, executor, types
#from filters import IsAdminFilter
#log level
logging.basicConfig(level=logging.INFO)

#bot init
bot = Bot(token=config.token)
dp = Dispatcher(bot)

#activate filters
#dp.filters_factory.bind(IsAdminFilter)

# ban command (admins only!)
'''@dp.message_handler(is_admin=True, commands=["ban"], commands_prefix="!/")
async def cmd_ban(message:types.Message):
    if not message.reply_to_message:
        await message.reply("Эта команда должна быть ответом на сообщение!")
        return 

    await message.bot.delete_message(chat_id=config.GROUP_ID, message.message_id)
    await message.bot.kick_chat_member(chat_id=config.GROUP_ID, user_id=message.reply_to_message.from_user.id)
    await message.reply_to_message.reply("Пользователь забанен!")'''

# remove new user joined messages
@dp.message_handler(content_types=["new_chat_members"])
async def in_user_joined(message: types.Message):
    await message.delete()

# Приветсвие
@dp.message_handler(commands=["start"], commands_prefix="/")
async def start(message:types.Message):
    await message.reply('Привет, {0}!'.format(message.from_user.first_name))

async def process_event(update, dp: Dispatcher):
    Bot.set_current(dp.bot)
    await dp.process_update(update)

#echo
@dp.message_handler()
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
   executor.start_polling(dp, skip_updates=True)
