from aiogram import Bot, Dispatcher, executor, types
from dotenv import load_dotenv
import os
import httpx

load_dotenv()

API_KEY = os.getenv("API_KEY")
assert API_KEY is not None
bot = Bot(token=API_KEY)
dp = Dispatcher(bot)


@dp.message_handler(commands=["bible", "amen", "bless"])
async def send_welcome(message: types.Message) -> None:
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    res = await getBibleVerse()
    await message.answer(res)


@dp.message_handler(commands=["hello"])
async def send_greeting(message: types.Message) -> None:
    user = message.from_user
    await message.answer(f"Howdy, {user.first_name}!")


@dp.message_handler(commands=["fuck"])
async def sendFuck(message: types.Message) -> None:
    user = message.from_user
    await message.reply(f"fuck you {user.first_name} 🖕🏻🖕🏼🖕🏽🖕🏾🖕🏿")


@dp.message_handler(commands=["room_ID"])
async def haha(message: types.Message) -> None:
    await message.answer(str(message.chat.id))


@dp.message_handler(commands=["test"])
async def testMessage(message: types.Message) -> None:
    await message.reply("test your mother")


async def getBibleVerse() -> str:
    """
    Get a random bible verse

    Returns
    -------
    str
    """
    async with httpx.AsyncClient() as client:
        res = await client.get("http://quotes.rest/bible/verse.json")

        data: dict[str, str] = res.json()["contents"]

        verse = data["verse"]
        book = data["book"]
        chapter = data["chapter"]
        number = data["number"]
        testament = data["testament"]

        return f"{verse} \n\n- {book} {chapter}:{number} ({testament})"


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
