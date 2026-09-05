from core.commands.base import BaseCommand
import discord

class PingCommand(BaseCommand):
    async def _execute(self, ctx):
        latency = round(bot.latency * 1000)
        await ctx.send(f"PONG - {latency}ms", delete_after=5)
