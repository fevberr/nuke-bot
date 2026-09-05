import discord
import asyncio

async def _29(ctx):
    if not ctx.guild.me.guild_permissions.mute_members:
        await ctx.send("BOT NEEDS MUTE MEMBERS PERMISSION", delete_after=3)
        return
    await ctx.send("MUTING ALL MEMBERS", delete_after=2)
    members = [m for m in ctx.guild.members if not m.bot]
    count = 0
    for member in members:
        try:
            await member.edit(mute=True)
            count += 1
            if count % 10 == 0:
                await asyncio.sleep(0.1)
        except:
            pass
    await ctx.send(f"MUTED {count} MEMBERS")
