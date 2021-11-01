from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters, PicklePersistence
import os
from datetime import datetime
from database import Suggest_database
from admin import Admin as admin 
from suggest import Suggest as suggest


INPUT_TEXT = 0
INPUT_PASS = 0
INPUT_EXIT = 0
INPUT_DELETE=0

#Start message
def start(update,context):
    update.message.reply_text("¡Hola soy SuggETSII! Aún estoy en fase de desarrollo. Os iré informando cuando tenga actualizaciones")
    
#Main function
if __name__ == "__main__":
    #token = os.environ.get("TOKEN")
    persistence = PicklePersistence(filename='conversationbot')
    token = "2061681773:AAHMkxsAb8ASIRgjFGTLbaWbwDcpZA8oOXs"
    updater = Updater(token, use_context=True, persistence=persistence)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start',start))
    
    dp.add_handler(ConversationHandler(
        entry_points=[
            CommandHandler('suggest',suggest.suggest_handler)
        ],
        states={
            INPUT_TEXT:[MessageHandler(Filters.text, suggest.suggest_input)]
        },
        fallbacks=[]
    ))

    dp.add_handler(ConversationHandler(
        entry_points=[
            CommandHandler('admin', admin.admin_handler)
        ],
        states={
            INPUT_PASS:[MessageHandler(Filters.text, admin.admin_input)]
        },
        fallbacks=[],
        name="my_conversation2",
        persistent=True,
    ))
    
    dp.add_handler(ConversationHandler(
        entry_points=[
            CommandHandler('logout',admin.salir)
        ],
        states={
            INPUT_EXIT:[MessageHandler(Filters.text, admin.input_exit)]
        },
        fallbacks=[],
        name="my_conversation2",
        persistent=True,
    ))
    dp.add_handler(CommandHandler('list',admin.listar))
    
    dp.add_handler(ConversationHandler(
        entry_points=[
            CommandHandler('delete',admin.delete_handler)
        ],
        states={
            INPUT_DELETE:[MessageHandler(Filters.text, admin.delete_input)],
        },
        fallbacks=[],
        name="my_conversation2",
        persistent=True,
    ))

    updater.start_polling()
    updater.idle()