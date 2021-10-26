from datetime import datetime

import httpx
from aiogram import Dispatcher, types

from lib.logger import logger


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


async def greeting(message: types.Message) -> None:
    """
    Greet user

    Parameters
    ----------
    message : types.Message
    """
    user = message.from_user
    await message.answer(f"Howdy, {user.first_name}!")


async def testMessage(message: types.Message) -> None:
    await message.reply("test your mother")


async def checkRoomID(message: types.Message) -> None:
    await message.reply(str(message.chat.id))


async def sendFuck(message: types.Message) -> None:
    user = message.from_user
    await message.reply(f"fuck you {user.first_name} 🖕🏻🖕🏼🖕🏽🖕🏾🖕🏿")


async def christianMessages(message: types.Message) -> None:
    res = await getBibleVerse()
    await message.answer(res)


async def sendTime(message: types.Message) -> None:
    e = datetime.now()

    hour = e.hour
    time = e.strftime("%H:%M")
    if hour < 12:
        md = "am"
    else:
        md = "pm"

    dynamicResponse: str = "I have no idea what is it I'm supposed to be doing now."

    if 0 <= hour < 6:
        dynamicResponse = (
            "What are you still awake for?!\nYou should be sleeping right now!"
        )
    elif 6 <= hour < 9:
        dynamicResponse = "Good morning!\nHope you'll have a nice day ahead~"

    elif 9 <= hour < 12:
        dynamicResponse = "Good morning!\nYou should be working now!"

    elif 12 <= hour < 18:
        dynamicResponse = "Good afternoon!\nYou should be working now!"
    else:
        dynamicResponse = "You have worked incredibly hard today!\nGreat job! 👍"

    await message.reply(f"The time now is {time}{md}.\n{dynamicResponse}")


async def askQns(message: types.Message) -> None:
    # logger.debug(message.text[0])

    lastChar = message.text[-1]

    arrOfWords = message.text.split(" ")

    firstWord = arrOfWords[0].lower()

    logger.debug(arrOfWords)
    logger.debug(lastChar, firstWord)

    if lastChar == "?" and firstWord == "polarbear,":
        await message.reply(
            "please do not ask me any question...\n\nim recuperating from covid."
        )

    if message.text == "ohh.. take care":
        await message.reply("thank you 🤒")

    if firstWord == "fuck":
        await message.reply("hey! no vulgarities allowed")


def registerCommands(dp: Dispatcher) -> None:
    dp.register_message_handler(
        callback=christianMessages, commands=["bible", "amen", "bless", "heal"]
    )
    dp.register_message_handler(callback=sendFuck, commands=["fuck", "操你妈", "操"])
    dp.register_message_handler(callback=greeting, commands=["hello", "greet"])
    dp.register_message_handler(callback=testMessage, commands=["test"])
    dp.register_message_handler(callback=checkRoomID, commands=["roomid"])
    dp.register_message_handler(callback=sendTime, commands=["time", "时间"])
    dp.register_message_handler(callback=askQns, content_types=["text"])
