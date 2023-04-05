import string
import matplotlib.pyplot as plt
import networkx as nx
import copy
# chain(*iterables) - возвращает по одному элементу из первого итератора, потом из второго, до тех пор, пока итераторы не кончатся.
from itertools import chain 


# Лямбда - функция для подсчета делителей числа:
divs = lambda n: chain(*((d, n // d) for d in range(1, int(n ** 0.5) + 1) if n % d == 0)) 


# Функция для создания матрицы контекста:
def create_matrix(n):
    # Вводим n столбцов n раз:
    matrix = [list(map(int, input().split())) for _ in range(n)]
    return matrix


options = {'font_size': 9}

# Функция для вывода матрицы контекста на экран:
def print_matrix(matrix):
    n = len(matrix)+1
    for i in range(n):
        for j in range(n):
            if i == 0:
                if j == 0:
                    print("\033[4m\033[37m{}\033[0m".format("K|"), end = '_')
                else:
                    print("\033[4m\033[37m{}\033[0m".format(string.ascii_lowercase[j-1]), end = '_')
            else:
                if j == 0:
                    print(i, end = '| ')
                else:
                    print(matrix[i-1][j-1], end = ' ')
        print('')


# Функция для построения отношения порядка (отношения делимости):
def create_relation(n):
    order_relation = list(divs(n))
    order_relation.sort()
    order_relation.pop(0)
    print("Заданное отношение порядка(делимости):\n", order_relation)
    return order_relation


# # Функция для нахождения минимальных элементов заданного отношения:
# def find_min(order_relation):
#     lst = copy.deepcopy(order_relation)
#     for i in lst:
#         for j in order_relation:
#             if i != j and j % i == 0: 
#                 if j in lst:
#                     lst.remove(j)
#     return lst


# Функция для нахождения минимальных (наименьших) и максимальных (наибольших)
# элементов заданного отношения порядка:
def find_min_max(order_relation):
    # Вспомогательные переменные для сравнения и списки для хранения элементов
    max = 0
    min = 0
    max_lst = []
    min_lst = []
    min_max = {}
    # Проходимся по отношению порядка:
    for i in order_relation:
        count_max = 0
        count_min = 0
        # Каждый элемент проверяем на отношение с остальными:
        for j in order_relation:
            if i != j:
                if i % j == 0:  # если отношение найдено, то увеличиваем max
                    count_max+=1
                else:   # иначе увеличиваем min:
                    count_min+=1
        # Если у рассматриваемого элемента отношений больше чем у всех
        # предыдущих, то полностью обновляем массив и переприсваиваем max:
        if count_max > max:
            max = count_max
            max_lst.clear()
            max_lst.append(i)
        # Если у рассматриваемого элемента отношений столько же, сколько и у
        # предыдущего, то добавляем этот элемен в список:
        elif count_max == max:
            max_lst.append(i)
        # Аналогичные действия предпринимаем для минимальных (наименьших)
        # элементов множества:
        if count_min > min:
            min = count_min
            min_lst.clear()
            min_lst.append(i)
        elif count_min == min:
            min_lst.append(i)
    min_max['min'] = min_lst
    min_max['max'] = max_lst
    return min_max


# ФУНКЦИИ ДЛЯ ПОСТРОЕНИЯ ДИАГРАММЫ ХАССЕ ЗАДАННОГО ОТНОШЕНИЯ ПОРЯДКА:

# Функция распределения элементов отношения по уровням:
def hasse_levels(order_relation):   # На вход подается отношение порядка
    lst = copy.deepcopy(order_relation)    # Создается его копия
    result = []    # И список для хранения обнаруженных уровней
    # Пока список не пуст
    while len(lst) != 0:    # Проходимся по нему
        sublist = find_min_max(lst)    # И находим минимальные элементы
        for i in sublist['min']:   # После чего удаляем эти элементы из списка
            if i in lst:
                lst.remove(i)
        result.append(sublist['min'])  # И добавляем их в новый список 
                                # как очередной уровень диаграммы
    return result
        

# Функция для нахождения отношений элементов в диаграмме между собой
def hasse_relations(order_relation):     # На вход подается список уровней
    lst = copy.deepcopy(order_relation)    # Создается его копия
    result = []    # И список для хранения обнаруженных отношений
    i = 1
    while i != len(lst):    # Пока не дошли до конца списка
        for j in lst[i]:    # Проверяем, находится ли в отношении
            for k in lst[i-1]:  # Каждый из элементов рассматриваемого уровня
                if j % k == 0:  # С каждым из элементов на уровень ниже
                    result.append([j,k])    # Добавляем найденные отношения 
                                            # в список отношений как пару
        i+=1
    return result


# Визуализация диаграммы Хассе с помощью библиотек
# matplotlib и networkx:
def create_hasse_diag(nodes, edges, levels):
    hasse = nx.Graph()
    hasse.add_nodes_from(nodes)
    hasse.add_edges_from(edges)
    pos = {}
    n = len(levels)
    max_lenght = 0
    for i in range(n):
        if len(levels[i]) > max_lenght:
            max_lenght = len(levels[i])
    for i in range(n):
        if len(levels[i]) == 1:
            pos[levels[i][0]] = (0, i)
            x = (max_lenght-1)/max_lenght/2
        else:
            j = 0
            if (len(levels[i])) % 2 > 0:
                pos[levels[i][len(levels[i])//2]] = (0, i)
                while j != (len(levels[i])//2):
                    pos[levels[i][j]] = (j-len(levels[i])//2, i)
                    pos[levels[i][-(len(levels[i])//2-j)]] = (j+1, i)
                    j+=1
            else:
                while j != (len(levels[i])//2):
                    pos[levels[i][j]] = (j+0.5-len(levels[i])//2, i)
                    pos[levels[i][-(len(levels[i])//2-j)]] = (j+0.5, i)
                    j+=1
    nx.draw(hasse, pos = pos, node_color = 'w', with_labels = True, font_weight = 'bold', **options)
    plt.show()

#######################################################################

# ФУНКЦИИ ДЛЯ СОЗДАНИЯ КОНЦЕПТА ИЗ ВВЕДЕННОЙ МАТРИЦЫ КОНТЕКСТА:
# Функция получения системы замыканий (далее СЗ) из матрицы контекста:
def get_sets(matrix):
    empty_set = '\u2205' # Пустое множество
    setG = 'G'  # Множество G
    result = [] # Список для СЗ
    set_array = [] # Вспомогательный список
    transposeMatrix = list(zip(*matrix)) # Транспонированная матрица
    n = len(matrix) # Размер матрицы
    for i in range(n): # проходимся по матрице
        for j in range(n):
            if transposeMatrix[i][j] == 1: # если элемент матрицы равен 1
                set_array.append(j + 1) # добавляем в массив множества j + 1
        new_set = set(set_array)
        if new_set not in result:   # Если такого множества еще нет в результирующем
            result.append(new_set)  # Добавляем его в СЗ
        for k in result:    # После чего ищем пересечения данного множества
            if k != new_set:    # С остальными множествами СЗ
                intersection = set(new_set).intersection(k)
                if len(intersection) > 0:   # Результатом будет либо очередное множество
                    if intersection not in result:  # Которое при отсутствии его в СЗ
                        result.append(intersection) # Множестве добавляется в него
                else:
                    if empty_set not in result: # Либо пустое множество, если пересечения нет
                        result.append(empty_set)
        set_array.clear()
    result.append(setG) # Добавляем в СЗ множество G
    return result


# Распределение множеств СЗ по уровням для построения диграммы Хассе
# (аналогично распределению для упорядоченных множеств)
def hasse_levels_for_context(arrayOfSets):
    lst = copy.deepcopy(arrayOfSets)
    result = {}
    index = 1
    empty_set = '\u2205'
    if empty_set in lst:
        result[1] = [empty_set]
        lst.remove('\u2205')
        index+=1
    lst.remove('G')
    while len(lst) > 0:
        level = []
        for i in range(len(lst)):
            fl = True
            for j in range(len(lst)):
                if lst[j].issubset(lst[i]) and i != j:
                    fl = False
                    break
            if fl:
                level.append(lst[i])
        result[index] = level
        for k in level:
            lst.remove(k)
        index+=1
    result[index] = ['G']
    return result      


# Нахождение отнощений между элементами СЗ для 
# построения диаграммы Хассе (аналогично нахождению отношений для
# упорядоченных множеств)
def hasse_relations_for_context(lev_dict):
    relations = []
    a = lev_dict[2]
    for i in a:
        relations.append([i, *lev_dict[1]])
    array = []
    for key in lev_dict:
        array.append(lev_dict[key])
    array.remove(array[0])
    array.remove(array[-1])
    for i in range(len(array)-1):
        for j in array[i+1]:
            for k in array[i]:
                if k.issubset(j):
                    relations.append([j, k])
    b = lev_dict[list(lev_dict.keys())[-2]]
    for i in b:
        relations.append([*lev_dict[list(lev_dict.keys())[-1]], i])
    return relations


def set_to_str(input):
    result = []
    for i in input:
        if isinstance(i, str):
            str_b = ''.join(i)
        else: 
            str_b = ''.join(str(i))
        result.append(str_b)
    return result


def array_of_sets_to_str(input):
    result = []
    for i in input:
        str_b = ''
        a = []
        for j in i:
            if isinstance(j, str):
                str_b = ''.join(j)
            else: 
                str_b = ''.join(str(j))
            a.append(str_b)
        result.append(a)
    return result


def sort_dict(lev_dict):
    for key in lev_dict:
        for i in range(len(lev_dict[key]) - 1):
            if list(lev_dict[key][i])[0] > list(lev_dict[key][i+1])[0]:
                lev_dict[key][i], lev_dict[key][i+1] = lev_dict[key][i+1], lev_dict[key][i]
    return lev_dict


def create_hasse_diag_for_context(input_nodes, input_edges, lev_dict):
    nodes = set_to_str(input_nodes)
    edges = array_of_sets_to_str(input_edges)
    levels = []
    for key in lev_dict:
        levels.append(set_to_str(lev_dict[key]))
    create_hasse_diag(nodes, edges, levels)


# Создание решетки концептов из найденной системы замыканий
# заданного контекста
def concept_create(levels, matrix):
    concept = {}
    char_dict = {}  # Вспомогательный словарь для a b c d
    n = len(matrix)
    for i in range(n):  # Заполнение вспомогательного словаря
        a = set()
        for j in range(n):
            if matrix[i][j]:
                a.add(chr(j+97))    # Код каждой буквы в алфавите - это индекс элемента + 97
        char_dict[i+1] = a
    if levels[1] == ['\u2205']: # Если на первом уровне расположено пустое множество
            concept[1] = ([('\u2205', 'M')])    # Добавляем его в решетку концептов вместе с M
            del levels[1]   # И удаляем из словаря
    for key in levels:  # Проходимся по уровням
        array = []
        if levels[key] == ['G']:    # Если очередной элемент уровня системы замыканий - это множество G,
            array.append(('G', concept[1][0][0]))   # то записываем его в решетку концептов вместе с первым элементом первого уровня
        else:
            for i in levels[key]:   # Проходимся по каждому элементу уровня
                char_set = set()    # вспомогательное множество
                for m in i: 
                    for j in char_dict:
                        if set([j]) == set([m]):    # Если два множества равны между собой
                            if len(char_set) == 0:  # И вспомогательное множество еще пусто
                                char_set = char_dict[j] # То приравниваем его к соотвествующему в вспомогательном словаре
                            else:
                                char_set = char_set.intersection(char_dict[j])  # Иначе приравниваем его к пересечению множеств
                char_list = list(char_set)
                char_list.sort()    # Сортируем вспомогательное множество
                char_set = set(char_list)
                array.append(((i, char_set)))   # И записываем вместе с i-ым элементом в массив множеств текущего уровня
        concept[key] = array    # Заносим массив множеств на текущий уровень
    return concept


# Построение диграммы Хассе для решетки концептов: 
def create_hasse_diag_for_concept(input_nodes, input_edges, input_levels):
    nodes = []
    edges = []
    levels = {}
    # По очереди сортируем и редактируем данные для их подачи
    # в качестве аргументов в основную функцию для построения диаграммы:
    # Вершины:
    for i in input_nodes:
        for key in input_levels:
            for j in input_levels[key]:
                if i == j[0]:
                    nodes.append(j)
    n = 0
    # Ребра:
    for i in input_edges:
        edges.append([])
        for j in i:
            for k in nodes:
                if j == k[0]:
                    edges[n].append(k)
        n+=1
    # Уровни:
    for key in input_levels:
        array = []
        for i in input_levels[key]:
            s = str(i)
            s = s.replace("'",'')   # Перевод данных в строчный вид для визуализации
            array.append(s)
        levels[key] = array
    print(levels, '\n')
    for i in range(len(nodes)):
        s = str(nodes[i])
        s = s.replace("'",'')   # Перевод данных в строчный вид для визуализации
        nodes[i] = str(s)
    print(nodes,'\n')
    for i in range(len(edges)):
        for j in range(len(edges[i])):
            s = str(edges[i][j])
            s = s.replace("'",'')   # Перевод данных в строчный вид для визуализации
            edges[i][j] = s
    print(edges,'\n')
    lev_list = []
    for key in levels:
        lev_list.append(levels[key])
    # Вызов основной функции для построения диаграммы Хассе:
    create_hasse_diag(nodes, edges, lev_list)
    return
    