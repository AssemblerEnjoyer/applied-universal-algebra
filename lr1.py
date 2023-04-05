import copy
import numpy as np


# Функция для вывода матрицы бинарного отношения:
def print_matrix(matrix):
    # Проходимся по каждой строке матрицы
    for i in matrix:
        # и выводим её:
        print(*i, sep=" ")
    return matrix


# Функция для создания матрицы бинарного отношения размерности n x n:
def create_matrix(n):
    # Вводим n столбцов n раз:
    matrix = [list(map(int, input().split())) for _ in range(n)]
    print("Матрица бинарного отношения размерности ", len(matrix), " x ", len(matrix), ":")
    return matrix


# Функция для проверки бинарного отношения на рефлексивность:
def reflex_check(matrix):
    # Проходимся по главной диагонали матрицы
    for i in range(len(matrix)):
        # Если на главной диагонали все элементы единичные, то отношение рефлексивно, иначе отношение не рефлексивно
        if matrix[i][i] != 1:
            return
    print("Рефлексивно")


# Функция для проверки бинарного отношения на антирефлексивность:
def antireflex_check(matrix):
    # Проходимся по главной диагонали матрицы:
    for i in range(len(matrix)):
        # Если на главной диагонали все элементы единичные, то отношение антирефлексивно:
        if matrix[i][i] != 1:
            return
    print("Антирефлексивно")


# Функция для проверки бинарного отношения на симметричность:
def symmetry_check(matrix):
    # Проходимся по каждому элементу матрицы:
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            # Бинарное отношение симметрично т. и т. т., к. каждый элемент его матрицы с индексами [i, j] равен
            # элементу с индексами [j, i]:
            if matrix[i][j] != matrix[j][i]:
                return
    print("Симметрично")


# Функция для проверки бинарного отношения на антисимметричность:
def antisimmetry_check(matrix):
    tmatrix = copy.deepcopy(matrix)
    rmatrix = copy.deepcopy(matrix)
    # Транспонирование матрицы (zip() используется для объединения столбцов в строки matrix,
    # а list() для преобразования результата в список. Это дает транспонированную матрицу):
    tmatrix = list(zip(*matrix))
    # Получаем результирующую матрицу поэлементным умножением исходной матрицы на транспонированную:
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            rmatrix[i][j] = matrix[i][j]*tmatrix[i][j]
            # Если хотя бы один из элементов вне главной диагонали не равен нулю, то матрица не является
            # Антисимметричной
            if rmatrix[i][j] != 0 and i != j:
                return
    print("Антисимметрично")


# Функция для проверки бинарного отношения на транзитивность:
def tranzit_check(matrix):
    # Условие выполнение бинарного отношения: Если две вершины связаны через посредника,
    # то они также будут связаны и напрямую.
    # Проходимся по каждому элементу матрицы:
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            # Если элементы с индексами [i, j] и [j, k] связаны между собой и связаны через элемент [i, k],
            if matrix[i][j]:
                for k in range(len(matrix)):
                    if matrix[j][k] and not matrix[i][k]:
                        return
    # то бинарное отношение транзитивно, иначе отношение не транзитивно.
    print("Транзитивно")


# Функция для построения рефлексивного замыкания бинарного отношения:
def reflex_closure(matrix):
    # Проходимся по главной диагонали матрицы:
    for i in range(len(matrix)):
        # Если элемент главной диагонали нулевой,
        if not matrix[i][i]:
            # то делаем его единичным:
            matrix[i][i] = 1
    return matrix


# Функция для построения симметричного замыкания бинарного отношения:
def symmetry_closure(matrix):
    # Проходимся по каждому элементу матрицы:
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            # Если элемент матрицы с индексами [i, j] равен 1, а элемент матрицы с индексами [i, j] равен 0,
            if matrix[i][j] and not matrix[j][i]:
                # то приравниваем элемент с индексами [i, j] к 1:
                matrix[j][i] = 1
    return matrix


# Функция для логического умножения матриц:
def logical_multiply(matrix1, matrix2):
    result = [[0 for j in range(len(matrix2[0]))] for i in range(len(matrix1))]
    for i in range(len(matrix1)):
        for j in range(len(matrix1)):
            for k in range(len(matrix1)):
                result[i][j] += matrix1[i][k] & matrix2[k][j]
    return result


# Функция для логического сложения матриц:
def logical_sum(matrix1, matrix2):
    result = [[matrix1[i][j] or matrix2[i][j] for j in range(len(matrix1))] for i in range(len(matrix1))]
    return result


# Функция для построения транзитивного замыкания бинарного отношения:
def tranzit_closure(matrix):
    result = copy.deepcopy(matrix)
    degree = copy.deepcopy(matrix)
    for i in range(len(matrix)):
        # Очередное возведение матрицы в степень:
        degree = logical_multiply(matrix, degree)
        # И сложение с результирующей матрицей:
        result = logical_sum(result, degree)
    return result


# Функция для построения эквивалентного замыкания бинарного отношения:
def closure(matrix):
    # Последовательно применяем к изначальной матрице каждое из замыканий:
    matrix = reflex_closure(matrix)
    matrix = symmetry_closure(matrix)
    matrix = tranzit_closure(matrix)
    return matrix


# Функция для построения фактор-множества:
def factor_set(matrix):
    result = copy.deepcopy(matrix)
    result = closure(result)
    # Создание массива индексов, результирующего массива, массива для проверки посещения столбца:
    ind = []
    res = []
    check_arr = []
    buffer = [list(col) for col in zip(*result)]
    for i in range(len(matrix)):
        # Изначально все столбцы являются непосещенными:
        check_arr.append(0)
    for i in range(len(matrix)):
        if check_arr[i] == 0:
            a = buffer[i]
            # Сравнение со всеми остальными столбцами на равенство:
            for j in range(i + 1, len(matrix)):
                b = buffer[j]
                # Если два столбца одинаковы, то записываем в массив индексов j-ый столбец:
                if np.array_equal(a, b):
                    ind.append(j)
                    # Отмечаем его посещенным:
                    check_arr[j] = 1
            # Записываем в массив индексов i-ый столбец:
            ind.append(i)
            # Записываем массив индексов равных столбцов в результирующий массив:
            res.append(set(ind))
            # Обнуляем массив индексов и отмечаем i-ый столбец за посещенный:
            ind = []
            check_arr[i] = 1
    return res


# Функция для построения системы представителей фактор-множества:
def system(matrix):
    matrix_copy = copy.deepcopy(matrix)
    result = []
    for i in range(len(matrix_copy)):
        result.append(matrix_copy[i].pop())
    return result
