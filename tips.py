from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import ChatAction
class Tip:
    def help(update, context):
        update.message.reply_text("Tienes a tu disposición los siguientes comandos:\n--------------------------------------------\n" + 
        "/suggest: Este comando te servirá para poder realizar una sugerencia/reporte anónimamente.\n" + 
        "/tip: ¿Necesitas un consejo? Adelante.\n"+
        "/protocolo: ¿Estás viviendo una situación de acoso por parte de algún miembro de la universidad?\n"+
        "/admin: Funciones de administrador")
    def protocolo(update, context):
        button1 = InlineKeyboardButton("Enlace al protocolo de acoso de la US", url="https://igualdad.us.es/?page_id=844")
        button2 = InlineKeyboardButton("Descargar pdf del protocolo de la US", callback_data='pdfprot')
        update.message.reply_text(text='Aquí dispones de información sobre cómo actuar ante una situación de acoso:', 
                                reply_markup=InlineKeyboardMarkup([
                                    [button1, button2]
                                ]))
    def pdfprot_callback_handler(update, context):
        query = update.callback_query
        query.answer()
        chat = query.message.chat
        chat.send_action(action=ChatAction.UPLOAD_DOCUMENT, timeout=None)
        file = './US-Protocolo-Acoso_Acuerdo-9.1-CG_2018-06-19.pdf'
        chat.send_document(document=open(file, 'rb'))

    def tip(update, context):
        update.message.reply_text("Has entrado en los consejos. ¿En qué podemos ayudarte?\n--------------------------------------------\n"+
        "/etsii: Consejos sobre la escuela.\n" + 
        "/us: Consejos sobre el campus.")

    
    def etsii(update, context):
        button1 = InlineKeyboardButton("Aulas", callback_data='aulas')
        button2 = InlineKeyboardButton("Departamentos", callback_data='dep')
        update.message.reply_text(text='Selecciona una opción', 
                                reply_markup=InlineKeyboardMarkup([
                                    [button1, button2]
                                ]))
        
    def classes_callback_handler(update, context):
        query = update.callback_query
        query.answer()
        query.message.reply_text("Nomenclatura de la ETSII:\n" + 
        "Ejemplo: A4.30 -> La primera letra indica el Módulo donde se encuentra situada la clase, el primer "+
        "número indica la planta y el número después del punto el número de la clase. "+
        "Entonces, la clase A4.30 se encuentra en la cuarta planta del módulo A :)")


    def deps_callback_handler(update, context):
        query = update.callback_query
        query.answer()
        button1 = InlineKeyboardButton("Planos de la ETSII", url="https://www.informatica.us.es/index.php/plan-de-autoproteccion/68-autoproteccion/1658-planos-de-la-etsii")
        query.message.reply_text("¿No sabes dónde están los departamentos de la escuela?\n" + 
        "Los departamentos están indicados en los carteles que hay en toda la escuela. ¡Síguelos y no tendrás problema!\n")
        query.message.reply_text(text="Te dejamos los planos de la escuela por si son de tu ayuda:", reply_markup= InlineKeyboardMarkup([[button1]]))

    #Consejos US
    def us(update, context):
        button1 = InlineKeyboardButton("Sitios para comer", callback_data='comida')
        button2 = InlineKeyboardButton("Sitios cómodos para estudiar", callback_data='estudiar')
        update.message.reply_text(text='Selecciona una opción', 
                                reply_markup=InlineKeyboardMarkup([
                                    [button1, button2]
                                ]))

    def food_callback_handler(update, context):
        query = update.callback_query
        query.answer()
        query.message.reply_text("En el campus hay diversos sitios para poder comer. Nosotros te recomendamos los siguientes:\n"+
        "Comedor de nuestra Escuela: Primer y segundo plato + Pan y Postre = 4'50€\n"+
        "Comedor de la Escuela de Idiomas: Primer y segundo plato + Pan y Postre = 4'10€\n" + 
        "Comedor de la Facultad de Matemáticas: Primer y segundo plato + Pan y Postre = 4'10€\n" + 
        "Bocadillos:\n"+
        "\t- Ñam-ñam: Bocadillos variados a buen precio.")

    def study_callback_handler(update, context):
        query = update.callback_query
        query.answer()
        query.message.reply_text("Te recomendamos las siguientes bibliotecas para estudiar:\n"+
        "- Biblioteca de nuestra escuela.\n"+
        "- Biblioteca de Mates\n"+
        "- CRAI Antonio de Ulloa")