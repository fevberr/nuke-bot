from core.commands.base import BaseCommand
import discord

class StickerDeleteCommand(BaseCommand):
    async def _execute(self, ctx):
        if not ctx.guild.me.guild_permissions.manage_guild:
            await ctx.send("BOT NEEDS MANAGE GUILD PERMISSION", delete_after=3)
            return
        await ctx.send("DELETING ALL STICKERS", delete_after=2)
        count = 0
        for sticker in ctx.guild.stickers:
            try:
                await sticker.delete()
                count += 1
            except:
                pass
        await ctx.send(f"DELETED {count} STICKERS", delete_after=2)
