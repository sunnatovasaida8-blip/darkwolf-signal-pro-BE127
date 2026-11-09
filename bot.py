import logging
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

# Sizning Telegram bot tokeningiz
API_TOKEN = "9109506024:AAG8G_gAlzhODK57GdHGnPe8rsuRGfYEUB8"

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

# Vercel Web App manzilingiz
WEB_APP_URL = "https://darkwolfsignalprobe.vercel.app"

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    # Asosiy menyu tugmalari
    keyboard = InlineKeyboardMarkup(row_width=1)
    
    # Web App ochish tugmasi
    keyboard.add(
        InlineKeyboardButton("🎮 Signal Menyu va O'yinlar", web_app=WebAppInfo(url=WEB_APP_URL))
    )
    
    # Promokodlar va kanallar
    keyboard.add(
        InlineKeyboardButton("🎟 Promokodlarni ko'rish", callback_data="promos"),
        InlineKeyboardButton("📥 Linebet Yuklab olish", url="https://lb-aff.com/L?tag=d_6057106m_66803c_apk1&site=6057106&ad=66803"),
        InlineKeyboardButton("📥 Coldbet Yuklab olish", url="https://coldb10.com/Fhyhq8yL"),
        InlineKeyboardButton("📢 LINEBET STAFKALARR", url="https://t.me/LINEBET_STAFKALARR"),
        InlineKeyboardButton("📢 MUZZCOLD", url="https://t.me/MUZZCOLD")
    )
    
    text = (
        "🤖 **Xush kelibsiz!**\n\n"
        "Bu bot orqali siz **Apple of Fortune**, **Dragon's Gold** va **Gems & Mines** oʻyinlari uchun "
        "signal olishingiz, shuningdek rasmiy promokodlardan foydalanishingiz mumkin!\n\n"
        "Pastdagi tugmalar yordamida bo'limni tanlang 👇"
    )
    await message.answer(text, reply_markup=keyboard, parse_mode="Markdown")

@dp.callback_query_handler(text="promos")
async def show_promos(call: types.CallbackQuery):
    promo_text = (
        "🎁 **Rasmiy Promokodlar va Chegirmalar:**\n\n"
        "🧊 **Coldbet Promokod:** `MUZZ`\n"
        "🐺 **Linebet Promokod 1:** `DARKWOLF76`\n"
        "🔥 **Linebet Promokod 2:** `BE127`\n\n"
        "Roʻyxatdan oʻtayotganda ushbu promokodlarni kiriting va bonuslarga ega boʻling!"
    )
    await call.message.edit_text(promo_text, parse_mode="Markdown")
    
if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
    
