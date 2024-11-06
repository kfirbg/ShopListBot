from telegram import Update

from shop_list_manager import shop_list


async def handle_display_list(update: Update) -> None:
    items = shop_list.display()
    if items:
        await update.message.reply_text(f"רשימת המוצרים:\n{items}")
    else:
        await update.message.reply_text("הרשימה ריקה.")