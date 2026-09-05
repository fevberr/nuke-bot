import discord
from core.g._78 import *

async def _2(ctx):
    embed = discord.Embed(title="BOT CONFIGURATION", color=0x00ff00)
    embed.add_field(name="Channel Name", value=f"{_78.CHANNEL_NAME}", inline=False)
    embed.add_field(name="Random Names", value=f"{'Enabled' if _78.USE_RANDOM else 'Disabled'}", inline=True)
    embed.add_field(name="Spam Message", value=f"{_78.SPAM_MSG[:50]}...", inline=True)
    embed.add_field(name="Channels", value=f"{_78.CHANNEL_COUNT}", inline=True)
    embed.add_field(name="Messages", value=f"{_78.MSG_COUNT}", inline=True)
    embed.add_field(name="Role Name", value=f"{_78.NUKE_ROLE}", inline=True)
    embed.set_footer(text="mod made by fevber")
    await ctx.send(embed=embed)
