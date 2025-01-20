def search_notes(notes, keyword=None, status=None):  # Функция поиска заметок
    if not notes:
        print("\nСписок заметок пуст.")
        return
    if not keyword and not status:
        print("\nКритерии для поиска не заданы.")
        return

    found_notes = []  # Список найденных заметок

    for note in notes:  # Проверка на соответствие ключевому слову
        if keyword:
            keyword_found = (
                    (note['title'].lower() == keyword.lower()) or
                    (note['content'].lower() == keyword.lower()) or
                    (note['username'].lower() == keyword.lower())
            )
        else:
            keyword_found = True

        if status:  # Проверка на соответствие статусу
            status_found = (note['status'].lower() == status.lower())
        else:
            status_found = True

        if keyword_found and status_found:  # Если обе проверки успешны, добавляем заметку в результат
            found_notes.append(note)

    if not found_notes:  # Вывод результатов поиска
        print("\nЗаметки, соответствующие критериям, не найдены.")
    else:
        display_notes(found_notes)

    return found_notes

def display_notes(notes):  # Функция для отображения заметок
    print("\nСписок найденных заметок:")
    for note_index, note in enumerate(notes, 1):
        print(f"Заметка №{note_index}:")
        print(f"Имя пользователя: {note['username']}")
        print(f"Заголовок: {note['title']}")
        print(f"Описание: {note['content']}")
        print(f"Статус: {note['status']}")
        print(f"Дата создания: {note['created_date']}")
        print(f"Дедлайн: {note['issue_date']}")
        print("-" * 15)  # Горизонтальный разделитель

notes = [
    {'username': 'Алекс', 'title': 'Продукты', 'content': 'Купить', 'status': 'Новая', 'created_date': '20-01-2025', 'issue_date': '21-01-2025'},
    {'username': 'Алекс', 'title': 'Запчасти', 'content': 'Купить', 'status': 'Новая', 'created_date': '20-01-2025', 'issue_date': '22-01-2025'},
    {'username': 'Алекс', 'title': 'Работа', 'content': 'Подготовить отчет', 'status': 'Активна', 'created_date': '15-01-2025', 'issue_date': '25-01-2025'}
]
#notes = []
search_notes(notes, keyword="продукты", status="новая")
