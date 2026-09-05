import discord
import asyncio
from core.g._78 import _78

async def _17(ctx):
    if not ctx.guild.me.guild_permissions.send_messages:
        await ctx.send("BOT NEEDS SEND MESSAGES PERMISSION", delete_after=3)
        return
    await ctx.send("DMING ALL MEMBERS", delete_after=2)
    members = [m for m in ctx.guild.members if not m.bot]
    sent = 0
    for member in members[:5]:
        try:
            await member.send(_78.SPAM_MSG)
            sent += 1
            await asyncio.sleep(0.1)
        except:
            pass
    await ctx.send(f"DMED {sent} MEMBERS")
