import asyncio
import thino


async def main():
    return await thino.img("tomboy")
    

search_result = asyncio.run(main())
print(search_result['url'])