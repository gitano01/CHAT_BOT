import telebot
from telebot import types

TOKEN = "{{TOKEN}}"
bot = telebot.TeleBot(TOKEN)

#Creacion de comandos simples "/start" y "/help"


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message,'Hola! soy tu primer bot creado')
    
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message,'Puedes interactuar conmigo usuando comandoS. Por ahora, solo respondo a /start y /help')
    
    
# @bot.message_handler(func=lambda m: True)
# def echo_all(message):
#     bot.reply_to(message,message.text)
    
##implementar un comando para menus
@bot.message_handler(commands=['pizzas'])
def send_options(message):
    markup = types.InlineKeyboardMarkup(row_width=2)
    ##creacion de botones 
    btn_si= types.InlineKeyboardButton('Sí', callback_data='pizza_si')
    btn_no= types.InlineKeyboardButton('No', callback_data='pizza_no')
    ##agregar botones al markup
    markup.add(btn_si)
    markup.add(btn_no)
    
    ##Enviar mensaje con los botones
    bot.send_message(message.chat.id, "¿Te gusta la pizza?", reply_markup=markup)    

##Respuestas de los botones
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    if call.data == 'pizza_si':
        #bot.answer_callback_query(call.id, '¡A mí también! 🍕')
        bot.send_message(call.message.chat.id, 'Sí? Genial ---> A mí también me gusta la pizza 🍕')
    elif call.data == 'pizza_no':
        #bot.answer_callback_query(call.id, '¡Bueno, cada quien sus gustos!')
        bot.send_message(call.message.chat.id, 'No? ----> ¡Bueno, cada quien sus gustos!')
                   
##Envio de imagenes                   
@bot.message_handler(commands=['foto'])
def send_image(message):
    img_url = 'https://www.chetu.com/img/on-demand-developers/java/java-main/logo/java-logo.png'
    bot.send_photo(chat_id=message.chat.id, photo=img_url, caption='Imagen de java')
    
    
if __name__ == '__main__':
    bot.polling(none_stop=True)            