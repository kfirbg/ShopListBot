from telegram import Update
from telegram.ext import ContextTypes
from shop_list_manager import shop_list

async def handle_reset_list(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if shop_list.list_of_items:
        shop_list.reset()
        await update.message.reply_text("הרשימה נמחקה בהצלחה, אם תרצה לשחזר את הרשימה יש לכתוב 'שחזר את הרשימה'.")
    else:
        await update.message.reply_text("לא ניתן למחוק מכיוון שהרשימה ריקה.")
