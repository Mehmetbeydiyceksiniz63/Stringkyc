import asyncio

from pyrogram import Client, filters
from oldpyro import Client as Client1
from oldpyro.errors import ApiIdInvalid as ApiIdInvalid1
from oldpyro.errors import PasswordHashInvalid as PasswordHashInvalid1
from oldpyro.errors import PhoneCodeExpired as PhoneCodeExpired1
from oldpyro.errors import PhoneCodeInvalid as PhoneCodeInvalid1
from oldpyro.errors import PhoneNumberInvalid as PhoneNumberInvalid1
from oldpyro.errors import SessionPasswordNeeded as SessionPasswordNeeded1
from pyrogram.errors import (
    ApiIdInvalid,
    FloodWait,
    PasswordHashInvalid,
    PhoneCodeExpired,
    PhoneCodeInvalid,
    PhoneNumberInvalid,
    SessionPasswordNeeded,
)
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from telethon import TelegramClient
from telethon.errors import (
    ApiIdInvalidError,
    PasswordHashInvalidError,
    PhoneCodeExpiredError,
    PhoneCodeInvalidError,
    PhoneNumberInvalidError,
    SessionPasswordNeededError,
)
from telethon.sessions import StringSession
from telethon.tl.functions.channels import JoinChannelRequest
from pyromod.listen.listen import ListenerTimeout

from config import SUPPORT_CHAT
from StringGen import Alone
from StringGen.utils import retry_key


async def gen_session(
    message, user_id: int, telethon: bool = False, old_pyro: bool = False
):
    if telethon:
        ty = f"ᴛᴇʟᴇᴛʜᴏɴ"
    elif old_pyro:
        ty = f"ᴩʏʀᴏɢʀᴀᴍ v1"
    else:
        ty = f"ᴩʏʀᴏɢʀᴀᴍ v2"

    await message.reply_text(f"» {ty} oturum oluşturucu başlıyor, 1 sn☝🏻...")

    try:
        api_id = await Alone.ask(
            identifier=(message.chat.id, user_id, None),
            text="» Devam etmek için lütfen API-ID'nizi girin :",
            filters=filters.text,
            timeout=300,
        )
    except ListenerTimeout:
        return await Alone.send_message(
            user_id,
            "» 5 dakikalık zaman sınırına ulaşıldı.\n\nLütfen oturumu oluşturmaya tekrar başlayın.",
            reply_markup=retry_key,
        )

    if await cancelled(api_id):
        return

    try:
        api_id = int(api_id.text)
    except ValueError:
        return await Alone.send_message(
            user_id,
            "» Gönderdiğiniz API-ID geçersiz.\n\nLütfen oturum oluşturmaya tekrar başlayın.",
            reply_markup=retry_key,
        )

    try:
        api_hash = await Alone.ask(
            identifier=(message.chat.id, user_id, None),
            text="» Devam etmek için lütfen API-HASH'inizi girin  :",
            filters=filters.text,
            timeout=300,
        )
    except ListenerTimeout:
        return await Alone.send_message(
            user_id,
            "» 5 dakikalık zaman sınırına ulaşıldı.\n\nLütfen oturumu oluşturmaya tekrar başlayın.",
            reply_markup=retry_key,
        )

    if await cancelled(api_hash):
        return

    api_hash = api_hash.text

    if len(api_hash) < 30:
        return await Alone.send_message(
            user_id,
            "» Gönderdiğiniz API-HASH geçersiz.\n\nLütfen oturum oluşturmaya tekrar başlayın .",
            reply_markup=retry_key,
        )

    try:
        phone_number = await Alone.ask(
            identifier=(message.chat.id, user_id, None),
            text="» Devam etmek için lütfen telefon numaranızı girin :",
            filters=filters.text,
            timeout=300,
        )
    except ListenerTimeout:
        return await Alone.send_message(
            user_id,
            "» 5 dakikalık zaman sınırına ulaşıldı.\n\nLütfen oturumu oluşturmaya tekrar başlayın.",
            reply_markup=retry_key,
        )

    if await cancelled(phone_number):
        return
    phone_number = phone_number.text

    await Alone.send_message(user_id, "» Verilen numaraya giriş kodu gönderiliyor...")
    if telethon:
        client = TelegramClient(StringSession(), api_id, api_hash)
    elif old_pyro:
        client = Client1(":memory:", api_id=api_id, api_hash=api_hash)
    else:
        client = Client(name="Alone", api_id=api_id, api_hash=api_hash, in_memory=True)
    await client.connect()

    try:
        if telethon:
            code = await client.send_code_request(phone_number)
        else:
            code = await client.send_code(phone_number)
        await asyncio.sleep(1)

    except FloodWait as f:
        return await Alone.send_message(
            user_id,
            f"» Giriş kodu gönderilemedi.\n\nLütfen {f.value or f.x} saniye bekleyip tekrar deneyin..",
            reply_markup=retry_key,
        )
    except (ApiIdInvalid, ApiIdInvalidError, ApiIdInvalid1):
        return await Alone.send_message(
            user_id,
            "» API-ID veya API-HASH geçersiz.\n\nLütfen oturumunuzu yeniden oluşturmaya başlayın.",
            reply_markup=retry_key,
        )
    except (PhoneNumberInvalid, PhoneNumberInvalidError, PhoneNumberInvalid1):
        return await Alone.send_message(
            user_id,
            "» Telefon numarası geçersiz.\n\nLütfen oturumu yeniden oluşturmaya başlayın.",
            reply_markup=retry_key,
        )

    try:
        otp = await Alone.ask(
            identifier=(message.chat.id, user_id, None),
            text=f"Lütfen {phone_number} numarasına gönderilen giriş kodunu girin.\n\nEğer kod <code>12345</code> ise, Lütfen <code>1 2 3 4 5</code> şeklinde birer boşluk ile gönderin.",
            filters=filters.text,
            timeout=600,
        )
        if await cancelled(otp):
            return
    except ListenerTimeout:
        return await Alone.send_message(
            user_id,
            "»10 dakikalık zaman sınırına ulaşıldı.\n\nLütfen oturumu oluşturmaya tekrar başlayın.",
            reply_markup=retry_key,
        )

    otp = otp.text.replace(" ", "")
    try:
        if telethon:
            await client.sign_in(phone_number, otp, password=None)
        else:
            await client.sign_in(phone_number, code.phone_code_hash, otp)
    except (PhoneCodeInvalid, PhoneCodeInvalidError, PhoneCodeInvalid1):
        return await Alone.send_message(
            user_id,
            "» Gönderdiğiniz giriş kodu <b>Yanlış</b>.\n\nLütfen oturumunuzu yeniden oluşturmaya başlayın.",
            reply_markup=retry_key,
        )
    except (PhoneCodeExpired, PhoneCodeExpiredError, PhoneCodeExpired1):
        return await Alone.send_message(
            user_id,
            "» Gönderdiğiniz giriş kodu'nun <b>Süresi doldu.</b>Lütfen oturumunuzu yeniden oluşturmaya başlayın.",
            reply_markup=retry_key,
        )
    except (SessionPasswordNeeded, SessionPasswordNeededError, SessionPasswordNeeded1):
        try:
            pwd = await Alone.ask(
                identifier=(message.chat.id, user_id, None),
                text="» Devam etmek için lütfen iki adımlı doğrulama şifrenizi girin :",
                filters=filters.text,
                timeout=300,
            )
        except ListenerTimeout:
            return Alone.send_message(
                user_id,
                "» 5 dakikalık zaman sınırına ulaşıldı.\n\nLütfen oturumu oluşturmaya tekrar başlayın.",
                reply_markup=retry_key,
            )

        if await cancelled(pwd):
            return
        pwd = pwd.text

        try:
            if telethon:
                await client.sign_in(password=pwd)
            else:
                await client.check_password(password=pwd)
        except (PasswordHashInvalid, PasswordHashInvalidError, PasswordHashInvalid1):
            return await Alone.send_message(
                user_id,
                "» Gönderdiğiniz şifre yanlış.\n\nLütfen oturumunuzu yeniden oluşturmaya başlayın.",
                reply_markup=retry_key,
            )

    except Exception as ex:
        return await Alone.send_message(user_id, f"HATA : <code>{str(ex)}</code>")

    try:
        txt = "İşte {0} dize oturumunuz\n\n<code>{1}</code>\n\n<a href={2}>Yalnız ilişkilendirme</a> tarafından sağlanan bir dize oluşturma botu\n<b>Not :</b>Kimseyle paylaşmayın."
        if telethon:
            string_session = client.session.save()
            await client.send_message(
                "me",
                txt.format(ty, string_session, SUPPORT_CHAT),
                link_preview=False,
                parse_mode="html",
            )
            await client(JoinChannelRequest("@S1F1RB1RSOHBETT"))
        else:
            string_session = await client.export_session_string()
            await client.send_message(
                "me",
                txt.format(ty, string_session, SUPPORT_CHAT),
                disable_web_page_preview=True,
            )
            await client.join_chat("S1F1RB1RSOHBET")
    except KeyError:
        pass
    try:
        await client.disconnect()
        await Alone.send_message(
            chat_id=user_id,
            text=f"{ty} dize oturumunuz başarıyla oluşturuldu.\n\nBunu almak için lütfen kayıtlı mesajlarınızı kontrol edin.\n\nKıyıcı Boss`un hazırladığı dize oluşturma botunu güvenle kullanabilirsiniz.",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="Kayıtlı Mesajlarda.",
                            url=f"tg://openmessage?user_id={user_id}",
                        )
                    ]
                ]
            ),
            disable_web_page_preview=True,
        )
    except:
        pass


async def cancelled(message):
    if "/cancel" in message.text:
        await message.reply_text(
            "» Devam eden dize oluşturma süreci iptal edildi.", reply_markup=retry_key
        )
        return True
    elif "/restart" in message.text:
        await message.reply_text(
            "» Bu bot başarıyla yeniden başlatıldı.", reply_markup=retry_key
        )
        return True
    elif message.text.startswith("/"):
        await message.reply_text(
            "» Devam eden dize oluşturma süreci iptal edildi.", reply_markup=retry_key
        )
        return True
    else:
        return False
