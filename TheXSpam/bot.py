# 𝑪𝒐𝒑𝒚𝒓𝒊𝒈𝒉𝒕 𝑩𝒚 𝑨𝒍𝒕𝒓𝒐𝒏
# 𝑨𝒍𝒍 𝑹𝒊𝒈𝒉𝒕𝒔 𝑹𝒆𝒔𝒆𝒓𝒗𝒆𝒅

import sys
import datetime

from os import execle, environ
from config import ALIVE_PIC, SUDO_USERS

from pyrogram import Client, filters
from pyrogram.types import Message


ALT = f"""❖ 𝗦𝗧𝗥𝗔𝗡𝗚𝗘𝗥 𝐒𝐏𝐀𝐌 ❖

➠ **𝗣ʏᴛʜᴏɴ 𝗩ᴇʀsɪᴏɴ** : `3.11.1`
➠ **𝗣ʏʀᴏɢʀᴀᴍ 𝗩ᴇʀsɪᴏɴ** : `1.4.16`
➠ **𝗦ᴛʀᴀɴɢᴇʀ𝗦ᴘᴀᴍ 𝗩ᴇʀsɪᴏɴ**  : `3.3`
➠ **𝗨ᴘᴅᴀᴛᴇs** : @mastiwithfriendsx\n"""


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["ping"], ["/", ".", "!"]))
async def ping(_, e: Message):       
      start = datetime.datetime.now()
      Fuk = await e.reply("**Pong !!**")
      end = datetime.datetime.now()
      ms = (end-start).microseconds / 1000
      await Fuk.edit_text(f"⁂ STRANGER 𝚂𝙿𝙰𝙼\n⁂ ᴘɪɴɢ: `{ms}ms`\n➠ 𝗩ᴇʀsɪᴏɴ: `3.3`")


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["alive"], ["/", ".", "!"]))
async def alive(xspam: Client, msg: Message):
       if ".jpg" in ALIVE_PIC or ".png" in ALIVE_PIC:
              await xspam.send_photo(msg.chat.id, ALIVE_PIC, caption=ALT)
       if ".mp4" in ALIVE_PIC or ".MP4," in ALIVE_PIC:
              await xspam.send_video(msg.chat.id, ALIVE_PIC, caption=ALT)


@Client.on_message(filters.user(SUDO_USERS) & filters.command(["reboot", "restart"], ["/", ".", "!"]))
async def restart_bot(_, message: Message):
    msg = await message.reply("`ʀᴇsᴛᴀʀᴛɪɴɢ ʙᴏᴛ...`")
    args = [sys.executable, "main.py"]
    await msg.edit("» ʙᴏᴛ ʀᴇsᴛᴀʀᴛᴇᴅ...\n» ɴᴏᴡ ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ᴛʜɪs ʙᴏᴛ ")
    execle(sys.executable, *args, environ)
