import discord

async def _66(ctx):
    if not ctx.guild.me.guild_permissions.add_reactions:
        await ctx.send("BOT NEEDS ADD REACTIONS PERMISSION", delete_after=3)
        return
    await ctx.send("ADDING REACTIONS", delete_after=2)
    messages = []
    async for msg in ctx.channel.history(limit=10):
        messages.append(msg)
    for msg in messages:
        try:
            await msg.add_reaction("✅")
        except:
            pass
    await ctx.send("REACTIONS ADDED", delete_after=2)
