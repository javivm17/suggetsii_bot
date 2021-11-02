from telegram.ext import Updater, CommandHandler, ConversationHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import os

def start(update,context):
    update.message.reply_text("¡Hola soy SuggETSII!\nPara poder ver los comandos disponibles escribe /help.")

def tip(update, context):
    update.message.reply_text("Has entrado en los consejos. ¿En qué podemos ayudarte?\n"+
    "/etsii: Consejos sobre la escuela.\n" + 
    "/us: Consejos sobre el campus.")

def etsii(update, context):
    update.message.reply_text("Aulas: /aulas\n" + 
    "Departamentos: /dep\n")

#Consejos ETSII
def aulas(update, context):
    update.message.reply_text("Nomenclatura de la ETSII:\n" + 
    "Ejemplo: A4.30 -> La primera letra indica el Módulo donde se encuentra situada la clase, el primer "+
    "número indica la planta y el número después del punto el número de la clase. "+
    "Entonces, la clase A4.30 se encuentra en la cuarta planta del módulo A :)")

def dep(update, context):
    pass

def us(update, context):
    button1 = InlineKeyboardButton("Sitios para comer", callback_data='comida')
    button2 = InlineKeyboardButton("Sitios cómodos para estudiar", callback_data='estudiar')
    update.message.reply_text(text='Selecciona una opción', 
                              reply_markup=InlineKeyboardMarkup([
                                  [button1, button2]
                              ]))
#Consejos US
def food_callback_handler(update, context):
    query = update.callback_query
    query.answer()
    query.message.reply_text("En el campus hay diversos sitios para poder comer. Nosotros te recomendamos los siguientes:\n"+
    "Comedor de nuestra Escuela: Primer y segundo plato + Pan y Postre = 4'50€\n"+
    "Comedor de la Escuela de Idiomas: Primer y segundo plato + Pan y Postre = 4'10€\n" + 
    "Comedor de la Facultad de Matemáticas: Primer y segundo plato + Pan y Postre = 4'10€\n" + 
    "Bocadillos:\n"+
    "\t-Ñam-ñam: Bocadillos variados a buen precio.\n"
    "\t-Bocatería del pasillo: bocatas a euroxd")

def study_callback_handler(update, context):
    query = update.callback_query
    query.answer()
    query.message.reply_text("Te recomendamos las siguientes bibliotecas para estdiar:\n"+
    "- Biblioteca de nuestra escuela.\n"+
    "- Biblioteca de Mates\n"+
    "- CRAI Antonio de Ulloa jeje")

def help(update, context):
    update.message.reply_text("Tienes a tu disposición los siguientes comandos:\n " + 
    "/suggest: Este comando te servirá para poder realizar una sugerencia/reporte anónimamente.\n " + 
    "/tip: ¿Necesitas un consejo? Adelante.")

if __name__ == "__main__":
    #token = os.environ.get("TOKEN")
    token = "2073305103:AAEBMK382P0oXh8LLV1vKa-YQdVSpqEmPb0"
    updater = Updater(token, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start',start))
    dp.add_handler(CommandHandler('tip',tip))
    dp.add_handler(CommandHandler('etsii',etsii))
    dp.add_handler(CommandHandler('aulas',aulas))
    dp.add_handler(CommandHandler('dep',dep))

    dp.add_handler(CommandHandler('us',us))
    dp.add_handler(ConversationHandler(
        entry_points=[
            CallbackQueryHandler(pattern='comida', callback=food_callback_handler),
            CallbackQueryHandler(pattern='estudiar', callback=study_callback_handler)
        ], 
        states= {},
        fallbacks=[]
    ))

    dp.add_handler(CommandHandler('help',help))
    updater.start_polling()
    updater.idle()