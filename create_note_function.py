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

    valid_statuses = ["Новая", "Активна", "Выполнена"]  # Возможные статусы заметки
    while True:
        print("Выберите статус заметки из предложенных:")
        for i, temp_status in enumerate(valid_statuses, 1):
            print(f"{i}. {temp_status}")
        status = input("Введите статус: ").strip().title()
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
        "username": username,
        "title": title,
        "content": content,
        "status": status,
        "created_date": created_date,
        "issue_date": issue_date.strftime("%d.%m.%Y")
    }  # Создаём словарь заметки
    return note_dict

titles = set()  # Множество для проверки уникальности заголовков
note = create_note()
print(f"\nЗаметка создана: {note}")
