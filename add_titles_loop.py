titles = set()
print("Введите заголовки заметок (оставьте ввод пустым или введите 'стоп', чтобы завершить):")

while True:
    title = input("Введите заголовок: ").strip()  # Удаляем лишние пробелы по краям
    if title.lower() == "стоп" or title == "":  # Проверяем условие завершения
        break
    if title in titles:  # Проверяем уникальность заголовка
        print("Этот заголовок уже добавлен. Попробуйте другой.")
    else:
        titles.add(title)  # Добавляем уникальный заголовок в множество

print("\nСписок добавленных заголовков:")
for i, title in enumerate(titles, 1):
    print(f"{i}. {title}")
