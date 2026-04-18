import telebot
import requests
import json

bot = telebot.TeleBot('8588821651:AAGCBRETCLrn12gg0xQenQ-tr41Pz_W9dIw')

api_key = 'cc2ba876736132e270670f8d7ebb0aef'

base_url = 'https://api.openweathermap.org/data/2.5/weather'

@bot.message_hundler(commands = ['start'])
def send_welcome(message):
    welcome_text = (
        'Привет! я Погода-бот.\n\n'
        'ИСпользуйте команду /weather для получения прогноза.\n'
        'Пример:\n'
        '/weather Moscow\n'
        '/weather London\n'
        '/weather Tokyo\n'
        'Введите название города на английском языке'
    )
    bot.reply_to(message, welcome_text)

