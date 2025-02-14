# TODO Найдите количество книг, которое можно разместить на дискете

# Переводим объем дискеты в байты
disk_capacity_mb = 1.44
bytes_per_mb = 2 ** 20  # 1 Мб = 2^20 байт
disk_capacity_bytes = disk_capacity_mb * bytes_per_mb

# Параметры книги
pages_per_book = 100
lines_per_page = 50
chars_per_line = 25
bytes_per_char = 4

# Рассчитываем объем одной книги в байтах
book_size_bytes = pages_per_book * lines_per_page * chars_per_line * bytes_per_char

# Рассчитываем количество книг, которые можно поместить на дискете
number_of_books = disk_capacity_bytes // book_size_bytes

# Выводим результат
print(f"Количество книг, помещающихся на дискету: {int(number_of_books)}")