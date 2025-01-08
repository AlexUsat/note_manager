note_list = []
titles = []

temp_list = input("Введите имя пользователя: ")
note_list.append(temp_list)

temp_title = input("Введите заголовок №1 заметки: ")
titles.append(temp_title)
temp_title = input("Введите заголовок №2 заметки: ")
titles.append(temp_title)
temp_title = input("Введите заголовок №3 заметки: ")
titles.append(temp_title)
note_list.append(titles)

temp_list = input("Введите описание заметки: ")
note_list.append(temp_list)

temp_list = input("Введите статус заметки (например, 'Активна', 'Выполнена'): ")
note_list.append(temp_list)

temp_list = input("Введите дату создания заметки в формате 'дд.мм.гггг': ")
note_list.append(temp_list)

temp_list = input("Введите дату истечения заметки в формате 'дд.мм.гггг': ")
note_list.append(temp_list)

print("\nВы ввели следующие данные:")
print("Имя пользователя:", note_list[0])
print("Заголовки заметки:", note_list[1])
print("Описание заметки:", note_list[2])
print("Статус заметки:", note_list[3])
print("Дата создания заметки:", note_list[4])
print("Дата истечения заметки:", note_list[5])