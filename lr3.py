import copy


# Функция для создания таблицы Кэли:
def create_cayley_table():
    n = int(input("Введите размер таблицы Кэли: "))
    cayleyTable = []
    print("Введите таблицу Кэли: ")
    cayleyTable = [list(map(int, input(f"Строка №{i + 1}: ").split())) for i in range(n)]
    return cayleyTable


# Функция для вывода таблицы Кэли:
def print_cayley_table(cayleyTable):
    n = len(cayleyTable)
    for i in range(n):
        for j in range(n):
            print(cayleyTable[i][j], end=" ")
        print()


# Функция для проверки операции на ассоциативность/неассоциативность:
def check_assocoativity(cayleyTable):
    n = len(cayleyTable)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                if cayleyTable[cayleyTable[i][j]][k] != cayleyTable[i][cayleyTable[j][k]]:
                    print("Операция неассоциативна")
                    return False
    print("Операция ассоциативна")
    return True


# Функция получения подполугруппы:
def find_subsemigroup(cayleTable, X, semigroup):
    result = []
    for i in X:
        result.append(i)
    for i in result:
        index1 = semigroup.index(i)
        for j in result:
            index2 = semigroup.index(j)
            elementToAppend = cayleTable[index1][index2]
            if not(elementToAppend in result):
                result.append(elementToAppend)
    result = set(result)
    return result


# Функция для получения полугруппы бинарных отношений по заданному порождающему множеству X
def get_semigroup(X):
    semigroup = copy.deepcopy(X)  # начальное состояние полугруппы - порождающее множество
    # добавляем новые матрицы, полученные композицией уже имеющихся
    for i in range(len(semigroup)+1):
        for j in range(len(semigroup)):
            matrix = matrix_composition(semigroup[i], semigroup[j])
            if matrix not in semigroup:
                semigroup.append(matrix)
    return semigroup


# Функция для нахождения композиции двух матриц:
def matrix_composition(matrix1, matrix2):
    n = len(matrix1)
    m = len(matrix2[0])
    result = [[0 for j in range(m)] for i in range(n)]
    for i in range(n):
        for j in range(m):
            for k in range(len(matrix2)):
                if matrix1[i][k] and matrix2[k][j]:
                    result[i][j] = 1
                    break
    return result


#################################################################################
def make_semigroup(X):
    semigroup = X.copy()  # начальное состояние полугруппы - порождающее множество
    for i in semigroup:
        for j in semigroup:
            matrix = get_new_matrix(i, j)
            if matrix not in semigroup:
                semigroup.append(matrix)
    return semigroup


def get_new_matrix(matrix1, matrix2):
    n = len(matrix1[0])
    newMatrix = [] # результирующее преобразование
    layerMatrix = [] # строка преобразования
    for i in range(n): # проходимся по элементам строки
        layerMatrix.append(matrix1[0][i]) # добавляем элементы первый строки в layerMatrix
    newMatrix.append(layerMatrix) # добавляем полученную layerMatrix в результирующее преобразование
                                  # в кач-ве первой строки
    layerMatrix = [] # обновляем layerMatrix
    for i in range(n): # проходимся по всем элементам следующей строки первого преобразования
        layerMatrix.append(get_element(matrix1[1][i], matrix2, n)) # добавляем в layerMatrix
                                                               # соответствующий элемент из второго преобразования
    newMatrix.append(layerMatrix) # добавляем полученную layerMatrix в результирующее преобразование
                                  # в кач-ве второй строки
    return newMatrix


def get_element(a, matrix2, n):
    for i in range(n): # проходимся по элементам второго преобразования
        if (matrix2[0][i]) == a: # если элемент из первой строки второго преобразования равен
                                 # элементу из второй строки первого преобразования
            res = matrix2[1][i] # добавляем соответствующий
            return res


def create_gener_sets():
    matrixCount = int(input("Количество преобразований = "))
    matrixSizeN = 2
    matrixSizeM = (int(input("Количество элементов множества = ")))
    matrix = []
    for i in range(0, matrixCount):
        print("Преобразование №", i + 1, ":")
        mat = []
        a = []
        for i in range(matrixSizeN):
            if i == 0:
                for j in range(matrixSizeM):
                    a.append(j+1)
                mat.append(a)
            else:
                print(*a)
                a = []
                input_string = input()
                numbers = [int(num) for num in input_string.split()]
                for k in numbers:
                    a.append(k)
                mat.append(a)
                a = []
        matrix.append(mat)
    return matrix


def print_gener_sets(matrix):
    num = 1
    for mat in matrix:
        print("Преобразование №", num)
        for i in mat:
            print(*i, sep=' ')
        print()
        num += 1