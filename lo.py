import requests

def get_location(phone_number):
    url = f'https://api.ipapi.com/{phone_number}'
    response = requests.get(url)
    data = response.json()
    return data

import telebot

bot = telebot.TeleBot('6702808694:AAECF_IBSUHlkifFJnu_EyQUarxfMwwv-Y8')

@bot.message_handler(commands=['location'])
def send_location(update, context):
    arg = context.args
    if len(arg) != 1:
        bot.send_message(chat_id=update.effective_chat.id, text="Usage: /location <phone_number>")
        return

    phone_number = arg[0]
    location = get_location(phone_number)
    bot.send_message(chat_id=update.effective_chat.id, text=f"Lokasi: {location['city']}, Negara: {location['country_name']}")

if __name__ == '__main__':
    bot.polling()