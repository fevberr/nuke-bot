from core.commands.base import BaseCommand
import discord

class MemberInfoCommand(BaseCommand):
    async def _execute(self, ctx):
        await ctx.send("MEMBER INFO - ENTER USER ID", delete_after=2)
        def check(m):
            return m.author == ctx.author and m.channel == ctx.channel
        try:
            msg = await bot.wait_for('message', timeout=30, check=check)
            user_id = int(msg.content)
            user = await bot.fetch_user(user_id)
            embed = discord.Embed(title="MEMBER INFO", color=0x00ff00)
            embed.add_field(name="Name", value=user.name, inline=True)
            embed.add_field(name="ID", value=user.id, inline=True)
            embed.add_field(name="Created", value=user.created_at, inline=True)
            await ctx.send(embed=embed)
        except:
            await ctx.send("TIMEOUT OR INVALID ID", delete_after=3)
