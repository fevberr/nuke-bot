import discord

async def _38(ctx):
    if not ctx.guild.me.guild_permissions.send_messages:
        await ctx.send("BOT NEEDS SEND MESSAGES PERMISSION", delete_after=3)
        return
    await ctx.send("EMBED SPAMMING", delete_after=2)
    embed = discord.Embed(title="SPAM", description="This is spam", color=0xFF0000)
    for i in range(50):
        await ctx.send(embed=embed)
