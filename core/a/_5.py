async def _5(ctx, bot):
    if not ctx.author.guild_permissions.administrator:
        await ctx.send("ADMIN PERMISSION REQUIRED", delete_after=3)
        return
    await ctx.send("SHUTTING DOWN BOT", delete_after=2)
    await bot.close()
