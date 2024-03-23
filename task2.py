def calculate(weights):
    total_sum = sum(weights)
    if total_sum % 2 != 0:
        # Если сумма весов нечетная, то их
        # нельзя разложить на две чаши весов,
        # чтобы они оказались в равновесии
        return False

    # Сумма на одной чаше, половина общей
    half_sum = total_sum // 2

    # Список dp размером half_sum + 1 для фиксации
    # достигнутой массы
    dp = [False] * (half_sum + 1)
    # Первый элемент установлен в True, т.к. может
    # получиться, что масса будет равна нулю
    dp[0] = True

    # Цикл по гирям
    for w in weights:
        # Обновление значения для возможных сумм весов
        for i in range(half_sum, w - 1, -1):
            dp[i] = dp[i] or dp[i - w]

    # В последнем элементе будет True, если есть
    # возможность разложить гири в равновесии
    return dp[half_sum]


def test():
    print(calculate([8, 4, 5, 3, 1]))
    print(calculate([8, 4, 5, 4, 11]))


# Функция для быстрого тестирования алгоритма
# test()

# Чтение входных данных
N = int(input())
weights = [int(x) for x in input().split()]

# Вызов функции и вывод результата
print(calculate(weights))
