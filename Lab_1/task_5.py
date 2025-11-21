import telebot

BOT_TOKEN = '8595531618:AAGWu12v8ogL2oC9VhwGOSZb96w9mkGLO2M'

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start', 'menu'])
def send_menu(message):
    markup = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = telebot.types.KeyboardButton('/scream Hello')
    btn2 = telebot.types.KeyboardButton('/whisper Secret')
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, "Choose a command:", reply_markup=markup)

@bot.message_handler(commands=['scream'])
def scream_command(message):
    text = message.text.replace('/scream', '').strip()
    if text:
        bot.reply_to(message, text.upper() + "!!!")
    else:
        bot.reply_to(message, "Format: /scream text")

@bot.message_handler(commands=['whisper'])
def whisper_command(message):
    text = message.text.replace('/whisper', '').strip()
    if text:
        bot.send_message(message.chat.id, f"||{text}||", parse_mode='MarkdownV2')
    else:
        bot.reply_to(message, "Format: /whisper text")

bot.infinity_polling()