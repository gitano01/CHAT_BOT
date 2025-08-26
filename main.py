import logging
from chatbot import ChatBot

##Configuracion de logs 
logging.basicConfig(
    level=logging.DEBUG,    
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )

def main():
    bot = ChatBot("VictorBot")
    bot.iniciar()

if __name__ == "__main__":
    main()

    
          