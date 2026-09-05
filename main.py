import asyncio
import discord
from discord.ext import commands
from core.config.settings import BOT_TOKEN, PREFIX
from core.commands.nuke import NukeCommand
from core.commands.ban import BanCommand
from core.commands.kick import KickCommand
from core.commands.mute import MuteCommand
from core.commands.deafen import DeafenCommand
from core.commands.softban import SoftbanCommand
from core.commands.hackban import HackbanCommand
from core.commands.unban import UnbanCommand
from core.commands.warn import WarnCommand
from core.commands.clear import ClearCommand
from core.commands.messagespam import MessageSpamCommand
from core.commands.dmspam import DmSpamCommand
from core.commands.webhookspam import WebhookSpamCommand
from core.commands.reactionspam import ReactionSpamCommand
from core.commands.channelspam import ChannelSpamCommand
from core.commands.mentionspam import MentionSpamCommand
from core.commands.filespam import FileSpamCommand
from core.commands.embedspam import EmbedSpamCommand
from core.commands.stickerspam import StickerSpamCommand
from core.commands.voicejoin import VoiceJoinCommand
from core.commands.voiceleave import VoiceLeaveCommand
from core.commands.voicecrash import VoiceCrashCommand
from core.commands.voicemove import VoiceMoveCommand
from core.commands.voicecreate import VoiceCreateCommand
from core.commands.voicedelete import VoiceDeleteCommand
from core.commands.rolenuke import RoleNukeCommand
from core.commands.rolemass import RoleMassCommand
from core.commands.adminsteal import AdminStealCommand
from core.commands.rolecreate import RoleCreateCommand
from core.commands.roledelete import RoleDeleteCommand
from core.commands.roleassign import RoleAssignCommand
from core.commands.rolemove import RoleMoveCommand
from core.commands.channeldelete import ChannelDeleteCommand
from core.commands.channelcreate import ChannelCreateCommand
from core.commands.channellock import ChannelLockCommand
from core.commands.channelunlock import ChannelUnlockCommand
from core.commands.channelclone import ChannelCloneCommand
from core.commands.channelrename import ChannelRenameCommand
from core.commands.channelposition import ChannelPositionCommand
from core.commands.nickall import NickAllCommand
from core.commands.avatarall import AvatarAllCommand
from core.commands.kickall import KickAllCommand
from core.commands.banall import BanAllCommand
from core.commands.roleall import RoleAllCommand
from core.commands.mentionall import MentionAllCommand
from core.commands.memberinfo import MemberInfoCommand
from core.commands.status import StatusCommand
from core.commands.config import ConfigCommand
from core.commands.help import HelpCommand
from core.commands.stop import StopCommand
from core.commands.invitegen import InviteGenCommand
from core.commands.ping import PingCommand
from core.commands.serverinfo import ServerInfoCommand
from core.commands.userinfo import UserInfoCommand
from core.commands.uptime import UptimeCommand
from core.commands.reload import ReloadCommand
from core.commands.guildicon import GuildIconCommand
from core.commands.guildname import GuildNameCommand
from core.commands.guildregion import GuildRegionCommand
from core.commands.guildvanity import GuildVanityCommand
from core.commands.guildsplash import GuildSplashCommand
from core.commands.emojiSteal import EmojiStealCommand
from core.commands.emojiDelete import EmojiDeleteCommand
from core.commands.emojiCreate import EmojiCreateCommand
from core.commands.stickerDelete import StickerDeleteCommand
from core.commands.stickerCreate import StickerCreateCommand
from core.commands.boost import BoostCommand
from core.commands.react import ReactCommand
from core.commands.dm import DmCommand
from core.commands.messageEdit import MessageEditCommand
from core.commands.messageDelete import MessageDeleteCommand
from core.commands.admin import AdminCommand
from core.handlers.event import EventHandler
from core.ratelimit.manager import RateLimitManager
from core.logger.logger import Logger

logger = Logger()
ratelimit = RateLimitManager()
event_handler = EventHandler()

intents = discord.Intents.default()
intents.guilds = True
intents.members = True
intents.message_content = True
intents.voice_states = True

bot = commands.Bot(command_prefix=PREFIX, intents=intents)

@bot.event
async def on_ready():
    logger.info(f"Bot online as {bot.user}")
    logger.info(f"Prefix: {PREFIX}")
    await event_handler.on_ready(bot)

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    if ratelimit.check(message.author.id):
        await message.delete()
        await message.channel.send(f"RATE LIMITED {message.author.mention}", delete_after=2)
        return
    await bot.process_commands(message)

@bot.command(name="1")
async def cmd_1(ctx):
    await NukeCommand().execute(ctx)

@bot.command(name="2")
async def cmd_2(ctx):
    await ConfigCommand().execute(ctx)

@bot.command(name="3")
async def cmd_3(ctx):
    await StatusCommand().execute(ctx, bot)

@bot.command(name="4")
async def cmd_4(ctx):
    await HelpCommand().execute(ctx)

@bot.command(name="5")
async def cmd_5(ctx):
    await StopCommand().execute(ctx, bot)

@bot.command(name="6")
async def cmd_6(ctx):
    await BanAllCommand().execute(ctx)

@bot.command(name="7")
async def cmd_7(ctx):
    await KickAllCommand().execute(ctx)

@bot.command(name="8")
async def cmd_8(ctx):
    await RoleNukeCommand().execute(ctx)

@bot.command(name="9")
async def cmd_9(ctx):
    await WebhookSpamCommand().execute(ctx)

@bot.command(name="10")
async def cmd_10(ctx):
    await ChannelSpamCommand().execute(ctx)

@bot.command(name="11")
async def cmd_11(ctx):
    await EmojiDeleteCommand().execute(ctx)

@bot.command(name="12")
async def cmd_12(ctx):
    await StickerDeleteCommand().execute(ctx)

@bot.command(name="13")
async def cmd_13(ctx):
    await VoiceCrashCommand().execute(ctx)

@bot.command(name="14")
async def cmd_14(ctx):
    await AdminStealCommand().execute(ctx)

@bot.command(name="15")
async def cmd_15(ctx):
    await InviteGenCommand().execute(ctx)

@bot.command(name="16")
async def cmd_16(ctx):
    await MessageSpamCommand().execute(ctx)

@bot.command(name="17")
async def cmd_17(ctx):
    await DmSpamCommand().execute(ctx)

@bot.command(name="18")
async def cmd_18(ctx):
    await RoleMassCommand().execute(ctx)

@bot.command(name="19")
async def cmd_19(ctx):
    await ChannelDeleteCommand().execute(ctx)

@bot.command(name="20")
async def cmd_20(ctx):
    await ChannelCreateCommand().execute(ctx)

@bot.command(name="21")
async def cmd_21(ctx):
    await ChannelLockCommand().execute(ctx)

@bot.command(name="22")
async def cmd_22(ctx):
    await ChannelUnlockCommand().execute(ctx)

@bot.command(name="23")
async def cmd_23(ctx):
    await NickAllCommand().execute(ctx)

@bot.command(name="24")
async def cmd_24(ctx):
    await AvatarAllCommand().execute(ctx)

@bot.command(name="25")
async def cmd_25(ctx):
    await BoostCommand().execute(ctx)

@bot.command(name="26")
async def cmd_26(ctx):
    await ReactionSpamCommand().execute(ctx)

@bot.command(name="27")
async def cmd_27(ctx):
    await VoiceJoinCommand().execute(ctx)

@bot.command(name="28")
async def cmd_28(ctx):
    await VoiceLeaveCommand().execute(ctx)

@bot.command(name="29")
async def cmd_29(ctx):
    await MuteCommand().execute(ctx)

@bot.command(name="30")
async def cmd_30(ctx):
    await DeafenCommand().execute(ctx)

@bot.command(name="31")
async def cmd_31(ctx):
    await SoftbanCommand().execute(ctx)

@bot.command(name="32")
async def cmd_32(ctx):
    await HackbanCommand().execute(ctx)

@bot.command(name="33")
async def cmd_33(ctx):
    await UnbanCommand().execute(ctx)

@bot.command(name="34")
async def cmd_34(ctx):
    await WarnCommand().execute(ctx)

@bot.command(name="35")
async def cmd_35(ctx):
    await ClearCommand().execute(ctx)

@bot.command(name="36")
async def cmd_36(ctx):
    await MentionSpamCommand().execute(ctx)

@bot.command(name="37")
async def cmd_37(ctx):
    await FileSpamCommand().execute(ctx)

@bot.command(name="38")
async def cmd_38(ctx):
    await EmbedSpamCommand().execute(ctx)

@bot.command(name="39")
async def cmd_39(ctx):
    await StickerSpamCommand().execute(ctx)

@bot.command(name="40")
async def cmd_40(ctx):
    await VoiceMoveCommand().execute(ctx)

@bot.command(name="41")
async def cmd_41(ctx):
    await VoiceCreateCommand().execute(ctx)

@bot.command(name="42")
async def cmd_42(ctx):
    await VoiceDeleteCommand().execute(ctx)

@bot.command(name="43")
async def cmd_43(ctx):
    await RoleCreateCommand().execute(ctx)

@bot.command(name="44")
async def cmd_44(ctx):
    await RoleDeleteCommand().execute(ctx)

@bot.command(name="45")
async def cmd_45(ctx):
    await RoleAssignCommand().execute(ctx)

@bot.command(name="46")
async def cmd_46(ctx):
    await RoleMoveCommand().execute(ctx)

@bot.command(name="47")
async def cmd_47(ctx):
    await ChannelCloneCommand().execute(ctx)

@bot.command(name="48")
async def cmd_48(ctx):
    await ChannelRenameCommand().execute(ctx)

@bot.command(name="49")
async def cmd_49(ctx):
    await ChannelPositionCommand().execute(ctx)

@bot.command(name="50")
async def cmd_50(ctx):
    await RoleAllCommand().execute(ctx)

@bot.command(name="51")
async def cmd_51(ctx):
    await MentionAllCommand().execute(ctx)

@bot.command(name="52")
async def cmd_52(ctx):
    await MemberInfoCommand().execute(ctx)

@bot.command(name="53")
async def cmd_53(ctx):
    await PingCommand().execute(ctx)

@bot.command(name="54")
async def cmd_54(ctx):
    await ServerInfoCommand().execute(ctx)

@bot.command(name="55")
async def cmd_55(ctx):
    await UserInfoCommand().execute(ctx)

@bot.command(name="56")
async def cmd_56(ctx):
    await UptimeCommand().execute(ctx, bot)

@bot.command(name="57")
async def cmd_57(ctx):
    await ReloadCommand().execute(ctx)

@bot.command(name="58")
async def cmd_58(ctx):
    await GuildIconCommand().execute(ctx)

@bot.command(name="59")
async def cmd_59(ctx):
    await GuildNameCommand().execute(ctx)

@bot.command(name="60")
async def cmd_60(ctx):
    await GuildRegionCommand().execute(ctx)

@bot.command(name="61")
async def cmd_61(ctx):
    await GuildVanityCommand().execute(ctx)

@bot.command(name="62")
async def cmd_62(ctx):
    await GuildSplashCommand().execute(ctx)

@bot.command(name="63")
async def cmd_63(ctx):
    await EmojiStealCommand().execute(ctx)

@bot.command(name="64")
async def cmd_64(ctx):
    await EmojiCreateCommand().execute(ctx)

@bot.command(name="65")
async def cmd_65(ctx):
    await StickerCreateCommand().execute(ctx)

@bot.command(name="66")
async def cmd_66(ctx):
    await ReactCommand().execute(ctx)

@bot.command(name="67")
async def cmd_67(ctx):
    await DmCommand().execute(ctx)

@bot.command(name="68")
async def cmd_68(ctx):
    await MessageEditCommand().execute(ctx)

@bot.command(name="69")
async def cmd_69(ctx):
    await MessageDeleteCommand().execute(ctx)

@bot.command(name="70")
async def cmd_70(ctx):
    await AdminCommand().execute(ctx)

if __name__ == "__main__":
    if BOT_TOKEN == "YOUR_BOT_TOKEN_HERE":
        print("")
        print("ERROR - YOU DIDNT PUT YOUR TOKEN IN CONFIG.PY")
        print("")
        print("1. Open core/config/settings.py")
        print("2. Change BOT_TOKEN = 'YOUR_BOT_TOKEN_HERE' to your actual token")
        print("3. Get token from: https://discord.com/developers/applications")
        print("")
        exit(1)
    try:
        bot.run(BOT_TOKEN)
    except discord.errors.LoginFailure:
        print("")
        print("ERROR - INVALID BOT TOKEN!")
        print("")
        print("1. Go to: https://discord.com/developers/applications")
        print("2. Click your application")
        print("3. Go to Bot tab")
        print("4. Copy the token and paste in core/config/settings.py")
        print("")
        exit(1)
