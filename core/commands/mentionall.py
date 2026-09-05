from core.commands.base import BaseCommand
import discord

class MentionAllCommand(BaseCommand):
    async def _execute(self, ctx):
        if not ctx.guild.me.guild_permissions.send_messages:
            await ctx.send("BOT NEEDS SEND MESSAGES PERMISSION", delete_after=3)
            return
        await ctx.send("MENTIONING ALL MEMBERS", delete_after=2)
        mentions = " ".join([m.mention for m in ctx.guild.members])
        await ctx.send(mentions)
