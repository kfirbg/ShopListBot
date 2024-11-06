from telegram import Update
from telegram.ext import ContextTypes
from Buttons.answer_with_display_list_button import answer_with_display_list_button
from shop_list_manager import shop_list

async def handle_restore_list(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if shop_list.backup_list_of_items:
        shop_list.restore()
        await answer_with_display_list_button(update ,"הרשימה שוחזרה בהצלחה.")
    else:
        await update.message.reply_text("לא ניתן לשחזר את הרשימה.")
