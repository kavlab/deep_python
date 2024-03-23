def calculate(N, M, weights):
    # Список dp для хранения минимального
    # количества предметов для каждого возможного веса
    dp = [float('inf')] * (M + 1)
    # Нулевой вес можно получить без предметов
    dp[0] = 0

    # Цикл по предметам
    for weight in weights:
        # Обновление значений в списке dp
        for w in range(M, weight - 1, -1):
            # Заполнение минимальным количеством
            dp[w] = min(
                # Текущее количество предметов
                dp[w],
                # Количество предметов из текущего минус текущий вес
                dp[w - weight] + 1
            )

    if dp[M] == float('inf'):
        # Если в dp[M] осталось значение бесконечность,
        # то результат не достижим
        return 0
    else:
        # Минимальное количество предметов будет в dp[M]
        return dp[M]


def test():
    print(calculate(5, 100, [80, 50, 30, 10, 30]))
    print(calculate(5, 100, [10, 50, 30, 20, 40]))
    print(calculate(7, 100, [30, 50, 10, 30, 30, 15, 10]))
    print(calculate(7, 100, [80, 50, 20, 30, 20, 15, 10]))


# Функция для быстрого тестирования алгоритма
# test()

# Чтение входных данных
N, M = [int(x) for x in input().split()]
weights = [int(x) for x in input().split()]

# Вызов функции и вывод результата
print(calculate(N, M, weights))
