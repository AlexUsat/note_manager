from datetime import datetime

def create_note():  # Функция создания новой заметки
    print('"\nДобро пожаловать в "Менеджер заметок"! Вы можете добавить новую заметку.')
    username = input("Введите имя пользователя: ").strip()

    while True:  # Цикл по добавлению заголовка
        title = input("Введите заголовок: ").strip()
        if not title:
            print("Заголовок не может быть пустым. Попробуйте снова")
        elif title in titles:  # Проверка на уникальность заголовка
            print("Заголовок уже существует. Попробуйте другой")
        else:
            titles.add(title)  # Добавляем заголовок в список уникальных
            break

    content = input("Введите описание: ").strip()

    valid_statuses = ["Выполнена", "Активна", "Отложена"]  # Возможные статусы заметки
    while True:
        print("Выберите статус заметки из предложенных:")
        for k, temp_status in enumerate(valid_statuses, 1):
            print(f"{k}. {temp_status}")
        status = input("Введите статус: ").strip()
        if status in valid_statuses:  # Проверяем корректность ввода
            print("Статус успешно добавлен")
            break
        else:
            print("Некорректный ввод. Попробуйте снова")

    created_date = datetime.now().date().strftime("%d.%m.%Y")  # Получаем текущую дату в формате "дд.мм.гггг"

    while True:  # Цикл проверки формата ввода даты дедлайна
        issue_date = input("Введите дату дедлайна в формате 'дд.мм.гггг' (например, 01.01.2025): ").strip()
        try:
            issue_date = datetime.strptime(issue_date,"%d.%m.%Y").date()  # Преобразуем строку в объект datetime и берем только дату
            break  # Выходим из цикла, если формат верный
        except ValueError:
            print("Неверный формат даты. Попробуйте снова")

    note_dict = {
        "Имя": username,
        "Заголовок": title,
        "Описание": content,
        "Статус": status,
        "Дата создания": created_date,
        "Дедлайн": issue_date.strftime("%d.%m.%Y")
    }  # Создаём словарь заметки
    return note_dict


notes = []  # Список для хранения всех заметок
titles = set()  # Множество для проверки уникальности заголовков
while True:  # Цикл создания новых заметок
    note = create_note()
    notes.append(note)
    print("Заметка успешно добавлена!")

    # Спрашиваем пользователя, хочет ли он добавить ещё одну заметку
    add_more = input("\nХотите добавить ещё одну заметку? (да/нет): ").strip().lower()
    if add_more != "да":
        break

print("\nСписок всех заметок:")
for i, note in enumerate(notes, 1):
    print(f"\nЗаметка {i}:")
    for key, value in note.items():
        print(f"{key}: {value}")
