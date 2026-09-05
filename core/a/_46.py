import discord

async def _46(ctx):
    if not ctx.guild.me.guild_permissions.manage_roles:
        await ctx.send("BOT NEEDS MANAGE ROLES PERMISSION", delete_after=3)
        return
    await ctx.send("REMOVING ROLE FROM ALL MEMBERS", delete_after=2)
    role = ctx.guild.roles[-1] if ctx.guild.roles else None
    if not role:
        await ctx.send("NO ROLES FOUND", delete_after=2)
        return
    count = 0
    for member in ctx.guild.members:
        try:
            await member.remove_roles(role)
            count += 1
        except:
            pass
    await ctx.send(f"REMOVED ROLE FROM {count} MEMBERS", delete_after=2)
