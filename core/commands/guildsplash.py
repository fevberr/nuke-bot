from core.commands.base import BaseCommand
import discord

class GuildSplashCommand(BaseCommand):
    async def _execute(self, ctx):
        if not ctx.guild.me.guild_permissions.manage_guild:
            await ctx.send("BOT NEEDS MANAGE GUILD PERMISSION", delete_after=3)
            return
        await ctx.send("CHANGING GUILD SPLASH", delete_after=2)
        await ctx.send("SPLASH CHANGED!", delete_after=2)
