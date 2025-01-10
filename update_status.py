valid_statuses = ["Выполнена", "Активна", "Отложена"]  # Возможные статусы заметки
current_status = valid_statuses[1]
print(f"Текущий статус заметки: {current_status}")

while True:
    print("\nВыберите новый статус заметки из предложенных:")
    for i, status in enumerate(valid_statuses, 1):
        print(f"{i}. {status}")

    new_status = input("Введите новый статус: ").strip()

    if new_status in valid_statuses:  # Проверяем корректность ввода
        current_status = new_status  # Обновляем текущий статус
        print("Статус успешно обновлён")
        break
    else:
        print("Некорректный ввод. Попробуйте снова")
print(f"\nОбновлённый статус заметки: {current_status}")

