# Исходный список
numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# Шаг 1: Найти индекс пропущенного элемента
missing_index = numbers.index(None)

# Шаг 2: Рассчитать сумму всех чисел, исключая None
total_sum = sum(x for x in numbers if x is not None)

# Шаг 3: Вычислить количество всех элементов (включая None)
count = len(numbers)

# Шаг 4: Рассчитать среднее арифметическое
average = total_sum / count

# Шаг 5: Заменить None на среднее арифметическое
numbers[missing_index] = average

# Вывод результата
print("Измененный список:", numbers)