import telebot
from telebot import types
from reg import user_exists, add_user_to_list, add_to_blacklist, is_user_banned
from config import TOKEN, ADMIN_ID, START_MESSAGE

bot = telebot.TeleBot(TOKEN)

@bot.callback_query_handler(func=lambda call: call.data.startswith('add_to_blacklist'))
def add_to_blacklist_callback(call):
    try:
        user_id = call.data.split('_')[-1]
        add_to_blacklist(user_id)
        bot.send_message(call.message.chat.id, f"User {user_id} has been added to the blacklist!")
    except Exception as e:
        print(f"An error occurred in add_to_blacklist_callback: {e}")

@bot.message_handler(commands=['start'])
def handle_start(message):
    try:
        user_id = message.from_user.id
        if not user_exists(user_id):
            add_user_to_list(user_id)

        bot.send_message(user_id, START_MESSAGE)
    except Exception as e:
        print(f"An error occurred in handle_start: {e}")

@bot.message_handler(content_types=['text', 'photo', 'video', 'document', 'audio', 'sticker', 'voice'])
def handle_content(message):
    try:
        user = message.from_user
        user_id = user.id
        user_name = user.username if user.username else user.full_name

        if is_user_banned(user_id):
            bot.send_message(user_id, "Your message was not delivered because you are on the blacklist!")
        else:
            bot.forward_message(ADMIN_ID, user_id, message.message_id)
            markup = types.InlineKeyboardMarkup()
            button = types.InlineKeyboardButton(text="Add to blacklist", callback_data=f"add_to_blacklist_{user_id}")
            markup.add(button)
            bot.send_message(ADMIN_ID, f"Message from user @{user_name}", reply_markup=markup)
                             
            bot.send_message(user_id, "Your message has been delivered to the moderators!")

    except Exception as e:
        print(f"An error occurred in handle_content: {e}")

bot.polling('')