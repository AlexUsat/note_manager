def del_notes(notes, criterion, value):  # Удаляет заметки из списка по заданному критерию

    found = 0
    j = 0
    while j < len(notes):
        if notes[j].get(criterion, "").lower() == value.lower():
            found = 1
            del notes[j]  # Удаляем заметку из списка
        else:
            j += 1  # Переходим к следующей заметке, если текущая не соответствует
    if found == 0:
        print(f"Заметки по {criterion} '{value}' не найдены.")
    else:
        print(f"Заметки по {criterion} '{value}' успешно удалены.")
    return notes

notes = [
    {"name": "Алексей", "title": "Покупки", "description": "Купить продукты на неделю"},
    {"name": "Мария", "title": "Учеба", "description": "Подготовиться к экзамену"},
    {"name": "Алексей", "title": "Работа", "description": "Подготовить отчет"}
]

while True:
    print("\nТекущие заметки:")
    for i, note in enumerate(notes, 1):
        print(f"{i}. Имя: {note['name']}\n   Заголовок: {note['title']}\n   Описание: {note['description']}")

    print("\nВыберите действие:")
    print("1. Удалить заметку по имени")
    print("2. Удалить заметку по заголовку")
    print("3. Выход")

    choice = input("Введите номер действия: ").strip()

    if choice == "1":
        name = input("Введите имя для удаления заметок: ").strip()
        notes = del_notes(notes, "name", name)
    elif choice == "2":
        title = input("Введите заголовок для удаления заметок: ").strip()
        notes = del_notes(notes, "title", title)
    elif choice == "3":
        print("Выход из программы")
        break
    else:
        print("Некорректный ввод. Попробуйте снова")