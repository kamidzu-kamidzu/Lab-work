def find_common_participants(group1, group2, separator=','):
    # Преобразуем строки в списки участников, используя указанный разделитель
    participants_first_group = group1.split(separator)
    participants_second_group = group2.split(separator)

    # Находим общих участников с помощью пересечения множеств
    common_participants = set(participants_first_group).intersection(set(participants_second_group))

    # Возвращаем отсортированный список общих участников
    return sorted(common_participants)


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# Проверяем работу функции с разделителем отличным от запятой (в данном случае '|')
common_participants = find_common_participants(participants_first_group, participants_second_group, '|')

# Выводим результат
print("Общие участники:", common_participants)
