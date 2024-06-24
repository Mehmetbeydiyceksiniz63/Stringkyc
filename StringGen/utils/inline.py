from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import SUPPORT_CHAT


keyboard = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton(text="OTURUM OLUŞTUR", callback_data="gensession")],
        [
            InlineKeyboardButton(text="𝐒ᴜᴘᴘᴏʀᴛ", url=SUPPORT_CHAT),
            InlineKeyboardButton(
                text="OWNER", url="https://t.me/Officialkiyici"
            ),
        ],
    ]
)

gen_key = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="ᴩʏʀᴏɢʀᴀᴍ v1", callback_data="pyrogram1"),
            InlineKeyboardButton(text="ᴩʏʀᴏɢʀᴀᴍ v2", callback_data="pyrogram"),
        ],
        [InlineKeyboardButton(text="ᴛᴇʟᴇᴛʜᴏɴ", callback_data="telethon")],
    ]
)

retry_key = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="YENİDEN DENE", callback_data="gensession")]]
)
