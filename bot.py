from telegram import InlineKeyboardMarkup, InlineKeyboardButton, Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = '8036423963:AAHkPQh2493Wx0FRTOQ590g1_qm9ot0BYcU'  # Coloque seu token aqui

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Envia uma mensagem com um botão que abre o Web App dentro do Telegram.
    """
    keyboard = [
        [InlineKeyboardButton("Abrir Web App", web_app={"url": "https://assinaturasnetflix.github.io/Webapp/"})]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Clique no botão para abrir o Web App:', reply_markup=reply_markup)

async def handle_webapp_data(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """
    Recebe dados enviados pelo WebApp via tg.sendData() e responde no chat.
    """
    data = update.message.web_app_data.data
    await update.message.reply_text(f"Recebi os dados do WebApp:\n{data}")

def main():
    app = ApplicationBuilder().token(TOKEN).build()
    
    app.add_handler(CommandHandler('start', start))
    app.add_handler(MessageHandler(filters.WEB_APP_DATA, handle_webapp_data))
    
    print("Bot rodando...")
    app.run_polling()

if __name__ == '__main__':
    main()