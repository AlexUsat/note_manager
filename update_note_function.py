from datetime import datetime

def update_note(note):  # Функция обновления данных заметки
    data = ["username", "title", "content", "status", "issue_date"]  # Список с возможными полями для обновления
    print(f"Текущие данные заметки: {note}")
    while True:
        update_data = input("Какие данные вы хотите обновить? (username, title, content, status, issue_date): ").strip().lower()
        if not update_data:
            print("Данное поле не может быть пустым. Попробуйте снова")
        elif update_data in data:  # Проверяем корректность ввода
            new_value = input(f"Введите новое значение для '{update_data}': ").strip()

            if update_data == "issue_date":
                try:
                    datetime.strptime(new_value,"%d.%m.%Y")  # Преобразуем строку в объект datetime и берем только дату
                except ValueError:
                    print("Неверный формат даты. Попробуйте снова")
                    continue

            note[update_data] = new_value  # Обновляем значения поля данных заметки
            break
        else:
            print("Некорректный ввод. Попробуйте снова")
    return note

note = {
    'username': 'Алекс',
    'title': 'Продукты',
    'content': 'Купить',
    'status': 'Новая',
    'created_date': '20-01-2025',
    'issue_date': '21-01-2025'
}
update_note = update_note(note)
print(f"Заметка обновлена: {update_note}")