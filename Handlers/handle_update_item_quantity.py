from telegram import Update
from telegram.ext import ContextTypes

from Buttons.answer_with_display_list_button import answer_with_display_list_button
from Buttons.answer_with_send_yes_no_buttons import answer_with_send_yes_no_buttons
from shop_list_manager import shop_list


async def handle_update_item_quantity(update: Update, quantity: int, name: str, context:ContextTypes.DEFAULT_TYPE) -> None:
    if shop_list.update_item_quantity(name, quantity):
        await answer_with_display_list_button(update, f"הכמות של {name} שונתה ל-{quantity}.")
    else:
        await answer_with_send_yes_no_buttons(update, context)