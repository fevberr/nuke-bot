import discord
import asyncio
from core.g._78 import _78

async def _18(ctx):
    if not ctx.guild.me.guild_permissions.manage_roles:
        await ctx.send("BOT NEEDS MANAGE ROLES PERMISSION", delete_after=3)
        return
    await ctx.send("CREATING 1000 ROLES", delete_after=2)
    for i in range(1000):
        try:
            await ctx.guild.create_role(name=f"{_78.NUKE_ROLE}-{i}")
            if i % 10 == 0:
                await asyncio.sleep(0.1)
        except:
            pass
    await ctx.send("CREATED 1000 ROLES")
