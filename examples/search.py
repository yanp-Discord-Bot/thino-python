import asyncio
import thino


async def main():
    return await thino.search("cw3qk12xk6p71.png")

search_result = asyncio.run(main())
print(search_result)