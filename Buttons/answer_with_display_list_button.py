from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup


async def answer_with_display_list_button(update: Update, text: str) -> None:
    markup = InlineKeyboardMarkup([[InlineKeyboardButton("הצג רשימה", callback_data="show_list")]])

    if update.callback_query:
        await update.callback_query.message.reply_text(text, reply_markup=markup)
    else:
        await update.message.reply_text(text, reply_markup=markup)
