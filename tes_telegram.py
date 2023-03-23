"""
iniciamos bot prototipo Telegram
"""


import telebot  # Libreria de Telegram
import time
import threading  #Ejecucion denhilos o subprocesos.

from config import *

# Instanciamos el bot
bot = telebot.TeleBot(TOKEN_TELEGRAM)


# responde al comando Hola  o /start
@bot.message_handler(
    commands=["start"]
)  # Usamos decorador(una duncioin que reponde otra funcion)
def cmd_start(message):
    # Bienvanida bot
    bot.reply_to(message, "Hola como andamos!!!!")


@bot.message_handler(content_types=["text"])
def bot_mensajes_texto(message):
    """Gestiona mensajes texto recibidos"""
    # Formatos HTML
    # texto_html = '<b><u><i>Formatos convinados...</i></u></b>'
    # texto_html += '<b>NEGRITA</b>' + '\n'
    # texto_html += '<i>CURSIVA</i>' + '\n'
    # texto_html += '<u>SUBRAYADO</u>' + '\n'
    # texto_html += '<s>TACHADO</s>' + '\n'
    # texto_html += '<code>MONOESPACIO</code>' + '\n'
    # texto_html += '<span class="tg-spolier">SPOILER</span>' + '\n'
    texto_html = '<a href="https://www.serchartmann.com/">ENLACE</a>' + "\n"

    # texto markdown
    # texto_markdown = '*NEGRITA*' + '\n'
    # texto_markdown += '_CURSIVA_' + '\n'
    # texto_markdown += '__sUBRAYADO__' + '\n'
    # texto_markdown += '~TACHADO~' + '\n'
    # texto_markdown += '```MONOESPACIADO```' + '\n'
    # texto_markdown += '||SPOILER||' + '\n'
    # texto_markdown += '[ENLACE(https://www.serchartmann.com/)]' + '\n'

    if message.text.startswith("/"):
        bot.send_message(message.chat.id, "Opcion invalida...")  # recibe 2 parametros
    else:
        bot.send_chat_action(
            message.chat.id, "typing"
        )  # para que se muestre escribinedo cuando el bot va a mandar una respuesta
        x = bot.send_message(message.chat.id, texto_html, parse_mode="html")
        # bot.send_message(message.chat.id, texto_markdown, parse_mode="MarkdownV2")
        time.sleep(3)
        bot.edit_message_text(
            "<u>Adios</u>", message.chat.id, x.message_id, parse_mode="html"
        )  # editar un mensaje
        bot.delete_message(message.chat.id, x.message_id)  # eliminar mensaje del bot
        bot.delete_message(
            message.chat.id, message.message_id
        )  # elimina el mensaje del usuario
        fotos = open("./imagenes/jabones.jpeg", "rb")  # cargamos la imagen
        bot.send_photo(message.chat.id, fotos, "OFErton!!")
        archivo = open("./libros/Entrevista con el vampiro.pdf", "rb")
        bot.send_document(message.chat.id, archivo, caption="Algo de lectura")


# Incializamos
if __name__ == "__main__":
    print("Iniciando bot")
    bot.infinity_polling()  # Metodo que comprueba si se reciben mensajes nuevos
    print('Fin')