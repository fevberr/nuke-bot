from core.commands.base import BaseCommand
import discord

class WarnCommand(BaseCommand):
    async def _execute(self, ctx):
        await ctx.send("WARN - ENTER USER ID AND REASON", delete_after=2)
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel
        try:
            msg = await bot.wait_for('message', timeout=30, check=check)
            parts = msg.content.split(' ', 1)
            user_id = int(parts[0])
            reason = parts[1] if len(parts) > 1 else "No reason"
            user = await bot.fetch_user(user_id)
            await ctx.send(f"WARNED USER {user.name} - REASON: {reason}")
        except:
            await ctx.send("TIMEOUT OR INVALID INPUT", delete_after=3)
