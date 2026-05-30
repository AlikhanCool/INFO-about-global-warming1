import telebot
from telebot import types
import random
from settings import TG_API_TOKEN


bot = telebot.TeleBot(TG_API_TOKEN)

INFO_LIST = [
    "С начала двадцатого века средняя температура воздуха на планете выросла более чем на один градус.",
    "Главной причиной современного изменения климата признан человеческий фактор, в частности выбросы углекислого газа.",
    "Таяние ледников приводит к постепенному повышению уровня Мирового океана, что угрожает прибрежным городам.",
    "Около девяноста процентов избыточного тепла, задерживаемого парниковыми газами, поглощается океанами.",
    "Глобальное потепление приводит к увеличению частоты экстремальных погодных явлений, таких как засухи и наводнения.",
    "Концентрация углекислого газа в атмосфере Земли сейчас является самой высокой за последние несколько миллионов лет."
]

def get_info_keyboard():
    keyboard = types.InlineKeyboardMarkup()
    btn = types.InlineKeyboardButton(text="Получить новую информацию", callback_data="get_new_info")
    keyboard.add(btn)
    return keyboard

@bot.message_handler(commands=['start', 'info'])
def send_welcome(message):
    first_info = random.choice(INFO_LIST)
    bot.send_message(
        chat_id=message.chat.id,
        text=f"Приветствуем. Вот информация о глобальном потеплении:\n\n{first_info}",
        reply_markup=get_info_keyboard()
    )

@bot.callback_query_handler(func=lambda call: call.data == "get_new_info")
def callback_inline(call):
    new_info = random.choice(INFO_LIST)
    current_text = call.message.text.split("\n\n")[-1]
    
    while new_info == current_text:
        new_info = random.choice(INFO_LIST)
        
    try:
        bot.edit_message_text(
            chat_id=call.message.chat.id,
            message_id=call.message.id,
            text=f"Приветствуем. Вот информация о глобальном потеплении:\n\n{new_info}",
            reply_markup=get_info_keyboard()
        )
    except Exception:
        pass

    bot.answer_callback_query(call.id)


    bot.infinity_polling()
