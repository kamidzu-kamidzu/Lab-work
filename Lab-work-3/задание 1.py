# Функция для поиска индекса первого вхождения товара в списке
def find_index_of_item(items_list, find_item):
    try:
        # Используем метод index для поиска индекса первого вхождения
        return items_list.index(find_item)
    except ValueError:
        # Если элемент не найден, возвращаем None
        return None


items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = find_index_of_item(items_list, find_item)
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
