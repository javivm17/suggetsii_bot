from telegram.ext import Updater, CommandHandler, ConversationHandler, CallbackQueryHandler
from tips import Tip as tipp

def start(update,context):
    update.message.reply_text("¡Hola soy SuggETSII!\nPara poder ver los comandos disponibles escribe /help.")


if __name__ == "__main__":
    token = "2073305103:AAEBMK382P0oXh8LLV1vKa-YQdVSpqEmPb0"
    updater = Updater(token, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start',start))
    dp.add_handler(CommandHandler('tip',tipp.tip))
    dp.add_handler(CommandHandler('etsii',tipp.etsii))
    dp.add_handler(CommandHandler('protocolo',tipp.protocolo))

    dp.add_handler(CommandHandler('us',tipp.us))
    dp.add_handler(ConversationHandler(
        entry_points=[
            CallbackQueryHandler(pattern='comida', callback=tipp.food_callback_handler),
            CallbackQueryHandler(pattern='estudiar', callback=tipp.study_callback_handler),
            CallbackQueryHandler(pattern='aulas', callback=tipp.classes_callback_handler),
            CallbackQueryHandler(pattern='dep', callback=tipp.deps_callback_handler),
            CallbackQueryHandler(pattern='pdfprot', callback=tipp.pdfprot_callback_handler)
        ], 
        states= {},
        fallbacks=[]
    ))

    dp.add_handler(CommandHandler('help',tipp.help))
    updater.start_polling()
    updater.idle()