import csv
import json


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    # Открываем CSV файл для чтения
    with open(INPUT_FILENAME, 'r', encoding='utf-8') as input_f:
        # Используем DictReader для чтения CSV файла
        reader = csv.DictReader(input_f, delimiter=',')

        # Преобразуем данные в список словарей
        data = [row for row in reader]

        # Открываем JSON файл для записи
        with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as output_f:
            # Сериализуем данные в JSON формат с отступами равными 4
            json.dump(data, output_f, ensure_ascii=False, indent=4)

        # Распечатываем JSON строку с отступами равными 4
        print(json.dumps(data, ensure_ascii=False, indent=4))


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
