import discord

async def _39(ctx):
    if not ctx.guild.me.guild_permissions.send_messages:
        await ctx.send("BOT NEEDS SEND MESSAGES PERMISSION", delete_after=3)
        return
    await ctx.send("STICKER SPAMMING", delete_after=2)
    stickers = ctx.guild.stickers
    if not stickers:
        await ctx.send("NO STICKERS FOUND", delete_after=2)
        return
    for i in range(50):
        await ctx.send(stickers[0])
