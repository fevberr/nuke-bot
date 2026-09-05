from core.commands.base import BaseCommand
import discord

class MessageDeleteCommand(BaseCommand):
    async def _execute(self, ctx):
        if not ctx.guild.me.guild_permissions.manage_messages:
            await ctx.send("BOT NEEDS MANAGE MESSAGES PERMISSION", delete_after=3)
            return
        await ctx.send("DELETE MESSAGES - ENTER AMOUNT", delete_after=2)
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel
        try:
            msg = await bot.wait_for('message', timeout=30, check=check)
            amount = int(msg.content)
            await ctx.channel.purge(limit=amount + 1)
            await ctx.send(f"DELETED {amount} MESSAGES", delete_after=2)
        except:
            await ctx.send("TIMEOUT OR ERROR", delete_after=3)
