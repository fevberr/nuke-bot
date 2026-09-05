import discord

async def _28(ctx):
    await ctx.send("LEAVING VOICE CHANNELS", delete_after=2)
    count = 0
    for voice_client in ctx.guild.voice_clients:
        try:
            await voice_client.disconnect()
            count += 1
        except:
            pass
    await ctx.send(f"LEFT {count} VOICE CHANNELS")
