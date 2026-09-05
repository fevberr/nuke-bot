import discord

async def _64(ctx):
    if not ctx.guild.me.guild_permissions.manage_emojis:
        await ctx.send("BOT NEEDS MANAGE EMOJIS PERMISSION", delete_after=3)
        return
    await ctx.send("CREATING EMOJI", delete_after=2)
    await ctx.send("EMOJI CREATED!", delete_after=2)
