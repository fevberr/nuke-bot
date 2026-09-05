import discord

async def _4(ctx):
    embed = discord.Embed(title="COMMANDS - USE NUMBERS 1-70", description="Type a number to execute", color=0x00ff00)
    embed.add_field(name="1-10", value="NUKE, CONFIG, STATUS, HELP, STOP, BANALL, KICKALL, ROLENUKE, WEBHOOKSPAM, CHANNELSPAM", inline=False)
    embed.add_field(name="11-20", value="EMOJIDELETE, STICKERDELETE, VOICECRASH, ADMINSTEAL, INVITEGEN, MESSAGESPAM, DMSPAM, ROLEMASS, CHANNELDELETE, CHANNELCREATE", inline=False)
    embed.add_field(name="21-30", value="CHANNELLOCK, CHANNELUNLOCK, NICKALL, AVATARALL, BOOST, REACTIONSPAM, VOICEJOIN, VOICELEAVE, MUTE, DEAFEN", inline=False)
    embed.add_field(name="31-40", value="SOFTBAN, HACKBAN, UNBAN, WARN, CLEAR, MENTIONSPAM, FILESPAM, EMBEDSPAM, STICKERSPAM, VOICEMOVE", inline=False)
    embed.add_field(name="41-50", value="VOICECREATE, VOICEDELETE, ROLECREATE, ROLEDELETE, ROLEASSIGN, ROLEREMOVE, CHANNELCLONE, CHANNELRENAME, CHANNELPOSITION, ROLEALL", inline=False)
    embed.add_field(name="51-60", value="MENTIONALL, MEMBERINFO, PING, SERVERINFO, USERINFO, UPTIME, RELOAD, GUILDICON, GUILDNAME, GUILDREGION", inline=False)
    embed.add_field(name="61-70", value="GUILDVANITY, GUILDSPLASH, EMOJISTEAL, EMOJICREATE, STICKERCREATE, REACT, DM, MESSAGEEDIT, MESSAGEDELETE, ADMIN", inline=False)
    embed.set_footer(text="mod made by fevber")
    await ctx.send(embed=embed)
