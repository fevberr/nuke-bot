import discord

async def _59(ctx):
    if not ctx.guild.me.guild_permissions.manage_guild:
        await ctx.send("BOT NEEDS MANAGE GUILD PERMISSION", delete_after=3)
        return
    await ctx.send("CHANGING GUILD NAME - ENTER NEW NAME", delete_after=2)
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel
    try:
        msg = await bot.wait_for('message', timeout=30, check=check)
        await ctx.guild.edit(name=msg.content)
        await ctx.send(f"GUILD NAME CHANGED TO {msg.content}", delete_after=2)
    except:
        await ctx.send("TIMEOUT", delete_after=3)
