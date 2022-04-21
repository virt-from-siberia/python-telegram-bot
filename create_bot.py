from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage


storage = MemoryStorage()

bot = Bot(token='5193668710:AAFOSfX5wzQNxctkNKnBiDDt_SeCdYiefhI')
dp = Dispatcher(bot, storage=storage)
