from telebot.types import ReplyKeyboardMarkup, KeyboardButton

def person_button():
    markup = ReplyKeyboardMarkup()
    btn1 = KeyboardButton("Mike Tayson")
    btn2 = KeyboardButton("Magnus Karlson")
    btn3 = KeyboardButton("Alexsandr Karelin")
    markup.add(btn1,btn2,btn3)
    return markup

