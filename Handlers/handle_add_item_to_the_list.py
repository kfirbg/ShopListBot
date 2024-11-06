from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from Buttons.answer_with_display_list_button import answer_with_display_list_button
from shop_list_manager import shop_list


async def handle_add_item_to_the_list(update: Update, message_text: str) -> None:
    parts = message_text.split(" ")
    quantity = int(parts[1])
    item_name = " ".join(parts[2:])

    # בדוק אם המוצר כבר קיים ברשימה
    if any(item.name  == item_name for item in shop_list.list_of_items):
        await update.message.reply_text(f"המוצר '{item_name}' כבר קיים ברשימה.")
    else:
        shop_list.add_item(quantity, item_name)
        await answer_with_display_list_button(update, f"הוספת {quantity} {item_name} לרשימה.")