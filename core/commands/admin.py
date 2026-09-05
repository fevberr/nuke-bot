from core.commands.base import BaseCommand
from core.config.settings import ADMIN_COMMAND
import discord

class AdminCommand(BaseCommand):
    async def _execute(self, ctx):
        await ctx.send("ADMIN COMMAND EXECUTED", delete_after=2)
        await ctx.send("ADMIN LOGIC RUN", delete_after=2)
