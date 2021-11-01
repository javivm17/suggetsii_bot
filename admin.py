from telegram.ext import Updater, CommandHandler, ConversationHandler, MessageHandler, Filters, PicklePersistence
import os
from datetime import datetime
from database import Suggest_database 

INPUT_PASS = 0
INPUT_EXIT = 0
INPUT_DELETE = 0

class Admin:
    def admin_handler(update,context):
        update.message.reply_text("Inicia sesión escribiendo tu usuario y contraseña separado por espacios")
        return INPUT_PASS


    def admin_input(update,context):
        suggest = update.message.text
        try:
            user = suggest.split(" ")[0]
            password = suggest.split(" ")[1]
            if(user==str(os.environ.get("ADMIN_USER")) and password==str(os.environ.get("ADMIN_PASSWORD"))):
                context.user_data["logged"] = True
                update.message.reply_text("Has iniciado sesión como administrador!")
                update.message.reply_text("¿Que deseas hacer? \n--------------------------------------------"+
                "\nListar sugerencias -> /list\nEliminar sugerencia -> /delete\nCerrar sesion -> /logout")
                return ConversationHandler.END
            else:
                update.message.reply_text("El usuario o la contraseña son incorrectos, vuelve a intentarlo de nuevo /admin")
                return ConversationHandler.END
        except:
            update.message.reply_text("El usuario o la contraseña son incorrectos, vuelve a intentarlo de nuevo /admin")
            return ConversationHandler.END
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
        try:
            if (context.user_data["logged"]==True):
                update.message.reply_text("¿Está seguro que desea salir? (Y/N)")
                return INPUT_EXIT
            else:
                update.message.reply_text("Necesitas iniciar sesion como administrador")
            return ConversationHandler.END
        except:
            update.message.reply_text("Necesitas iniciar sesion como administrador")
            return ConversationHandler.END

    def input_exit(update,context):
        try:
            if(update.message.text=="Y"): 
                context.user_data["logged"]=False
                update.message.reply_text("Se ha cerrado sesión correctamente")
            return ConversationHandler.END
        except:
            return ConversationHandler.END

        