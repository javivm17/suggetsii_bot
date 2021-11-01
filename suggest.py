from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters, PicklePersistence
import os
from datetime import datetime
from database import Suggest_database
from admin import Admin as admin 

INPUT_TEXT = 0

class Suggest:
    #Suggest functionality
    def suggest_handler(update,context):
            update.message.reply_text("Envíame la sugerencia para poder registrarla de forma anónima")
            return INPUT_TEXT

    def suggest_input(update,context):
        suggest = update.message.text
        date= str(datetime.today()).split(" ")[0]
        
        #Almacenar sugerencia en base de datos
        db = Suggest_database()
        db.insert_suggest(date,suggest)

        update.message.reply_text("Muchas gracias, tu sugerencia ha sido registrada")

        return ConversationHandler.END