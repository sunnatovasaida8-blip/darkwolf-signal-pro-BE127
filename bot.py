import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, WebAppInfo

# Sizning Telegram bot tokeningiz
API_TOKEN = "9109506024:AAG8G_gAlzhODK57GdHGnPe8rsuRGfYEUB8"
bot = telebot.TeleBot(API_TOKEN)

# Vercel Web App manzilingiz
WEB_APP_URL = "https://darkwolfsignalprobe.vercel.app"

@bot.message_handler(commands=['start'])
def send_welcome(message):
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
        "🤖 *Xush kelibsiz!*\n\n"
        "Bu bot orqali siz *Apple of Fortune*, *Dragon's Gold* va *Gems & Mines* oʻyinlari uchun "
        "signal olishingiz, shuningdek rasmiy promokodlardan foydalanishingiz mumkin!\n\n"
        "Pastdagi tugmalar yordamida bo'limni tanlang 👇"
    )
    bot.send_message(message.chat.id, text, reply_markup=keyboard, parse_mode="Markdown")

@bot.callback_query_handler(func=lambda call: call.data == "promos")
def show_promos(call):
    promo_text = (
        "🎁 *Rasmiy Promokodlar va Chegirmalar:*\n\n"
        "🧊 *Coldbet Promokod:* `MUZZ`\n"
        "🐺 *Linebet Promokod 1:* `DARKWOLF76`\n"
        "🔥 *Linebet Promokod 2:* `BE127`\n\n"
        "Roʻyxatdan oʻtayotganda ushbu promokodlarni kiriting va bonuslarga ega boʻling!"
    )
    bot.edit_message_text(promo_text, call.message.chat.id, call.message.message_id, parse_mode="Markdown")

if __name__ == '__main__':
    print("Bot ishga tushdi...")
    bot.infinity_polling()
    
