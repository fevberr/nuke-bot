import asyncio
import discord
from discord.ext import commands
from core.g._78 import BOT_TOKEN
from core.a._1 import _1
from core.a._2 import _2
from core.a._3 import _3
from core.a._4 import _4
from core.a._5 import _5
from core.a._6 import _6
from core.a._7 import _7
from core.a._8 import _8
from core.a._9 import _9
from core.a._10 import _10
from core.a._11 import _11
from core.a._12 import _12
from core.a._13 import _13
from core.a._14 import _14
from core.a._15 import _15
from core.a._16 import _16
from core.a._17 import _17
from core.a._18 import _18
from core.a._19 import _19
from core.a._20 import _20
from core.a._21 import _21
from core.a._22 import _22
from core.a._23 import _23
from core.a._24 import _24
from core.a._25 import _25
from core.a._26 import _26
from core.a._27 import _27
from core.a._28 import _28
from core.a._29 import _29
from core.a._30 import _30
from core.a._31 import _31
from core.a._32 import _32
from core.a._33 import _33
from core.a._34 import _34
from core.a._35 import _35
from core.a._36 import _36
from core.a._37 import _37
from core.a._38 import _38
from core.a._39 import _39
from core.a._40 import _40
from core.a._41 import _41
from core.a._42 import _42
from core.a._43 import _43
from core.a._44 import _44
from core.a._45 import _45
from core.a._46 import _46
from core.a._47 import _47
from core.a._48 import _48
from core.a._49 import _49
from core.a._50 import _50
from core.a._51 import _51
from core.a._52 import _52
from core.a._53 import _53
from core.a._54 import _54
from core.a._55 import _55
from core.a._56 import _56
from core.a._57 import _57
from core.a._58 import _58
from core.a._59 import _59
from core.a._60 import _60
from core.a._61 import _61
from core.a._62 import _62
from core.a._63 import _63
from core.a._64 import _64
from core.a._65 import _65
from core.a._66 import _66
from core.a._67 import _67
from core.a._68 import _68
from core.a._69 import _69
from core.a._70 import _70
from core.b._71 import _71
from core.b._72 import _72
from core.b._73 import _73
from core.c._74 import _74
from core.f._77 import _77

DRAGON = r'''
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡠⠔⠒⠊⠉⠉⠉⠉⠙⠋⠛⠻⠶⣢⢄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠔⠊⠁⠉⠀⠀⠀⠀⠀⠀⠀⠀⢰⡆⠀⠀⣈⣑⢌⠳⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣜⠁⣀⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡊⣟⢿⣷⡌⠳⡄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⡷⠊⡁⠀⠀⠀⠀⣀⣠⠤⠤⠖⠒⠒⠒⠒⠐⠒⣓⡛⠊⠈⢷⢤⠜⢆⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⣿⣷⡯⠟⢀⡄⠀⠈⠁⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣙⣁⣂⣀⡀⠹⠕⡢⢝⡢⢄⡀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⣯⣴⠞⠁⠀⠀⣤⠀⠀⢀⣀⡠⣴⣶⡋⠉⠩⢿⡧⠤⠹⣿⣿⣿⣿⣶⣶⣬⣝⣻⢦⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⡿⠋⠀⠀⠀⠀⢀⣩⢴⣾⠟⠛⠙⠂⡇⠀⠀⠀⠈⢷⠐⠒⠻⣿⣿⣿⣿⣿⣿⣿⣿⣷⢵
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⡿⠋⠀⠀⠀⣀⣴⣾⡿⣿⡿⢿⣿⣶⡀⠈⠀⠀⠀⠀⠀⠀⢠⣤⣤⡘⡏⣿⣿⣿⣿⣿⣿⣿⡏
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⠫⠀⠀⣠⣴⣿⣿⣿⣿⡿⠋⣼⣿⣿⣽⣆⠀⠀⠀⠀⠀⠀⠀⣽⣿⣿⣟⣆⢹⣿⣿⣿⣿⣿⠏⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡜⢁⢀⣴⣿⣿⣿⣿⣿⣿⣿⢧⣄⢻⢟⣿⣿⠏⠀⠀⠀⠀⠀⠀⠀⣿⢿⣿⡿⢸⢸⣿⣿⣿⡟⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡎⣠⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⠀⠉⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⠋⠁⠈⢸⡞⠋⠈⢷⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡶⣿⣿⣿⣿⣿⣿⠷⢾⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⡼⡇⠀⠀⠈⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠿⠿⣿⣿⡿⣇⠘⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣧⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣶⠖⠒⠒⠛⠭⠷⣿⣿⣿⡀⠀⠀⠀⠀⠀⠀⠀⠒⠙⠀⠀⠀⠀⠀⢀⡠⣾⣿⣿⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⠀⠀⢀⣀⠀⠀⠀⠸⣿⣿⣿⣶⣦⣤⣄⣀⣀⠀⠀⢀⣀⣀⣤⣴⣾⣉⣀⣿⣿⡏⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢧⠀⠀⠈⠻⢷⣤⡀⠀⢿⢿⡿⣿⣿⣿⣿⣻⣶⡭⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣷⡤⣀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣆⠠⢀⠀⠀⠈⢙⣦⣁⠈⠧⣿⣿⣿⡉⠻⢿⣷⣾⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠟⠛⢋⢳⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⣾⡟⣿⡩⡤⠖⢾⠉⠀⠊⠳⢬⣸⣿⣿⣷⠂⠄⠙⢿⢿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠀⣀⣦⠃⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢏⠀⠀⢰⠛⠂⠘⡆⠀⢸⣿⣷⠙⣿⣿⣿⡇⠀⣠⠵⡭⠛⠿⡟⣿⣿⣿⡤⠖⠻⣻⡃⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⡄⢀⡏⠀⠐⠀⢹⡀⢸⣿⣟⠁⣿⣿⡟⣿⠚⠁⠀⢯⣀⠀⡎⠹⣿⣿⣿⡀⠄⠐⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⡼⠀⠀⠀⠀⠀⣇⢸⣿⡇⢀⣾⣿⣿⣿⣄⠀⠀⢸⡹⣿⣹⠯⣿⣿⣿⡇⠀⡸⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠋⠀⠀⠀⠀⠀⢸⣾⣿⣠⣿⡼⣿⣿⣿⣧⠤⣄⡀⣇⠙⠋⣇⠘⣿⣿⣿⣶⠃⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡎⠀⠀⠀⠀⠀⠀⠨⣿⣿⣿⡇⢴⣿⣿⣿⣿⣇⣸⡀⢸⠂⠀⢸⣶⣿⣿⣿⣟⡄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠰⠀⠀⠀⠠⢀⠀⣿⣿⣿⣯⣯⠉⣿⣿⣿⣿⡿⡉⣇⠌⡗⢛⢣⣽⣿⣿⣿⣿⣹⠀⠀⠀⠀⠀⠀⠀
'''

intents = discord.Intents.default()
intents.guilds = True
intents.members = True
intents.message_content = True
intents.voice_states = True

bot = commands.Bot(command_prefix=".", intents=intents)
_72_inst = _72()
_77_inst = _77()

@bot.event
async def on_ready():
    print(DRAGON)
    print("")
    _73(f"Bot online as {bot.user}")
    _73(f"Prefix: .")
    await _77_inst._78(bot)

@bot.event
async def on_message(message):
    if message.author.bot:
        return
    if _72_inst._73(message.author.id):
        await message.delete()
        await message.channel.send(f"RATE LIMITED {message.author.mention}", delete_after=2)
        return
    await bot.process_commands(message)

@bot.command(name="1")
async def _79(ctx): await _1(ctx)
@bot.command(name="2")
async def _80(ctx): await _2(ctx)
@bot.command(name="3")
async def _81(ctx): await _3(ctx, bot)
@bot.command(name="4")
async def _82(ctx): await _4(ctx)
@bot.command(name="5")
async def _83(ctx): await _5(ctx, bot)
@bot.command(name="6")
async def _84(ctx): await _6(ctx)
@bot.command(name="7")
async def _85(ctx): await _7(ctx)
@bot.command(name="8")
async def _86(ctx): await _8(ctx)
@bot.command(name="9")
async def _87(ctx): await _9(ctx)
@bot.command(name="10")
async def _88(ctx): await _10(ctx)
@bot.command(name="11")
async def _89(ctx): await _11(ctx)
@bot.command(name="12")
async def _90(ctx): await _12(ctx)
@bot.command(name="13")
async def _91(ctx): await _13(ctx)
@bot.command(name="14")
async def _92(ctx): await _14(ctx)
@bot.command(name="15")
async def _93(ctx): await _15(ctx)
@bot.command(name="16")
async def _94(ctx): await _16(ctx)
@bot.command(name="17")
async def _95(ctx): await _17(ctx)
@bot.command(name="18")
async def _96(ctx): await _18(ctx)
@bot.command(name="19")
async def _97(ctx): await _19(ctx)
@bot.command(name="20")
async def _98(ctx): await _20(ctx)
@bot.command(name="21")
async def _99(ctx): await _21(ctx)
@bot.command(name="22")
async def _100(ctx): await _22(ctx)
@bot.command(name="23")
async def _101(ctx): await _23(ctx)
@bot.command(name="24")
async def _102(ctx): await _24(ctx)
@bot.command(name="25")
async def _103(ctx): await _25(ctx)
@bot.command(name="26")
async def _104(ctx): await _26(ctx)
@bot.command(name="27")
async def _105(ctx): await _27(ctx)
@bot.command(name="28")
async def _106(ctx): await _28(ctx)
@bot.command(name="29")
async def _107(ctx): await _29(ctx)
@bot.command(name="30")
async def _108(ctx): await _30(ctx)
@bot.command(name="31")
async def _109(ctx): await _31(ctx)
@bot.command(name="32")
async def _110(ctx): await _32(ctx)
@bot.command(name="33")
async def _111(ctx): await _33(ctx)
@bot.command(name="34")
async def _112(ctx): await _34(ctx)
@bot.command(name="35")
async def _113(ctx): await _35(ctx)
@bot.command(name="36")
async def _114(ctx): await _36(ctx)
@bot.command(name="37")
async def _115(ctx): await _37(ctx)
@bot.command(name="38")
async def _116(ctx): await _38(ctx)
@bot.command(name="39")
async def _117(ctx): await _39(ctx)
@bot.command(name="40")
async def _118(ctx): await _40(ctx)
@bot.command(name="41")
async def _119(ctx): await _41(ctx)
@bot.command(name="42")
async def _120(ctx): await _42(ctx)
@bot.command(name="43")
async def _121(ctx): await _43(ctx)
@bot.command(name="44")
async def _122(ctx): await _44(ctx)
@bot.command(name="45")
async def _123(ctx): await _45(ctx)
@bot.command(name="46")
async def _124(ctx): await _46(ctx)
@bot.command(name="47")
async def _125(ctx): await _47(ctx)
@bot.command(name="48")
async def _126(ctx): await _48(ctx)
@bot.command(name="49")
async def _127(ctx): await _49(ctx)
@bot.command(name="50")
async def _128(ctx): await _50(ctx)
@bot.command(name="51")
async def _129(ctx): await _51(ctx)
@bot.command(name="52")
async def _130(ctx): await _52(ctx)
@bot.command(name="53")
async def _131(ctx): await _53(ctx)
@bot.command(name="54")
async def _132(ctx): await _54(ctx)
@bot.command(name="55")
async def _133(ctx): await _55(ctx)
@bot.command(name="56")
async def _134(ctx): await _56(ctx, bot)
@bot.command(name="57")
async def _135(ctx): await _57(ctx)
@bot.command(name="58")
async def _136(ctx): await _58(ctx)
@bot.command(name="59")
async def _137(ctx): await _59(ctx)
@bot.command(name="60")
async def _138(ctx): await _60(ctx)
@bot.command(name="61")
async def _139(ctx): await _61(ctx)
@bot.command(name="62")
async def _140(ctx): await _62(ctx)
@bot.command(name="63")
async def _141(ctx): await _63(ctx)
@bot.command(name="64")
async def _142(ctx): await _64(ctx)
@bot.command(name="65")
async def _143(ctx): await _65(ctx)
@bot.command(name="66")
async def _144(ctx): await _66(ctx)
@bot.command(name="67")
async def _145(ctx): await _67(ctx)
@bot.command(name="68")
async def _146(ctx): await _68(ctx)
@bot.command(name="69")
async def _147(ctx): await _69(ctx)
@bot.command(name="70")
async def _148(ctx): await _70(ctx)

if __name__ == "__main__":
    if BOT_TOKEN == "YOUR_BOT_TOKEN_HERE":
        print("")
        print("ERROR - YOU DIDNT PUT YOUR TOKEN")
        print("")
        print("1. Open core/g/_78.py")
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
        print("4. Copy the token and paste in core/g/_78.py")
        print("")
        exit(1)
