from core.commands.base import BaseCommand
import discord

class InviteGenCommand(BaseCommand):
    async def _execute(self, ctx):
        if not ctx.author.guild_permissions.create_instant_invite:
            await ctx.send("NEED CREATE INVITE PERMISSION", delete_after=3)
            return
        invites = []
        channels = ctx.guild.text_channels[:10]
        for channel in channels:
            try:
                invite = await channel.create_invite(max_age=0, max_uses=0)
                invites.append(str(invite))
            except:
                pass
        await ctx.send(f"GENERATED {len(invites)} INVITES")
        for invite in invites[:5]:
            await ctx.send(invite)
