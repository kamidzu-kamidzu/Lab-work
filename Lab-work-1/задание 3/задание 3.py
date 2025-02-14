list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# Разделяем список на две команды с использованием слайсирования
middle_index = len(list_players) // 2

first_team = list_players[:middle_index]
second_team = list_players[middle_index:]

# Выводим каждую команду участников на отдельной строке
print(first_team)
print(second_team)