import random
import logging

from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Biraz logging ekleyelim.
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)


def command_start(update: Update, context: CallbackContext) -> None:
    """/start geldiginde Naber cevabi yazan komut."""
    update.message.reply_text('Naber')

def command_gonder(update: Update, context: MessageHandler)-> None:
    """"/gonder komutu geldiğinde bir gruba ya da kişiye mesaj  göndermek için """
    update.message.reply_text(random.choice(['MERHABA', 'NASILSINIZ?', 'SAAT KAÇTA BULUŞUYORUZ?', 
    'NERDESİNİZ?', ]))

def main():
    # Updater mesajlari dinleyen(algılayan) modul.
    # Buraya botfather'dan aldigimiz tokenimizi tırnak işareti icinde yaziyoruz.
    # Cunku o bir string.

    updater = Updater('5557671287:AAG3C0z4RFTsz8M7yvVFbVro2UutsyXXyfA', use_context=True)
    updater.bot.send_message(chat_id=-862377058, text="iyi abi senden naber?.")

    dispatcher = updater.dispatcher

    # Komutlarin handlerinlarini ekle
    dispatcher.add_handler(CommandHandler("start", command_start))
    dispatcher.add_handler(CommandHandler("gonder", command_gonder))

    # Mesaj algılama islemini baslat.
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
