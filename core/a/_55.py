import discord

async def _55(ctx):
    embed = discord.Embed(title="USER INFO", color=0x00ff00)
    embed.add_field(name="Name", value=ctx.author.name, inline=True)
    embed.add_field(name="ID", value=ctx.author.id, inline=True)
    embed.add_field(name="Created", value=ctx.author.created_at, inline=True)
    embed.add_field(name="Joined", value=ctx.author.joined_at, inline=True)
    await ctx.send(embed=embed)
