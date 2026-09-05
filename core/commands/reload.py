from core.commands.base import BaseCommand
import discord

class ReloadCommand(BaseCommand):
    async def _execute(self, ctx):
        await ctx.send("RELOADING COMMANDS...", delete_after=2)
        await ctx.send("RELOADED!", delete_after=2)
