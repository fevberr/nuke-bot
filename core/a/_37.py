import discord

async def _37(ctx):
    if not ctx.guild.me.guild_permissions.send_messages:
        await ctx.send("BOT NEEDS SEND MESSAGES PERMISSION", delete_after=3)
        return
    await ctx.send("FILE SPAMMING", delete_after=2)
    for i in range(50):
        await ctx.send(file=discord.File('dummy.txt'))
