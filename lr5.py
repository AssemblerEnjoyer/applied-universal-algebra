import string

# Функция получения идеалов
def getIdeals(caleyTable, semigroup):
    ideals = {} # идеалы полугруппы
    for i in range(len(semigroup)): # проходимся по полученной полугруппе
        setFirst = set(caleyTable[i]) # получаем i-ый эл-т из таблицы Кэли
        newSet = []
        for row in caleyTable:
            newSet.append(row[i])
        setSecond = set(newSet)
        rIdeal, lIdeal, dIdeal = setFirst, setSecond, setFirst.union(setSecond)
        ideals[semigroup[i]] = rIdeal, lIdeal, dIdeal
        print(f"Подполугруппа <{semigroup[i]}>. Правый идеал: ", *rIdeal,
              f"\nПодполугруппа <{semigroup[i]}>. Левый идеал: ", *lIdeal,
              f"\nПодполугруппа <{semigroup[i]}>. Двусторонний идеал: ", *dIdeal)

# функция получения правого отношения Грина
def getGrinRelation(matrix, array):
    relation = []
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            if set(matrix[i]) == set(matrix[j]):
                pair = (array[i], array[j])
                relation.append(pair)
                if i != j:
                    pair = (array[j], array[i])
                    relation.append(pair)
    return relation

# функция получения классов эквивалентности
def getClass(array):
    result = []
    subresult = []
    for pair in array:
        for otherPair in array:
            if pair[0] == otherPair[0]:
                subresult.append(pair[1])
                subresult.append(otherPair[1])
        if set(subresult) not in result:
            result.append(set(subresult))
        subresult = []
    return result

# функция получения egg-box-картины
def getEggBox(array):
    for mySet in array:
        res = ' ' + ' | '.join(item for item in mySet) + ' '
        print("\033[4m\033[37m{}\033[0m".format(res))