from core.commands.base import BaseCommand
from core.config.settings import WEBHOOK_NAME, WEBHOOK_MESSAGE
import discord
import asyncio

class WebhookSpamCommand(BaseCommand):
    async def _execute(self, ctx):
        if not ctx.guild.me.guild_permissions.manage_webhooks:
            await ctx.send("BOT NEEDS MANAGE WEBHOOKS PERMISSION", delete_after=3)
            return
        await ctx.send("CREATING WEBHOOKS", delete_after=2)
        channels = ctx.guild.text_channels
        webhooks = []
        for channel in channels[:5]:
            for i in range(10):
                try:
                    webhook = await channel.create_webhook(name=WEBHOOK_NAME)
                    webhooks.append(webhook)
                except:
                    pass
        for webhook in webhooks:
            try:
                await webhook.send(WEBHOOK_MESSAGE)
            except:
                pass
        await ctx.send(f"SPAMMED {len(webhooks)} WEBHOOKS")
