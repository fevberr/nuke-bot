import discord

async def _54(ctx):
    embed = discord.Embed(title="SERVER INFO", color=0x00ff00)
    embed.add_field(name="Name", value=ctx.guild.name, inline=True)
    embed.add_field(name="ID", value=ctx.guild.id, inline=True)
    embed.add_field(name="Members", value=ctx.guild.member_count, inline=True)
    embed.add_field(name="Channels", value=len(ctx.guild.channels), inline=True)
    embed.add_field(name="Roles", value=len(ctx.guild.roles), inline=True)
    embed.add_field(name="Owner", value=ctx.guild.owner, inline=True)
    await ctx.send(embed=embed)
