from lib.bot import dp
import httpx
from aiogram import types


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
