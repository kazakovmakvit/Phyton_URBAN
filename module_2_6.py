import json

persona_object = {
    'name': input('Введите имя: '),
    'age': input('Введите возраст: '),
    'sity': input('Введите город: ')
}

print('______________________________')
for key, value in persona_object.items():
    print(f'{key}: {value}')


def save_info():
    try:
        with open('persona_object.json', 'w', encoding='utf-8') as file:
            json.dump(persona_object, file, indent=4, ensure_ascii=False)
        print("Данные успешно записаны в файл.")
    except IOError:
        print("Ошибка при записи в файл.")
    except json.JSONEncodeError:
        print("Ошибка при кодировании JSON.")

save_info()
