from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from ZelzalMusic import app

@app.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(bot: Client, msg: Message):
    if not "https://t.me/ye20_r":  # Not compulsory
        return
    try:
        try:
            await bot.get_chat_member("ye20_r", msg.from_user.id)
        except UserNotParticipant:
            if "https://t.me/ye20_r".isalpha():
                link = "https://t.me/ye20_r"
            else:
                chat_info = await bot.get_chat("ye20_r")
                link = chat_info.invite_link
            try:
                await msg.reply(
                    f"⌯︙عذࢪاَ حَبيبي ↫ {msg.from_user.mention} \n⌯︙عـليك الاشـتࢪاك في قنـاة Not Res .\n⌯︙قناة : t.me/ye20_r 🍓.\nꔹ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ ┉ꔹ",
                    disable_web_page_preview=True,
                    reply_markup=InlineKeyboardMarkup([
                        [InlineKeyboardButton("Not Res", url=link)]
                    ])
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"I'm not admin in the MUST_JOIN chat @ye20_r !")