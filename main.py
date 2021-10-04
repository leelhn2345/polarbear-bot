import os

from aiogram import Bot, Dispatcher, executor
from dotenv import load_dotenv

from lib.logger import logger
from src.commands import registerCommands


def main() -> None:
    load_dotenv()

    API_KEY = os.getenv("API_KEY")
    assert API_KEY is not None, "API KEY is not set"
    bot = Bot(token=API_KEY)
    dp = Dispatcher(bot)

    registerCommands(dp)

    logger.info("starting polar bear bot! ( ͡° ͜ʖ ͡°)")

    executor.start_polling(dp, skip_updates=True)


if __name__ == "__main__":
    try:
        main()
    except (SystemExit, KeyboardInterrupt):
        logger.error("bot has been stopped, either abruptly or intentionally")
