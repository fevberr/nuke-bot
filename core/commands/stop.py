from core.commands.base import BaseCommand
import discord

class StopCommand(BaseCommand):
    async def _execute(self, ctx, bot):
        await ctx.send("SHUTTING DOWN BOT", delete_after=2)
        await bot.close()
