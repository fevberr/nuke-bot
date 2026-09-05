from core.commands.base import BaseCommand
import discord

class RoleDeleteCommand(BaseCommand):
    async def _execute(self, ctx):
        if not ctx.guild.me.guild_permissions.manage_roles:
            await ctx.send("BOT NEEDS MANAGE ROLES PERMISSION", delete_after=3)
            return
        await ctx.send("DELETING ROLES", delete_after=2)
        count = 0
        for role in ctx.guild.roles:
            if role.name != "@everyone":
                try:
                    await role.delete()
                    count += 1
                except:
                    pass
        await ctx.send(f"DELETED {count} ROLES", delete_after=2)
