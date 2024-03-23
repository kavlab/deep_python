def calculate(N, M):
    # Матрица dp размером NxM, где dp[i][j] будет
    # содержать количество способов добраться до клетки (i, j)
    dp = [[0 for _ in range(M)] for _ in range(N)]

    # Начальная позиция коня в левом верхнем углу
    dp[0][0] = 1

    # Заполнение матрицы dp
    for i in range(N):
        for j in range(M):
            # Увеличение количества на доступных коню клетках
            if i + 2 < N and j + 1 < M:
                # Два шага вниз и один вправо
                dp[i + 2][j + 1] += dp[i][j]
            if i + 1 < N and j + 2 < M:
                # Два шага вправо и один вниз
                dp[i + 1][j + 2] += dp[i][j]

    # Результат в последней клетке
    return dp[N-1][M-1]


def test():
    print(calculate(2, 2))
    print(calculate(3, 3))
    print(calculate(4, 4))
    print(calculate(5, 6))


# Функция для быстрого тестирования алгоритма
# test()

# Чтение входных данных
N, M = [int(x) for x in input().split()]

# Вызов функции и вывод результата
print(calculate(N, M))
