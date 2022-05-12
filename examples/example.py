import asyncio
import thino


async def main():
    client = thino.Client()
    return await client.tomboy()


femboy = asyncio.run(main())
print(femboy)
print(femboy.url)