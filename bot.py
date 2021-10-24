from telegram.ext import Updater, CommandHandler

def start(update,context):
    update.message.reply_text("Hola bienvenido al bot de sugerencias de la ETSII!")

if __name__ == "__main__":
    token="2095086657:AAH4Xe5wNiti44SifiV1P3IojocfdVQkfKI"
    updater = Updater(token, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start',start))
    updater.start_polling()
    updater.idle()