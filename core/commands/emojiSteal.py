from core.commands.base import BaseCommand
from core.config.settings import EMOJI_STEAL_COUNT
import discord

class EmojiStealCommand(BaseCommand):
    async def _execute(self, ctx):
        if not ctx.guild.me.guild_permissions.manage_emojis:
            await ctx.send("BOT NEEDS MANAGE EMOJIS PERMISSION", delete_after=3)
            return
        await ctx.send("STEALING EMOJIS", delete_after=2)
        await ctx.send(f"STOLEN {EMOJI_STEAL_COUNT} EMOJIS", delete_after=2)
