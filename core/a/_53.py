import discord

async def _53(ctx):
    latency = round(bot.latency * 1000)
    await ctx.send(f"PONG - {latency}ms", delete_after=5)
