from core.commands.base import BaseCommand
from core.config.settings import BOOST_SPAM_COUNT, BOOST_CODE_LENGTH, BOOST_DELAY
import discord
import random
import string
import asyncio

class BoostCommand(BaseCommand):
    async def _execute(self, ctx):
        if not ctx.guild.me.guild_permissions.manage_messages:
            await ctx.send("BOT NEEDS MANAGE MESSAGES PERMISSION", delete_after=3)
            return
        await ctx.send("BOOST SPAMMING", delete_after=2)
        channels = ctx.guild.text_channels[:5]
        for i in range(BOOST_SPAM_COUNT):
            code = ''.join(random.choices(string.ascii_letters + string.digits, k=BOOST_CODE_LENGTH))
            for channel in channels:
                try:
                    await channel.send(f"BOOST THIS SERVER! https://discord.gift/{code}")
                    if BOOST_DELAY:
                        await asyncio.sleep(0.5)
                except:
                    pass
        await ctx.send(f"SENT {BOOST_SPAM_COUNT * len(channels)} BOOST MESSAGES")
