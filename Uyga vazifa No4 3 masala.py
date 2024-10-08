from telebot import TeleBot
from telebot.types import Message
from button import person_button

bot = TeleBot("7653940499:AAHCF7eH4cwYJpat5aTByslbl9lIxios0Uo")
mike_tayson_info = "Mike Tayson - Boks, Nikname: Iron Mike. Ma'lumot: Boks olamidagi eng mashhur sportchilardan biri."
magnus_karlson_info = "Magnus Karlson - Shahmat, Nikname: The Mozart of chess. Ma'lumot: Shahmat bo'yicha jahondagi eng kuchli o'yinchilardan biri."
alexsandr_karelin_info = "Alexsandr Karelin - Kurash, Nikname: Russian King Kong. Ma'lumot: Og'ir vazn toifasida ko'plab yutug'lari bor."

@bot.message_handler(commands=['start'])
def reaction_to_start(message: Message):
    chat_id = message.chat.id
    bot.send_message(chat_id, f"Assalomu alaykum {message.from_user.full_name}, kim haqida bilmoqchisiz",reply_markup=person_button())

@bot.message_handler(regexp="Mike Tayson")
def reaction_to_tayson(messege: Message):
    chat_id = messege.chat.id
    bot.send_message(chat_id,mike_tayson_info)

@bot.message_handler(regexp="Magnus Karlson")
def reaction_to_tayson(messege: Message):
    chat_id = messege.chat.id
    bot.send_message(chat_id,magnus_karlson_info)

@bot.message_handler(regexp="Alexsandr Karelin")
def reaction_to_tayson(messege: Message):
    chat_id = messege.chat.id
    bot.send_message(chat_id,alexsandr_karelin_info)

bot.polling()
