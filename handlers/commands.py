import httpx


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
