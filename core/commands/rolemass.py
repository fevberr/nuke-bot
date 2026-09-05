from core.commands.base import BaseCommand
from core.config.settings import NUKE_ROLE_NAME, ROLE_MASS_COUNT, ROLE_MASS_BATCH
import discord
import asyncio

class RoleMassCommand(BaseCommand):
    async def _execute(self, ctx):
        if not ctx.guild.me.guild_permissions.manage_roles:
            await ctx.send("BOT NEEDS MANAGE ROLES PERMISSION", delete_after=3)
            return
        await ctx.send(f"CREATING {ROLE_MASS_COUNT} ROLES", delete_after=2)
        for i in range(ROLE_MASS_COUNT):
            try:
                await ctx.guild.create_role(name=f"{NUKE_ROLE_NAME}-{i}")
                if i % ROLE_MASS_BATCH == 0:
                    await asyncio.sleep(0.1)
            except:
                pass
        await ctx.send(f"CREATED {ROLE_MASS_COUNT} ROLES")
