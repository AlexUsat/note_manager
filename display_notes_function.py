def display_notes(notes):  # Функция для отображения всех заметок
    if not notes:
        print("\nУ вас нет сохраненных заметок.")
        return
    print("\nСписок всех заметок:")
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
#    {'username': 'Алекс', 'title': 'Продукты', 'content': 'Купить', 'status': 'Новая', 'created_date': '20-01-2025', 'issue_date': '21-01-2025'},
#    {'username': 'Алекс', 'title': 'Запчасти', 'content': 'Купить', 'status': 'Новая', 'created_date': '20-01-2025', 'issue_date': '22-01-2025'},
    {'username': 'Алекс', 'title': 'Работа', 'content': 'Подготовить отчет', 'status': 'Активна', 'created_date': '15-01-2025', 'issue_date': '25-01-2025'}
]
#notes = []
display_notes(notes)