from telegram.ext import Updater, CommandHandler
import os

def start(update,context):
    update.message.reply_text("¡Hola soy SuggETSII! Aún estoy en fase de desarrollo. Os iré informando cuando tenga actualizaciones")


if __name__ == "__main__":
    token = os.environ.get("TOKEN")
    updater = Updater(token, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start',start))
    updater.start_polling()
    updater.idle()