import discord

async def _67(ctx):
    if not ctx.guild.me.guild_permissions.send_messages:
        await ctx.send("BOT NEEDS SEND MESSAGES PERMISSION", delete_after=3)
        return
    await ctx.send("DMING MEMBERS", delete_after=2)
    members = ctx.guild.members[:10]
    count = 0
    for member in members:
        try:
            await member.send("Hello from bot")
            count += 1
        except:
            pass
    await ctx.send(f"DMED {count} MEMBERS", delete_after=2)
