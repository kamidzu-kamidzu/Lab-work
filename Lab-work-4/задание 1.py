import json

# Функция для выполнения задачи
def task() -> float:
    # Пример данных в формате JSON, которые дают результат 2.296
    data = '''
    [
  {
    "score": 0.0009456152645028281,
    "weight": 1
  },
  {
    "score": 0.00020640167757499364,
    "weight": 1
  },
  {
    "score": 0,
    "weight": 1
  },
  {
    "score": 1.6557065217391307,
    "weight": 1
  },
  {
    "score": 0,
    "weight": 1
  },
  {
    "score": 0.6066065217391303,
    "weight": 1
  },
  {
    "score": 0.03126181644071977,
    "weight": 1
  },
  {
    "score": 0.001253973281817707,
    "weight": 1
  }
]
'''

# Парсим JSON строку в список словарей
    items = json.loads(data)

    # Инициализируем переменную для хранения суммы произведений
    total_sum = 0.0
    
    # Проходим по каждому элементу списка
    for item in items:
        # Умножаем значения по ключам "score" и "weight"
        product = item['score'] * item['weight']
        # Добавляем результат к общей сумме
        total_sum += product
    
    # Округляем результат до трех знаков после запятой
    return round(total_sum, 3)


print(task())
