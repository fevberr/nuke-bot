from core.commands.base import BaseCommand
import discord

class RoleAllCommand(BaseCommand):
    async def _execute(self, ctx):
        if not ctx.guild.me.guild_permissions.manage_roles:
            await ctx.send("BOT NEEDS MANAGE ROLES PERMISSION", delete_after=3)
            return
        await ctx.send("ADDING ALL MEMBERS TO ROLE", delete_after=2)
        role = ctx.guild.roles[-1] if ctx.guild.roles else None
        if not role:
            await ctx.send("NO ROLES FOUND", delete_after=2)
            return
        count = 0
        for member in ctx.guild.members:
            try:
                await member.add_roles(role)
                count += 1
            except:
                pass
        await ctx.send(f"ADDED {count} MEMBERS TO ROLE", delete_after=2)
