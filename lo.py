import telebot
from telebot import types

bot = telebot.TeleBot('6702808694:AAECF_IBSUHlkifFJnu_EyQUarxfMwwv-Y8')

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Selamat datang!, Masukkan nomor HP:")

@bot.message_handler(content_types=['text'])
def get_location(message):
    if message.text.startswith("0"):
        try:
            print(message.text)
            response = requests.get(f"https://ipapi.co/{message.text}/json/").json()
            kota = response['region']
            wilayah = response['region_code']
            ip = response['ip']

            bot.send_message(message.chat.id, f"IP: {ip}, Negara: {response['country_name']}, Wilayah: {wilayah}, Kota: {kota}")
        except Exception as e:
            bot.reply_to(message, f"ERROR: {e}")
    else:
        bot.send_message(message.chat.id, "Usage: /start <number>")

TOKEN = '6702808694:AAECF_IBSUHlkifFJnu_EyQUarxfMwwv-Y8'

if __name__ == '__main__':
    bot.infinity_polling()