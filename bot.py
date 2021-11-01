from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters, PicklePersistence
import os
from datetime import datetime
from database import Suggest_database 

INPUT_TEXT = 0
INPUT_PASS = 0
INPUT_EXIT = 0
INPUT_DELETE=0

#Start message
def start(update,context):
    update.message.reply_text("¡Hola soy SuggETSII! Aún estoy en fase de desarrollo. Os iré informando cuando tenga actualizaciones")
    

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

#Log in administrator
def admin_handler(update,context):
    update.message.reply_text("Inicia sesión escribiendo tu usuario y contraseña separado por espacios")
    return INPUT_PASS


def admin_input(update,context):
    suggest = update.message.text
    user = suggest.split(" ")[0]
    password = suggest.split(" ")[1]
    if(user=="admin" and password=="admin"):
        context.user_data["logged"] = True
        update.message.reply_text("Has iniciado sesión como administrador!")
        update.message.reply_text("¿Que deseas hacer? \n--------------------------------------------\nListar sugerencias -> /list\nCerrar sesion -> /logout")
        return ConversationHandler.END
    else:
        update.message.reply_text("El usuario o la contraseña son incorrectos, vuelve a intentarlo")


#Suggest list
def listar(update, context):
    try:
        if (context.user_data["logged"]==True):
            update.message.reply_text("Listando sugerencias...")
            db = Suggest_database()
            data = db.get_suggests()
            text = ""
            for item in data:
                text += "Id: "+str(item[0])+"\nFecha: "+str(item[1])+"\nSugerencia: "+str(item[2])+"\n\n"
            update.message.reply_text(text)
            
        else:
            update.message.reply_text("Necesitas iniciar sesion como administrador")
        return ConversationHandler.END
    except:
        update.message.reply_text("Necesitas iniciar sesion como administrador")
        return ConversationHandler.END

#Delete suggest
def delete_handler(update, context):
    try:
        if (context.user_data["logged"]==True):
            update.message.reply_text("Dime el Id de la sugerencia que quieres eliminar")  
            return INPUT_DELETE
        else:
            update.message.reply_text("Necesitas iniciar sesion como administrador")
        return ConversationHandler.END
    except:
        update.message.reply_text("Necesitas iniciar sesion como administrador")
        return ConversationHandler.END

def delete_input(update,context):
    suggest_id = update.message.text
    db = Suggest_database()
    db.delete_suggest(suggest_id)
    update.message.reply_text("La sugerencia con id: "+str(suggest_id)+" ha sido eliminada con exito")
    return ConversationHandler.END
    
#Log out administrator
def salir(update,context):
    update.message.reply_text("¿Está seguro que desea salir? (Y/N)")
    return INPUT_EXIT

def input_exit(update,context):
    try:
        if(update.message.text=="Y"): 
            context.user_data["logged"]=False
            update.message.reply_text("Se ha cerrado sesión correctamente")
        return ConversationHandler.END
    except:
        return ConversationHandler.END


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
            CommandHandler('suggest',suggest_handler)
        ],
        states={
            INPUT_TEXT:[MessageHandler(Filters.text, suggest_input)]
        },
        fallbacks=[]
    ))


    dp.add_handler(ConversationHandler(
        entry_points=[
            CommandHandler('admin',admin_handler)
        ],
        states={
            INPUT_PASS:[MessageHandler(Filters.text, admin_input)]
        },
        fallbacks=[],
        name="my_conversation2",
        persistent=True,
    ))
    
    dp.add_handler(ConversationHandler(
        entry_points=[
            CommandHandler('logout',salir)
        ],
        states={
            INPUT_EXIT:[MessageHandler(Filters.text, input_exit)]
        },
        fallbacks=[],
        name="my_conversation2",
        persistent=True,
    ))
    dp.add_handler(CommandHandler('list',listar))
    
    dp.add_handler(ConversationHandler(
        entry_points=[
            CommandHandler('delete',delete_handler)
        ],
        states={
            INPUT_DELETE:[MessageHandler(Filters.text, delete_input)],
        },
        fallbacks=[],
        name="my_conversation2",
        persistent=True,
    ))

    updater.start_polling()
    updater.idle()