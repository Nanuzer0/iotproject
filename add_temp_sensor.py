import requests

# URL сервера
url = 'http://localhost:5000/tempsensors'

def add_sensor(equipment_id, description):
    # Данные для отправки на сервер
    payload = {
        'equipment_id': equipment_id,
        'description': description,
    }
    
    # Отправка POST-запроса на сервер
    response = requests.post(url, json=payload)
    
    # Проверка статуса ответа
    if response.status_code == 201:
        print('Датчик успешно добавлен.')
        print('ID датчика:', response.json()['sensor_id'])
    else:
        print('Ошибка при добавлении датчика:', response.status_code)
        print(response.text)

# Пример использования функции
equipment_id = input("Введите ID оборудования: ")
description = input("Введите описание: ")

add_sensor(equipment_id, description)