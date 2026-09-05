from core.config.settings import *
from core.logger.logger import Logger

logger = Logger()

class BaseCommand:
    async def execute(self, ctx):
        if not ctx.author.guild_permissions.administrator:
            await ctx.send("ADMIN PERMISSION REQUIRED", delete_after=3)
            return
        await self._execute(ctx)
    
    async def _execute(self, ctx):
        raise NotImplementedError
