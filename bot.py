from telegram import InlineKeyboardMarkup, InlineKeyboardButton, Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = 'SEU_TOKEN_AQUI'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Abrir Web App", web_app={"url": "https://assinaturasnetflix.github.io/webapp/"})]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text('Clique no botão para abrir o Web App:', reply_markup=reply_markup)

async def handle_webapp_data(update: Update, context: ContextTypes.DEFAULT_TYPE):
    data = update.message.web_app_data.data
    await update.message.reply_text(f"Recebi os dados do WebApp:\n{data}")

def has_webapp_data(update: Update):
    return update.message is not None and update.message.web_app_data is not None

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler('start', start))

    # Usando filtro customizado para capturar web_app_data
    app.add_handler(MessageHandler(filters.MessageFilter(has_webapp_data), handle_webapp_data))

    print("Bot rodando...")
    app.run_polling()

if __name__ == '__main__':
    main()
