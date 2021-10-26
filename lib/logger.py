import sys

from loguru import logger

logger.remove()

logger.add(
    sys.stdout,
    colorize=True,
    format="{time:YYYY-MM-DD HH:mm:ss} | <level>{level}</level> | {name} -- line {line} | {message}",
    level="INFO",
)

logger.add("logs/wow.log")

logger.level("INFO", color="<magenta>")
