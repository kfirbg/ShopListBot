from telegram import Update

from Handlers.handle_add_item_to_the_list import handle_add_item_to_the_list


# פונקציה שמטפלת בלחיצה על כפתור כן או לא
async def handle_button_click(update: Update, context):
    message_text = context.user_data.get('item_name')
    query = update.callback_query
    await query.answer()

    # בדיקה מה המשתמש לחץ, ועדכון ההודעה בהתאם
    if query.data == 'yes':
        await query.edit_message_text(text="לחצת על 'כן', המוצר התווסף לרשימת הקניות")
        await handle_add_item_to_the_list(update, message_text)
    elif query.data == 'no':
        await query.edit_message_text(text="לחצת על 'לא'")
