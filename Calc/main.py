import logging
from config import TOKEN
from telegram import ForceReply, Update
from telegram.ext import (
    Application, CommandHandler, 
    ContextTypes, CallbackQueryHandler,
    ConversationHandler
    )


import controller
import model_sum
import model_keyboard as kb

CHOICE = 0


# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)




if __name__ == "__main__":
    application = Application.builder().token(TOKEN).build()
    conv_handler = ConversationHandler(
        entry_points=[
            CommandHandler("start", controller.start)
        ],
        states={
            CHOICE: [
                CallbackQueryHandler(controller.cheice),
            ],
        },
        fallbacks=[
            CommandHandler("stop", controller.stop),
        ],
    )
    
    application.add_handler(conv_handler)
    application.add_handler(CommandHandler('help', controller.help))
    
    application.run_polling()