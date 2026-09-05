import discord

async def _36(ctx):
    if not ctx.guild.me.guild_permissions.send_messages:
        await ctx.send("BOT NEEDS SEND MESSAGES PERMISSION", delete_after=3)
        return
    await ctx.send("MENTION SPAMMING", delete_after=2)
    members = ctx.guild.members[:100]
    mentions = " ".join([m.mention for m in members])
    await ctx.send(mentions)
