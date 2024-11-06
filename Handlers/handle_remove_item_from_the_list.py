from telegram import Update
from Buttons.answer_with_display_list_button import answer_with_display_list_button
from shop_list_manager import shop_list


async def handle_remove_item_from_the_list(update: Update, name: str) -> None:
    if shop_list.remove_item(name):
        await answer_with_display_list_button(update, f"המוצר {name} נמחק מהרשימה.")
    else:
        await update.message.reply_text(f"המוצר {name} לא נמצא ברשימה.")