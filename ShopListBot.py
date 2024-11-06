from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import MessageHandler, filters, ContextTypes, CallbackQueryHandler, CommandHandler, ApplicationBuilder

from Buttons.answer_with_send_yes_no_buttons import answer_with_send_yes_no_buttons
from Handlers.handle_display_list import handle_display_list
from Handlers.handle_add_item_to_the_list import handle_add_item_to_the_list
from Handlers.handle_button_click_yes_no import handle_button_click
from Handlers.handle_reset_list import handle_reset_list
from Handlers.handle_show_list import handle_show_list
from Handlers.handle_remove_item_from_the_list import handle_remove_item_from_the_list
from Handlers.handle_restore_list import handle_restore_list
from Handlers.handle_update_item_quantity import handle_update_item_quantity
from keep_alive import keep_alive

keep_alive()

async def shoplisBot(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message_text = update.message.text.lower()

    if "הוסף" in message_text:
        try:
            await handle_add_item_to_the_list(update, message_text)
        except (IndexError, ValueError):
            await update.message.reply_text("שגיאה: ודא שאתה משתמש בפורמט הנכון - 'הוסף <כמות> <שם מוצר>'.")

    elif "הצג רשימה" in message_text:
        await handle_display_list(update)

    elif "שנה" in message_text:
        try:
            parts = message_text.split(" ")
            quantity = int(parts[1])
            name_to_edit = " ".join(parts[2:])
            await handle_update_item_quantity(update, quantity, name_to_edit, context)
        except (IndexError, ValueError):
            await update.message.reply_text("שגיאה: ודא שאתה משתמש בפורמט הנכון - 'ערוך <כמות> <שם מוצר>'.")

    elif "מחק רשימה" in message_text:
        try:
            await handle_reset_list(update, context)
        except:
            await update.message.reply_text("עקב שגיאה לא היה ניתן למחוק את הרשימה הקיימת.")

    elif "שחזר רשימה" in message_text:
        try:
            await handle_restore_list(update, context)
        except:
            await update.message.reply_text("עקב שגיאה לא היה ניתן למחוק את הרשימה הקיימת.")

    elif "מחק" in message_text:
        try:
            parts = message_text.split(" ")
            name_to_remove = " ".join(parts[1:])
            await handle_remove_item_from_the_list(update, name_to_remove)
        except IndexError:
            await update.message.reply_text("שגיאה: ודא שאתה משתמש בפורמט הנכון - 'מחק <שם מוצר>'.")

    else:
        help_text = (
            "הפקודה לא נכונה. הנה האפשרויות הזמינות:\n\n"
            "1. הוסף <כמות> <שם מוצר> - להוסיף פריט לרשימה.\n"
            "2. הצג רשימה - להציג את כל הפריטים ברשימה.\n"
            "3. שנה <כמות> <שם מוצר> - לשנות את הכמות של פריט קיים.\n"
            "4. מחק רשימה - למחוק את כל הרשימה.\n"
            "5. שחזר רשימה - לשחזר את הרשימה הקודמת שנמחקה.\n"
            "6. מחק <שם מוצר> - להסיר פריט מסוים מהרשימה.\n\n"
            "אנא נסה שנית עם אחת מהפקודות הנ\"ל."
        )
        await update.message.reply_text(help_text)

async def start(update: Update, context):
    keyboard = [
        [InlineKeyboardButton("כן", callback_data='yes'), InlineKeyboardButton("לא", callback_data='no')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text("כן או לא?", reply_markup=reply_markup)



def main():
    application = ApplicationBuilder.token("7011966180:AAFbc2gwpjQvMAlUv_ckutQlq9lM7RBfHeU").build()
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, shoplisBot))

    application.add_handler(CallbackQueryHandler(handle_show_list, pattern="^show_list$"))
    application.add_handler(CommandHandler("start", answer_with_send_yes_no_buttons))
    application.add_handler(CallbackQueryHandler(handle_button_click, pattern="^(yes|no)$"))

    application.run_polling()

if __name__ == '__main__':
    main()
