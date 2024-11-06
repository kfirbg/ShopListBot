from telegram import Update
from telegram.ext import ContextTypes
from shop_list_manager import shop_list

async def handle_show_list(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    items = shop_list.display()
    message = f"רשימת המוצרים:\n{items}" if items else "הרשימה ריקה."
    await query.message.reply_text(message)
