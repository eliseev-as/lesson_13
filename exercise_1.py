import random

m = int(input("Введите количество строк матрицы: "))
n = int(input("Введите количество столбцов матрицы: "))

matrix_1 = [[random.randint(-100, 100) for _ in range(n)] for _ in range(m)]
print("Матрица 1:")
for i in matrix_1:
    print(i)

matrix_2 = [[random.randint(-100, 100) for _ in range(n)] for _ in range(m)]
print("Матрица 2:")
for i in matrix_2:
    print(i)

matrix_3 = [[matrix_1[i][j] + matrix_2[i][j] for j in range(len(matrix_1[0]))] for i in range(len(matrix_1))]
print("Матрица 3:")
for i in matrix_3:
    print(i)
