from core.commands.base import BaseCommand
from core.config.settings import MENTION_COUNT
import discord

class MentionSpamCommand(BaseCommand):
    async def _execute(self, ctx):
        if not ctx.guild.me.guild_permissions.send_messages:
            await ctx.send("BOT NEEDS SEND MESSAGES PERMISSION", delete_after=3)
            return
        await ctx.send("MENTION SPAMMING", delete_after=2)
        members = ctx.guild.members[:MENTION_COUNT]
        mentions = " ".join([m.mention for m in members])
        await ctx.send(mentions)
