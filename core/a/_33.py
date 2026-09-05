import discord

async def _33(ctx):
    await ctx.send("UNBAN - ENTER USER ID", delete_after=2)
    def check(m):
        return m.author == ctx.author and m.channel == ctx.channel
    try:
        msg = await bot.wait_for('message', timeout=30, check=check)
        user_id = int(msg.content)
        user = await bot.fetch_user(user_id)
        await ctx.guild.unban(user)
        await ctx.send(f"UNBANNED USER {user.name}")
    except:
        await ctx.send("TIMEOUT OR INVALID ID", delete_after=3)
