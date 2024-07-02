import requests
import json
import random
import time

# URL сервера для отправки данных
temperature_url = 'http://localhost:5000/temperature'
vibration_url = 'http://localhost:5000/vibration'

def generate_random_data(temp_sensor_id, vibration_sensor_id, delay):
    while True:
        # Генерация случайных данных для температуры
        temperature_data = {
            'sensor_id': temp_sensor_id,
            'temperature': round(random.uniform(20.0, 100.0), 2),  # Случайная температура от 20.0 до 100.0
            'timestamp': time.strftime('%Y-%m-%d %H:%M:%S')  # Текущая метка времени
        }
        
        # Генерация случайных данных для уровня вибрации
        vibration_data = {
            'sensor_id': vibration_sensor_id,
            'vibration_level': round(random.uniform(0.0, 10.0), 2),  # Случайный уровень вибрации от 0.0 до 10.0
            'timestamp': time.strftime('%Y-%m-%d %H:%M:%S')  # Текущая метка времени
        }
        
        # Отправка данных на сервер
        send_data(temperature_url, temperature_data)
        send_data(vibration_url, vibration_data)
        
        # Задержка перед отправкой следующих данных (например, каждые 5 секунд)
        time.sleep(delay)

def send_data(url, data):
    response = requests.post(url, json=data)
    if response.status_code == 200:
        print(f"Данные успешно отправлены на {url}: {data}")
    else:
        print(f"Ошибка при отправке данных на {url}: {response.status_code}")
        print(response.text)

# Пример использования функции
temp_sensor_id = int(input("Введите ID датчика температуры: "))
vibration_sensor_id = int(input("Введите ID датчика вибрации: "))
delay = int(input("Введите задержку(в секундах): "))
generate_random_data(temp_sensor_id,  vibration_sensor_id, delay=5)