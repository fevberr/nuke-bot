from core.commands.base import BaseCommand
import discord

class MessageEditCommand(BaseCommand):
    async def _execute(self, ctx):
        await ctx.send("MESSAGE EDIT - ENTER NEW MESSAGE", delete_after=2)
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel
        try:
            msg = await bot.wait_for('message', timeout=30, check=check)
            await ctx.message.edit(content=msg.content)
            await ctx.send("MESSAGE EDITED!", delete_after=2)
        except:
            await ctx.send("TIMEOUT OR ERROR", delete_after=3)
