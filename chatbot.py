import telebot
from telebot import types
import logging
import os

class ChatBot:
    def __init__(self, nombre):
        self.nombre = nombre
        bot_token = os.getenv("BOT_TOKEN")
        if not bot_token:
            logging.error("BOT_TOKEN no encontrado en las variables de entorno.")
            raise ValueError("BOT_TOKEN no configurado")
            
        self.bot = telebot.TeleBot(bot_token)
        logging.info(f"Chat Bot {self.nombre} iniciado")
        self.registrar_manejadores()

    def registrar_manejadores(self):
        """Registra todos los manejadores de mensajes y callbacks."""
        self.bot.message_handler(commands=['start'])(self.send_welcome)
        self.bot.message_handler(commands=['help'])(self.send_help)
        self.bot.message_handler(commands=['pizzas'])(self.send_options)
        self.bot.callback_query_handler(func=lambda call: True)(self.callback_query)
        self.bot.message_handler(commands=['foto'])(self.send_image)

    def send_welcome(self, message):
        self.bot.reply_to(message, 'Hola! soy tu primer bot creado')

    def send_help(self, message):
        self.bot.reply_to(message, 'Puedes interactuar conmigo usuando comandoS. Por ahora, solo respondo a /start y /help')

    def send_options(self, message):
        markup = types.InlineKeyboardMarkup(row_width=2)
        btn_si = types.InlineKeyboardButton('Sí', callback_data='pizza_si')
        btn_no = types.InlineKeyboardButton('No', callback_data='pizza_no')
        markup.add(btn_si, btn_no)
        self.bot.send_message(message.chat.id, "¿Te gusta la pizza?", reply_markup=markup)
        logging.info("Pregunto el Bot: ¿Te gusta la pizza?")

    def callback_query(self, call):
        if call.data == 'pizza_si':
            self.bot.send_message(call.message.chat.id, 'Sí? Genial ---> A mí también me gusta la pizza 🍕')
            logging.info("respuesta de si: " + "Sí?" + " Genial ---> A mí también me gusta la pizza 🍕" )
        elif call.data == 'pizza_no':
            self.bot.send_message(call.message.chat.id, 'No? ----> ¡Bueno, cada quien sus gustos!')
            logging.info("respuesta de no: " + "No?" + " Bueno, cada quien sus gustos!")


    def send_image(self, message):
        img_url = 'https://www.chetu.com/img/on-demand-developers/java/java-main/logo/java-logo.png'
        logging.info("se mando una imagen de la url:" + img_url)
        self.bot.send_photo(chat_id=message.chat.id, photo=img_url, caption='Imagen de java')

    def iniciar(self):
        """Arranca el bot"""
        logging.info("Bot escuchando mensajes...")
        self.bot.polling(none_stop=True, interval=0)