from core.commands.base import BaseCommand
import discord

class HackbanCommand(BaseCommand):
    async def _execute(self, ctx):
        await ctx.send("HACKBAN - ENTER USER ID TO BAN", delete_after=2)
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel
        try:
            msg = await bot.wait_for('message', timeout=30, check=check)
            user_id = int(msg.content)
            user = await bot.fetch_user(user_id)
            await ctx.guild.ban(user, reason="Hackban")
            await ctx.send(f"BANNED USER {user.name}")
        except:
            await ctx.send("TIMEOUT OR INVALID ID", delete_after=3)
