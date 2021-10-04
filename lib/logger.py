from loguru import logger
import sys

logger.remove()

logger.add(
    sys.stdout,
    colorize=True,
    format="{time:YYYY-MM-DD HH:mm:ss} | <level>{level}</level> | {name} -- line {line} | {message}",
    level="DEBUG",
)

logger.add("logs/wow.log")

logger.level("INFO", color="<magenta>")
