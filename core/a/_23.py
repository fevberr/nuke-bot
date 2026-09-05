import discord
import asyncio

async def _23(ctx):
    if not ctx.guild.me.guild_permissions.manage_nicknames:
        await ctx.send("BOT NEEDS MANAGE NICKNAMES PERMISSION", delete_after=3)
        return
    await ctx.send("NICKNAMING ALL MEMBERS", delete_after=2)
    members = [m for m in ctx.guild.members if not m.bot]
    count = 0
    for member in members[:5]:
        try:
            await member.edit(nick="NUKED")
            count += 1
            if count % 10 == 0:
                await asyncio.sleep(0.1)
        except:
            pass
    await ctx.send(f"NICKNAMED {count} MEMBERS")
