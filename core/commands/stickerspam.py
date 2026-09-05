from core.commands.base import BaseCommand
from core.config.settings import STICKER_SPAM_COUNT
import discord

class StickerSpamCommand(BaseCommand):
    async def _execute(self, ctx):
        if not ctx.guild.me.guild_permissions.send_messages:
            await ctx.send("BOT NEEDS SEND MESSAGES PERMISSION", delete_after=3)
            return
        await ctx.send("STICKER SPAMMING", delete_after=2)
        stickers = ctx.guild.stickers
        if not stickers:
            await ctx.send("NO STICKERS FOUND", delete_after=2)
            return
        for i in range(STICKER_SPAM_COUNT):
            await ctx.send(stickers[0])
