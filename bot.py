from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters
import os
import sqlite3
from datetime import datetime

INPUT_TEXT = 0

#CODE
def start(update,context):
    update.message.reply_text("¡Hola soy SuggETSII! Aún estoy en fase de desarrollo. Os iré informando cuando tenga actualizaciones")

def suggest_handler(update,context):
        update.message.reply_text("Envíame la sugerencia para poder registrarla de forma anónima")
        return INPUT_TEXT

def suggest_input(update,context):
    suggest = update.message.text
    date= datetime.today()
    #Almacenar sugerencia en base de datos
    update.message.reply_text("Muchas gracias, tu sugerencia ha sido registrada, enviame ahora un título")
    print("Sugerencia: "+suggest+" || "+str(date))

    return ConversationHandler.END


if __name__ == "__main__":
    token = os.environ.get("TOKEN")
    updater = Updater(token, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start',start))
    
    dp.add_handler(ConversationHandler(
        entry_points=[
            CommandHandler('suggest',suggest_handler)
        ],
        states={
            INPUT_TEXT:[MessageHandler(Filters.text, suggest_input)] 
        },
        fallbacks=[]
    ))
    updater.start_polling()
    updater.idle()