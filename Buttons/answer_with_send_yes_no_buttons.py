from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup


async def  answer_with_send_yes_no_buttons(update: Update, context):
    user_input_text = update.message.text
    context.user_data['item_name'] = user_input_text
    keyboard = [
        [InlineKeyboardButton("כן", callback_data='yes'), InlineKeyboardButton("לא", callback_data='no')]
    ]
    help_text = (
        "המוצר לא נמצא ברשימה.\n"
         "תרצה להוסיף אותו?")
    await update.message.reply_text(help_text, reply_markup=InlineKeyboardMarkup(keyboard))