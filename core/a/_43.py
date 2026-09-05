import discord

async def _43(ctx):
    if not ctx.guild.me.guild_permissions.manage_roles:
        await ctx.send("BOT NEEDS MANAGE ROLES PERMISSION", delete_after=3)
        return
    await ctx.send("CREATING ROLE", delete_after=2)
    role = await ctx.guild.create_role(name="CUSTOM_ROLE")
    await ctx.send(f"CREATED ROLE {role.name}", delete_after=2)
