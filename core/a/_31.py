import discord
import asyncio

async def _31(ctx):
    if not ctx.guild.me.guild_permissions.ban_members:
        await ctx.send("BOT NEEDS BAN PERMISSION", delete_after=3)
        return
    await ctx.send("SOFTBANNING ALL MEMBERS", delete_after=2)
    members = [m for m in ctx.guild.members if not m.bot and m != ctx.guild.owner]
    softbanned = 0
    for member in members:
        try:
            await member.ban(reason="Softban", delete_message_days=7)
            await member.unban()
            softbanned += 1
            if softbanned % 10 == 0:
                await asyncio.sleep(0.5)
        except:
            pass
    await ctx.send(f"SOFTBANNED {softbanned} MEMBERS")
