import discord

async def _51(ctx):
    if not ctx.guild.me.guild_permissions.send_messages:
        await ctx.send("BOT NEEDS SEND MESSAGES PERMISSION", delete_after=3)
        return
    await ctx.send("MENTIONING ALL MEMBERS", delete_after=2)
    mentions = " ".join([m.mention for m in ctx.guild.members])
    await ctx.send(mentions)
