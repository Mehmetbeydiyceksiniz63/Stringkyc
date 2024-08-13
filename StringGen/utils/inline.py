from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from config import SUPPORT_CHAT


keyboard = InlineKeyboardMarkup(
    [
        [InlineKeyboardButton(text="💫𝙊𝙩𝙪𝙧𝙪𝙢 𝙤𝙡𝙪ş𝙩𝙪𝙧💫", callback_data="gensession")],
        [
            InlineKeyboardButton(text="💫𝘿𝙚𝙨𝙩𝙚𝙠💫", url=SUPPORT_CHAT),
            InlineKeyboardButton(
                text="💫𝙨𝙖𝙝𝙞𝙗𝙞💫", url="https://t.me/expfedai"
            ),
        ],
    ]
)

gen_key = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text=" 💫𝙥𝙮𝙧𝙤𝙜𝙧𝙖𝙢 𝙫1💫", callback_data="pyrogram1"),
            InlineKeyboardButton(text="💫𝙥𝙮𝙧𝙤𝙜𝙧𝙖𝙢 𝙫2💫", callback_data="pyrogram"),
        ],
        [InlineKeyboardButton(text=" 💫𝙏𝙚𝙡𝙚𝙩𝙝𝙤𝙣💫", callback_data="telethon")],
    ]
)

retry_key = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="💫𝙩𝙚𝙠𝙧𝙖𝙧 𝙙𝙚𝙣𝙚💫", callback_data="gensession")]]
)
