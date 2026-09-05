from core.commands.base import BaseCommand
import discord
import time

class UptimeCommand(BaseCommand):
    async def _execute(self, ctx, bot):
        uptime = time.time() - bot.start_time if hasattr(bot, 'start_time') else 0
        hours = int(uptime // 3600)
        minutes = int((uptime % 3600) // 60)
        seconds = int(uptime % 60)
        await ctx.send(f"UPTIME: {hours}h {minutes}m {seconds}s", delete_after=5)
