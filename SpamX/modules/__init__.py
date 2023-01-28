from SpamX.config import *
from SpamX.core.version import __version__
from SpamX import sudoser, RiZoeL 
from RiZoeLX import __version__ as pip_vr
from pyrogram import __version__ as pyro_vr
import platform

__version__ = __version__


ping_msg = PING_MSG if PING_MSG else "SpamX"
pic = ALIVE_PIC if ALIVE_PIC else "https://te.legra.ph/file/74d210f7ebc9e05437fbc.jpg"
amsg = ALIVE_MSG if ALIVE_MSG else "ꜱᴜᴍɪᴛ x ꜱᴘᴀᴍ"

try:
   sah = RiZoeL.get_users(OWNER_ID)
   owner_mention = sah.mention
except:
   owner_mention = f"[{OWNER_ID}](tg://user?id={OWNER_ID})"

class Alive:
     Pic = pic
     
     msg = f"""
**⁂ {amsg} ⁂**

━───────╯•╰───────━
➠ **ᴹᵃˢᵗᵉʳ:** {owner_mention}
➠ **ᴘʏᴛʜᴏɴ x ꜱᴘᴀᴍ:** `{platform.python_version()}`
➠ **ꜱᴜᴍɪᴛ x ꜱᴘᴀᴍ Version:** `{__version__}`
➠ **ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ:** `{pyro_vr}`
➠ **ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀsɪᴏɴ :** `{pip_vr}`
➠ **Channel:** @ab_sumit
━───────╮•╭───────━
➠ **Source Code:** [•Repo•](https://t.me/ab_sumit)
     """

handler = HNDLR
Owner = int(OWNER_ID)
DATABASE_URL = DATABASE_URL
LOGS_CHANNEL = LOGS_CHANNEL

if DATABASE_URL:
   from SpamX.database import users_db
   Sudos = []
   Sudos.append(Owner)
   all = users_db.get_all_sudos()
   for user_id in all:
       Sudos.append(user_id)

else:
  Sudos = sudoser
  Sudos.append(Owner)
