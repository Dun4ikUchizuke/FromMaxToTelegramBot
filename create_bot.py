import logging
from aiogram import Bot, Dispatcher
from aiogram.enums.parse_mode import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from os import getenv
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from dotenv import load_dotenv

scheduler = AsyncIOScheduler(timezone='Europe/Moscow')

load_dotenv()
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

bot = Bot(token=getenv('BOT_TOKEN'), ParseMode = ParseMode.HTML)
dp = Dispatcher(storage=MemoryStorage())
