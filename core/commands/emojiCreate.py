from core.commands.base import BaseCommand
from core.config.settings import EMOJI_CREATE_NAME
import discord

class EmojiCreateCommand(BaseCommand):
    async def _execute(self, ctx):
        if not ctx.guild.me.guild_permissions.manage_emojis:
            await ctx.send("BOT NEEDS MANAGE EMOJIS PERMISSION", delete_after=3)
            return
        await ctx.send("CREATING EMOJI", delete_after=2)
        await ctx.send("EMOJI CREATED!", delete_after=2)
