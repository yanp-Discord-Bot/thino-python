import asyncio
import thino


async def main():
    client = thino.Client()
    return await client.tomboy()


tomboy = asyncio.run(main())
print(tomboy)
print(tomboy.url) # just gets the URL. in order to get specifc json data, use .raw method.