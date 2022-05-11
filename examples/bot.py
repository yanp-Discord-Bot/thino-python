import discord
from discord.ext import commands
import asyncio
import thino

bot = commands.Bot(command_prefix="prefixhere", intents=discord.Intents.default)

@bot.command()
async def nsfw(ctx: commands.Context):
    r = await thino.img("tomboy")

    await ctx.send(r['url'])

async def main():
    async with bot:
        await bot.start("tokenhere")


asyncio.run(main())