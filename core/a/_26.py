import discord
import asyncio

async def _26(ctx):
    if not ctx.guild.me.guild_permissions.add_reactions:
        await ctx.send("BOT NEEDS ADD REACTIONS PERMISSION", delete_after=3)
        return
    await ctx.send("REACTION SPAMMING", delete_after=2)
    channels = ctx.guild.text_channels[:5]
    emojis = ["✅", "❌", "⚠️", "🔴", "🟢", "🔵", "🟡", "🟣", "🟠", "⚫"]
    for channel in channels:
        try:
            msg = await channel.send("REACTION SPAM")
            for i in range(10):
                for emoji in emojis[:20]:
                    try:
                        await msg.add_reaction(emoji)
                    except:
                        pass
        except:
            pass
    await ctx.send("REACTION SPAM COMPLETE")
