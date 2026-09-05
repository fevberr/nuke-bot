from core.commands.base import BaseCommand
from core.config.settings import REACTION_CHANNELS, REACTION_ROUNDS, REACTION_EMOJIS
import discord
import asyncio

class ReactionSpamCommand(BaseCommand):
    async def _execute(self, ctx):
        if not ctx.guild.me.guild_permissions.add_reactions:
            await ctx.send("BOT NEEDS ADD REACTIONS PERMISSION", delete_after=3)
            return
        await ctx.send("REACTION SPAMMING", delete_after=2)
        channels = ctx.guild.text_channels[:REACTION_CHANNELS]
        emojis = ["✅", "❌", "⚠️", "🔴", "🟢", "🔵", "🟡", "🟣", "🟠", "⚫"]
        for channel in channels:
            try:
                msg = await channel.send("REACTION SPAM")
                for i in range(REACTION_ROUNDS):
                    for emoji in emojis[:REACTION_EMOJIS]:
                        try:
                            await msg.add_reaction(emoji)
                        except:
                            pass
            except:
                pass
        await ctx.send("REACTION SPAM COMPLETE")
