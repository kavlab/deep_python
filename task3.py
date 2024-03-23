def calculate(N, denominations, amount):
    # Списки для хранения количества банкнот
    # и информации о предыдущем элементе для формирования ответа
    banknotes = [float('inf')] * (amount + 1)
    prev = [-1] * (amount + 1)

    # Нулевая сумма выдается без банкнот
    banknotes[0] = 0

    # Цикл по всем значениям до заданной суммы
    for i in range(1, amount + 1):
        # Цикл по банкнотам
        for j in range(N):
            # Вычисление минимального количества банкнот для набора
            # текущей суммы
            if (i >= denominations[j]
                    and banknotes[i - denominations[j]] + 1 < banknotes[i]):
                # Обновление количества банкнот
                banknotes[i] = banknotes[i - denominations[j]] + 1
                # Сохранение использованного номинала
                prev[i] = denominations[j]

    if banknotes[amount] == float('inf'):
        # Заданную сумму нельзя набрать доступными банкнотами
        return "No solution"
    else:
        # Формирование ответа по сохраненному списку банкнот
        result = []
        while amount > 0:
            result.append(prev[amount])
            amount -= prev[amount]

        return " ".join(map(str, result))


def test():
    print(calculate(6, [50, 100, 200, 500, 1000, 5000], 1750))
    print(calculate(5, [100, 200, 500, 1000, 5000], 1750))


# Функция для быстрого тестирования алгоритма
# test()

# Чтение входных данных
N = int(input())
denominations = [int(x) for x in input().split()]
amount = int(input())

# Вызов функции и вывод результата
print(calculate(N, denominations, amount))
