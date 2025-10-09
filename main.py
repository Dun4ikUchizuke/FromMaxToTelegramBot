import asyncio
from create_bot import bot, dp, scheduler
from handlers import router, GetMessages

async def main():
    dp.include_router(router)
    scheduler.add_job(GetMessages, trigger='interval', minutes = 1)
    scheduler.start()
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    
if __name__ == "__main__":
    asyncio.run(main())
