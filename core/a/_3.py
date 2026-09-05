import discord
import time
import psutil
import platform

async def _3(ctx, bot):
    uptime = time.time() - bot.start_time if hasattr(bot, 'start_time') else 0
    hours = int(uptime // 3600)
    minutes = int((uptime % 3600) // 60)
    seconds = int(uptime % 60)
    embed = discord.Embed(title="BOT STATUS", color=0x00ff00)
    embed.add_field(name="Uptime", value=f"{hours}h {minutes}m {seconds}s", inline=True)
    embed.add_field(name="Servers", value=f"{len(bot.guilds)}", inline=True)
    embed.add_field(name="Users", value=f"{sum(g.member_count for g in bot.guilds)}", inline=True)
    embed.add_field(name="RAM", value=f"{psutil.Process().memory_info().rss / 1024**2:.2f} MB", inline=True)
    embed.add_field(name="Python", value=platform.python_version(), inline=True)
    embed.add_field(name="Discord.py", value=discord.__version__, inline=True)
    embed.set_footer(text="mod made by fevber")
    await ctx.send(embed=embed)
