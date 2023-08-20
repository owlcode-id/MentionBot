import os, logging, asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.tl.types import ChannelParticipantAdmin
from telethon.tl.types import ChannelParticipantCreator
from telethon.tl.types import ChannelParticipantsAdmins
from telethon.tl.functions.channels import GetParticipantRequest
from telethon.errors import UserNotParticipantError
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

logging.basicConfig(
    level=logging.INFO, format="%(name)s - [%(levelname)s] - %(message)s"
)
LOGGER = logging.getLogger(__name__)

api_id = int(os.environ.get("APP_ID", ""))
api_hash = os.environ.get("API_HASH", "")
bot_token = os.environ.get("TOKEN", "")
client = TelegramClient("client", api_id, api_hash).start(bot_token=bot_token)
spam_chats = []

@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
    chat_id = event.chat_id
    if not event.is_private:
        return await event.respond("ɪ ᴀᴍ ᴀʟɪᴠᴇ 🥺")
    await event.reply(
        "━━━━━━━━━━━━━━━━━━━━━━━━\n\n✪ Saya adalah Neko, untuk menyebutkan semua anggota grup di Telegram\n✪ Terima kasih telah menggunakan, jalankan /help..\n\n┏━━━━━━━━━━━━━━━━━┓\n┣★ Pemilik    : [Neko](https://t.me/OwnNeko)\n┣★ Perbarui › : [NekoLocal](https://t.me/NekoLocal)┓\n┣★  Grup [NekoMenfess](https://t.meNekoMemfess)\n┗━━━━━━━━━━━━━━━━━┛\n\n💞 Jika Anda memiliki pertanyaan,\nkirim pesan ke [pemilik saya](https://t.me/OwnNeko) ...\n\n━━━━━━━━━━━━━━━━━━━━━━━━",
        link_preview=False,
        buttons=(
            [
                Button.url(
                    "📍Tambahkan Ke Grup",
                    "https://t.me/NekoFilterBot?startgroup=true",
                ),
            ],
            [
                Button.url("📌 Grup", "https://t.me/NekoMenfessChat"),
                Button.url("📌 Channel", "https://t.me/NekoMenfess"),
            ],
            [
                Button.url("📌 NekoStore", "https://t.me/NekoLocal"),
                Button.url("😼 Pemilik", "https://t.me/OwnNeko"),
            ],
        ),
    )



@client.on(events.NewMessage(pattern="^/help$"))
async def help(event):
    chat_id = event.chat_id
    if not event.is_private:
        return await event.respond("ᴅɪᴋᴇᴛɪᴋ ᴍᴜʟᴀɪ ᴅᴀʀɪ ᴘᴇʀᴛᴀɴʏᴀᴀɴ ᴅɪ ᴘʀɪᴠᴀᴛᴇ ᴜɴᴛᴜᴋ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ᴄᴏᴍᴍᴀɴᴅ ɪɴɪ 🥺")
    helptext = "✪ ᴍᴇɴᴜ ʙᴀntᴜᴀɴ ᴛᴇɴᴛᴀɴɢ ᴄᴏᴍᴍᴀɴᴅ\n\n✪ ᴄᴏᴍᴍᴀɴᴅ: /mentionall\n✪ ᴄᴏᴍᴍᴀɴᴅ: /cancel ᴜɴᴛᴜ ᴍᴇɴɢʜᴇᴛɪᴋᴀɴ ᴘʀᴏsᴇs.\n✪ ᴄᴏᴍᴍᴀɴᴅ /admin ᴜɴᴛᴜᴋ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ᴍᴇɴᴛɪᴏɴ ᴀᴅᴍɪɴ ɢʀᴜᴘ ᴀɴᴅᴀ\n✪ ᴀɴᴅᴀ ʙɪsᴀ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ᴄᴏᴍᴍᴀɴᴅ ɪɴɪ ᴅᴇɴɢᴀɴ ᴛᴇᴋs ᴡʜᴀᴛsᴀᴘᴘ ʏᴀɴɢ ᴀɴᴅᴀ ɪɴɢɪɴᴋᴀɴ ᴜɴᴛᴜᴋ ᴍᴇɴᴛɪᴏɴ ᴏʀᴀɴ ʟᴀɪɴ.\n✪ `Contoh: /mentionall Selamat Pagi!`\n✪ ᴀɴᴅᴀ ʙɪsᴀ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ᴄᴏᴍᴍᴀɴᴅ ɪɴɪ sᴇʙᴀɢᴀɪ ʙᴀʟᴀsᴀɴ ᴋᴇᴘᴀᴅᴀ ᴍᴇssᴀɢᴇ ᴍᴀɴᴀᴘᴜɴ. ʙᴏᴛ ᴀᴋᴀɴ ᴍᴇɴᴛᴀɢɪ ᴘᴇɴɢɢᴜɴᴀ ʏᴀɴɢ ᴅɪʙᴀʟᴀsɪ ᴅᴀʀɪ ᴍᴇssᴀɢᴇ ᴛᴇʀsᴇʙᴜᴛ."
    await event.reply(
        helptext,
        link_preview=False,
        buttons=(
            [
                Button.url("NekoLocal", "https://t.me/NekoLocal"),
                Button.url("📌 Neko Website", "https://neko.ueuo.com"),
            ]
        ),
    )

@client.on(events.NewMessage(pattern="^/owner$"))
async def help(event):
    chat_id = event.chat_id
    if not event.is_private:
        return await event.respond("ᴅɪᴋᴇᴛɪᴋ ᴍᴜʟᴀɪ ᴅᴀʀɪ ᴘᴇʀᴛᴀɴʏᴀᴀɴ ᴅɪ ᴘʀɪᴠᴀᴛᴇ ᴜɴᴛᴜᴋ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ᴄᴏᴍᴍᴀɴᴅ ɪɴɪ 🥺")
    helptext = "✪ ᴍᴇɴᴜ ʙᴀᴛᴀs ᴅᴀʀɪ ᴀʟᴇxᴀ ᴍᴇɴᴛɪᴏɴ\n\n✪ ᴘᴇᴍɪʟɪᴋ sᴀʏᴀ [Neko](https://t.me/OwnNeko)\n✪ ᴀɴɢɢᴏᴛᴀ ʀᴇsᴍɪ [ʀᴏᴄᴋs](https://t.me/NekoMenfess)\n✪ ʏᴏᴜᴛᴜʙᴇ [ᴄʜᴀɴɴᴇʟ](https://t.me/NekoMenfess)\n✪ ᴀɴᴇsᴛʜᴇᴛɪᴄ ᴍᴀsᴀ ᴅᴇᴘᴀɴ ᴍᴀᴛᴀ."
    await event.reply(
        helptext,
        link_preview=False,
        buttons=(
            [
                Button.url("📌 NekoLocal", "https://t.me/NekoLocal"),
                Button.url("Website", "https:/neko.ueuo.com"),
            ]
        ),
    )

@client.on(events.NewMessage(pattern="^/mentionall ?(.*)"))
async def mentionall(event):
    chat_id = event.chat_id
    if event.is_private:
        return await event.respond(
            "ᴄᴏᴍᴍᴀɴᴅ ɪɴɪ ʙɪsᴀ ᴅɪɢᴜɴᴀᴋᴀɴ ʜᴀɴʏᴀ ᴅɪ ɢʀᴜᴘ ᴅᴀɴ ᴄʜᴀɴɴᴇʟ"
        )

    is_admin = False
    try:
        partici_ = await client(GetParticipantRequest(event.chat_id, event.sender_id))
    except UserNotParticipantError:
        is_admin = False
    else:
        if isinstance(
            partici_.participant, (ChannelParticipantAdmin, ChannelParticipantCreator)
        ):
            is_admin = True
    if not is_admin:
        return await event.respond("ʜᴀɴʏᴀ ᴀᴅᴍɪɴs ʏᴀɴɢ ʙɪsᴀ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ᴄᴏᴍᴍᴀɴᴅ ɪɴɪ ᴜɴᴛᴜᴋ ᴍᴇɴᴛɪᴏɴ sᴇᴍᴜᴀ")

    if event.pattern_match.group(1) and event.is_reply:
        return await event.respond("ʙᴇʀɪᴋᴀɴʟᴀʜ ᴅᴀɴᴀ ʀɢᴜᴍᴇɴᴛ")
    elif event.pattern_match.group(1):
        mode = "text_on_cmd"
        msg = event.pattern_match.group(1)
    elif event.is_reply:
        mode = "text_on_reply"
        msg = await event.get_reply_message()
        if msg == None:
            return await event.respond(
                "ᴀᴋᴜ ᴛɪᴅᴀᴋ ᴅᴀᴘᴀᴛ ᴍᴇɴɢᴇᴍᴇɴᴛɪᴏɴ ᴍᴇᴍʙᴇʀs ʙᴇʀᴅᴀsᴀʀᴋᴀɴ ᴘᴇsᴀɴ ʏᴀɴɢ ᴅɪᴋɪʀɪᴍ ᴘᴀᴅᴀ ᴍᴀsᴀʟᴀʜ ᴘᴇsᴀɴ ʏᴀɴɢ ᴅɪᴋɪʀɪᴍ ʙᴇꜰᴏʀᴇ ʙᴏᴛ ᴅɪᴛᴀᴍʙᴀʜᴋᴀɴ ᴋᴇ ɢʀᴜᴘ"
            )
    else:
        return await event.respond(
            "ʙᴀʟᴀsɪ ᴋᴇᴘᴀᴅᴀ ᴍᴇssᴀɢᴇ ᴀᴛᴀᴜ ʙᴇʀɪᴋᴀɴʟᴀʜ ᴘᴀᴅᴀ ᴋᴜɴᴛᴜʟᴀɴ ᴜɴᴛᴜᴋ ᴍᴇɴɢɢᴜɴᴀᴋᴀɴ ᴄᴏᴍᴍᴀɴᴅ ɪɴɪ ᴜɴᴛᴜᴋ ᴍᴇɴᴛɪᴏɴ ᴏʀᴀɴ ʟᴀɪɴ"
        )


spam_chats.append(chat_id)
usrnum = 0
usrtxt = ""
async for usr in client.iter_participants(chat_id):
    if not chat_id in spam_chats:
        break
    usrnum += 1
    usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}) "
    if usrnum == 5:
        if mode == "text_on_cmd":
            txt = f"{usrtxt}\n\n{msg}"
            await client.send_message(chat_id, txt)
        elif mode == "text_on_reply":
            await msg.reply(usrtxt)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
try:
    spam_chats.remove(chat_id)
except:
    pass

@client.on(events.NewMessage(pattern="^/admins|/admin|@admin|@admins ?(.*)"))
async def _(event):
    chat_id = event.chat_id
    if event.is_private:
        return await event.respond("ᴍᴀᴀғ, ʜᴀɴʏᴀ ᴀᴅᴍɪɴ ʏᴀɴɢ ʙɪsᴀ ᴍᴇɴɢᴍᴇɴᴛɪᴏɴ ʙᴇʀᴜʙᴀʜᴀɴ ᴅɪ ɢʀᴜᴘ")

    is_admin = False
    try:
        partici_ = await client(GetParticipantRequest(event.chat_id, event.sender_id))
    except UserNotParticipantError:
        is_admin = False
    else:
        if isinstance(
            partici_.participant, (ChannelParticipantAdmin, ChannelParticipantCreator)
        ):
            is_admin = True
    if not is_admin:
        return await event.respond("ʜᴀɴʏᴀ ᴀᴅᴍɪɴ ɢʀᴜᴘ ʙɪsᴀ ᴍᴇɴɢᴍᴇɴᴛɪᴏɴ ᴀᴅᴍɪɴ ɢʀᴜᴘ")

    if event.pattern_match.group(1) and event.is_reply:
        return await event.respond("ʙᴇʀɪᴋᴀɴʟᴀʜ ᴛᴇᴋs ᴜɴᴛᴜᴋ ᴍᴇɴɢᴍᴇɴᴛɪᴏɴ")
    elif event.pattern_match.group(1):
        mode = "text_on_cmd"
        msg = event.pattern_match.group(1)
    elif event.is_reply:
        mode = "text_on_reply"
        msg = await event.get_reply_message()
        if msg == None:
            return await event.respond(
                "ᴀᴋᴜ ᴛɪᴅᴀᴋ ᴅᴀᴘᴀᴛ ᴍᴇɴɢᴍᴇɴᴛɪᴏɴ ᴍᴇᴍʙᴇʀs ʙᴇʀᴅᴀsᴀʀᴋᴀɴ ᴘᴇsᴀɴ ʏᴀɴɢ ᴅɪᴋɪʀɪᴍ ᴘᴀᴅᴀ ᴍᴀsᴀʟᴀʜ ᴘᴇsᴀɴ ʏᴀɴɢ ᴅɪᴋɪʀɪᴍ ʙᴇꜰᴏʀᴇ ʙᴏᴛ ᴅɪᴛᴀᴍʙᴀʜᴋᴀɴ ᴋᴇ ɢʀᴜᴘ)"
            )
    else:
        return await event.respond(
            "ʙᴀʟᴀsɪ ᴋᴇᴘᴀᴅᴀ ᴍᴇssᴀɢᴇ ᴀᴛᴀᴜ ʙᴇʀɪᴋᴀɴʟᴀʜ ᴘᴀᴅᴀ ᴛᴇᴋs ᴜɴᴛᴜᴋ ᴍᴇɴɢᴍᴇɴᴛɪᴏɴ ʟᴀɪɴ!"

    spam_chats.append(chat_id)
    usrnum = 0
    usrtxt = ""
    chat = await event.get_input_chat()
    async for x in client.iter_participants(chat, filter=ChannelParticipantsAdmins):
        if not chat_id in spam_chats:
            break
        usrnum += 1
        usrtxt += f" \n [{x.first_name}](tg://user?id={x.id})"
        if usrnum == 5:
            if mode == "text_on_cmd":
                txt = f"{usrtxt}\n\n{msg}"
                await client.send_message(chat_id, txt)
            elif mode == "text_on_reply":
                await msg.reply(usrtxt)
            await asyncio.sleep(2)
            usrnum = 0
            usrtxt = ""
try:
    spam_chats.remove(chat_id)
except:
    pass

@client.on(events.NewMessage(pattern="^/cancel$"))
async def cancel_spam(event):
    if not event.chat_id in spam_chats:
        return await event.respond("ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴘʀᴏsᴇs ʏᴀɴɢ ʙᴇʀᴊᴀʟᴀɴ...")
    else:
        try:
            spam_chats.remove(event.chat_id)
        except:
            pass
        return await event.respond("ᴅɪʜᴇɴᴛɪᴋᴀɴ.")


print(">> ASAD ALEXA WORKING <<")
client.run_until_disconnected()

