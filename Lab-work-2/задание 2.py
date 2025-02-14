salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен


# Функция для расчета необходимой подушки безопасности
def calculate_money_capital(salary, spend, months, increase):
    # Начальное значение подушки безопасности
    money_capital = 0

    # Расчет необходимой подушки безопасности
    current_spend = spend
    for _ in range(months):
        if salary < current_spend:
            money_capital += (current_spend - salary)
        current_spend *= (1 + increase)

    return round(money_capital)


# Рассчитываем подушку безопасности
money_capital = calculate_money_capital(salary, spend, months, increase)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)
