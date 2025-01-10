from datetime import datetime

current_date = datetime.now().date()  # Получаем текущую дату без учета времени
print(f"Текущая дата: {current_date.strftime("%d.%m.%Y")}")  # Выводим текущую дату в нужном формате

while True:  # Цикл проверки формата ввода даты дедлайна
    issue_date = input("Введите дату дедлайна в формате 'дд.мм.гггг' (например, 01.01.2025): ").strip()
    try:
        issue_date = datetime.strptime(issue_date, "%d.%m.%Y").date()  # Преобразуем строку в объект datetime и берем только дату
        break  # Выходим из цикла, если формат верный
    except ValueError:
        print("Неверный формат даты. Попробуйте снова")

delta = (issue_date - current_date).days  # Рассчитываем разницу в днях между текущей датой и дедлайном
if delta < 0:
    print(f"Дедлайн истёк {abs(delta)} дней назад.")
elif delta == 0:
    print("Дедлайн истекает сегодня!")
else:
    print(f"До дедлайна осталось {delta} дней.")

