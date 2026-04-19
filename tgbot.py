import telebot
import requests
import json

bot = telebot.TeleBot('8588821651:AAGCBRETCLrn12gg0xQenQ-tr41Pz_W9dIw')

api_key = 'cc2ba876736132e270670f8d7ebb0aef'

base_url = 'https://api.openweathermap.org/data/2.5/weather'

@bot.message_handler(commands = ['start'])
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

@bot.message_handler(commands = ['weather'])
def get_weather(message):
    city = message.text.replace('/weather','').strip()

    if not city:
        bot.reply_to(
            message,
            'Пожалуйста, укажите название города\n'
            'Пример: /weather Mosow'
        )
        return
    
    try:
        params = {
            'q': city,
            'appid': api_key,
            'units': 'metric',
            'lang': 'ru'
        }

        response = requests.get(base_url, params)
        data = response.json()

        if response.status_CODE != 200:
            if data.get('cod') == '404':
                bot.reply_to(message, f'Город "{city}" не найден. Проверьте написание.')
            else:
                bot.reply_to(message, 'Ошибка при получении данных о погоде.')
                return
            
            weather_desc = data['weather'][0]['description']
            temp = data['main']['temp']
            feels_like = data['main']['feels_like']
            humidity = data['main']['humidity']
            pressure = data['main']['pressure']
            wind_speed = data['main']['wind_speed']