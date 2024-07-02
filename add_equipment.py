import requests

# URL сервера
url = 'http://localhost:5000/equipment'

def add_equipment(name, location):
    # Данные для отправки на сервер
    payload = {
        'name': name,
        'location': location,
    }
    
    # Отправка POST-запроса на сервер
    response = requests.post(url, json=payload)
    
    # Проверка статуса ответа
    if response.status_code == 201:
        print('Оборудование успешно добавлено.')
        print('ID оборудования:', response.json()['equipment_id'])
    else:
        print('Ошибка при добавлении оборудования:', response.status_code)
        print(response.text)

# Пример использования функции
name = input("Введите имя оборудования: ")
location = input("Введите местоположение оборудования: ")

add_equipment(name, location)