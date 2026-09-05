from core.commands.base import BaseCommand
from core.config.settings import REACT_EMOJI, REACT_MESSAGE_COUNT
import discord

class ReactCommand(BaseCommand):
    async def _execute(self, ctx):
        if not ctx.guild.me.guild_permissions.add_reactions:
            await ctx.send("BOT NEEDS ADD REACTIONS PERMISSION", delete_after=3)
            return
        await ctx.send("ADDING REACTIONS", delete_after=2)
        messages = []
        async for msg in ctx.channel.history(limit=REACT_MESSAGE_COUNT):
            messages.append(msg)
        for msg in messages:
            try:
                await msg.add_reaction(REACT_EMOJI)
            except:
                pass
        await ctx.send("REACTIONS ADDED", delete_after=2)
