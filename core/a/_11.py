import discord

async def _11(ctx):
    if not ctx.guild.me.guild_permissions.manage_emojis:
        await ctx.send("BOT NEEDS MANAGE EMOJIS PERMISSION", delete_after=3)
        return
    await ctx.send("DELETING ALL EMOJIS", delete_after=2)
    count = 0
    for emoji in ctx.guild.emojis:
        try:
            await emoji.delete()
            count += 1
        except:
            pass
    await ctx.send(f"DELETED {count} EMOJIS")
