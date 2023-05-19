import copy
import string
import sys
import matplotlib.pyplot as plt
import networkx as nx

# def hasse_levels_for_context(arrayOfSets):
#     lst = copy.deepcopy(arrayOfSets)
#     result = {}
#     result[1] = [lst[-1]]
#     lst.remove({'empty'})
#     lst.remove({'G'})
#     index = 2
#     while len(lst) > 0:
#         level = []
#         for i in range(len(lst)):
#             fl = True
#             for j in range(len(lst)):
#                 if lst[j].issubset(lst[i]) and i != j:
#                     fl = False
#                     break
#             if fl:
#                 level.append(lst[i])
#         result[index] = level
#         for k in level:
#             lst.remove(k)
#         index+=1
#     result[index] = [{'G'}]
#     return result

# def hasse (arrayOfSets):
#     lst = copy.deepcopy(arrayOfSets)
#     result = {}
#     result[0] = [lst[-1]]
#     lst.remove({'empty'})
#     lst.remove({'G'})

# a = [{1, 2}, {2, 3, 4}, {1}, {3, 4}, {'G'}, {'empty'}]
# print(hasse_levels_for_context(a))
# matrix = [[1,2,3],[1,2,3],[1,2,3]]
# transposeMatrix = list(zip(*matrix))
# print(*transposeMatrix)

# def get_sets(matrix):
#     empty_set = {'empty'}
#     setG = {'G'}
#     arrayOfSets = [] # массив множеств
#     array = [] # массив множества
#     predArray = []
#     transposeMatrix = list(zip(*matrix)) # транспонируем матрицу
#     n = len(matrix)
#     for i in range(n): # проходимся по матрице
#         for j in range(n):
#             if transposeMatrix[i][j] == 1: # если элемент матрицы равен 1
#                 array.append(j + 1) # добавляем в массив множества j + 1
#         arrayOfSets.append(set(array)) # добавляем в массив множеств текущий массив множества
#         intersection = set(array).intersection(set(predArray))
#         if len(intersection) > 0:
#             arrayOfSets.append(set(intersection))
#         predArray = copy.deepcopy(array)
#         array = [] # обновляем массив множества
#     arrayOfSets.append(setG)
#     arrayOfSets.append(empty_set)
#     return arrayOfSets


# matrix = [[1, 0, 1, 0],[1, 1, 0, 0],[0, 1, 0, 1],[0, 1, 0, 1]]
# print(get_sets(matrix))

# def hasse_relations_for_context(lev_dict):
#     relations = []
#     a = lev_dict[2]
#     for i in a:
#         relations.append([i, *lev_dict[1]])
#     array = []
#     for key in lev_dict:
#         array.append(lev_dict[key])
#     array.remove(array[0])
#     array.remove(array[-1])
#     for i in range(len(array)-1):
#         for j in array[i+1]:
#             for k in array[i]:
#                 if k.issubset(j):
#                     relations.append([j, k])
#     b = lev_dict[list(lev_dict.keys())[-2]]
#     for i in b:
#         relations.append([*lev_dict[list(lev_dict.keys())[-1]], i])
#     return relations

# d={1 :  [{'empty'}], 2 : [{2}, {1}, {3, 4}], 3 : [{1, 2}, {2, 3, 4}], 4 : [{'G'}]}

# print(hasse_relations_for_context(d))

# def set_to_str(a):
#     b = []
#     for i in a:
#         str_b = ''.join(str(i))
#         b.append(str_b)
#     return b

# a = [{1, 2}, {2, 3, 4}, {2}, {1}, {3, 4}, {'G'}, {'empty'}]

# print(set_to_str(a))

# def set_to_str(input):
#     result = []
#     for i in input:
#         str_b = ''.join(str(i))
#         result.append(str_b)
#     return result

# def array_of_sets_to_str(input):
#     result = []
#     for i in input:
#         str_b = ''
#         a = []
#         for j in i:
#             str_b = str(j)
#             a.append(str_b)
#         result.append(a)
#     return result


# def create_hasse_diag_for_context(input_nodes, input_edges):
#     hasse = nx.Graph()
#     nodes = set_to_str(input_nodes)
#     edges = array_of_sets_to_str(input_edges)
#     hasse.add_nodes_from(nodes)
#     hasse.add_edges_from(edges)
#     nx.draw(hasse, node_color = 'w',with_labels = True, font_weight = 'bold')
#     plt.show()

# a = [[{2}, {'empty'}], [{1}, {'empty'}], [{3, 4}, {'empty'}], [{1, 2}, {2}], [{1, 2}, {1}], [{2, 3, 4}, {2}], [{2, 3, 4}, {3, 4}], [{'G'}, {1, 2}], [{'G'}, {2, 3, 4}]]
# print(array_of_sets_to_str(a))
# b = [{1, 2}, {2, 3, 4}, {2}, {1}, {3, 4}, {'G'}, {'empty'}]

# create_hasse_diag_for_context(b,a)

# def sort_dict(lev_dict):
#     for key in lev_dict:
#         for i in range(len(lev_dict[key])-1):
#             if list(lev_dict[key][i])[0] > list(lev_dict[key][i+1])[0]:
#                 lev_dict[key][i], lev_dict[key][i+1] = lev_dict[key][i+1], lev_dict[key][i]
#     return lev_dict

# d={1 :  [{'empty'}], 2 : [{2}, {1}, {3, 4}], 3 : [{1, 2}, {2, 3, 4}], 4 : [{'G'}]}
# print(sort_dict(d))

# def get_sets(matrix):
#     empty_set = 'empty'
#     setG = 'G'
#     arrayOfSets = [] # массив множеств
#     array = [] # массив множества
#     predArray = []
#     transposeMatrix = list(zip(*matrix)) # транспонируем матрицу
#     n = len(matrix)
#     for i in range(n): # проходимся по матрице
#         for j in range(n):
#             if transposeMatrix[i][j] == 1: # если элемент матрицы равен 1
#                 array.append(j + 1) # добавляем в массив множества j + 1
#         arrayOfSets.append(set(array)) # добавляем в массив множеств текущий массив множества
#         intersection = set(array).intersection(set(predArray))
#         if len(intersection) > 0:
#             arrayOfSets.append(set(intersection))
#         predArray = copy.deepcopy(array)
#         array = [] # обновляем массив множества
#     arrayOfSets.append(setG)
#     arrayOfSets.append(empty_set)
#     return arrayOfSets


# def hasse_levels_for_context(arrayOfSets):
#     lst = copy.deepcopy(arrayOfSets)
#     result = {}
#     result[1] = [lst[-1]]
#     lst.remove('empty')
#     lst.remove('G')
#     index = 2
#     while len(lst) > 0:
#         level = []
#         for i in range(len(lst)):
#             fl = True
#             for j in range(len(lst)):
#                 if lst[j].issubset(lst[i]) and i != j:
#                     fl = False
#                     break
#             if fl:
#                 level.append(lst[i])
#         result[index] = level
#         for k in level:
#             lst.remove(k)
#         index+=1
#     result[index] = ['G']
#     return result        


# def hasse_relations_for_context(lev_dict):
#     relations = []
#     a = lev_dict[2]
#     for i in a:
#         relations.append([i, *lev_dict[1]])
#     array = []
#     for key in lev_dict:
#         array.append(lev_dict[key])
#     array.remove(array[0])
#     array.remove(array[-1])
#     for i in range(len(array)-1):
#         for j in array[i+1]:
#             for k in array[i]:
#                 if k.issubset(j):
#                     relations.append([j, k])
#     b = lev_dict[list(lev_dict.keys())[-2]]
#     for i in b:
#         relations.append([*lev_dict[list(lev_dict.keys())[-1]], i])
#     return relations


# def set_to_str(input):
#     result = []
#     for i in input:
#         if isinstance(i, str):
#             str_b = ''.join(i)
#         else: 
#             str_b = ''.join(str(i))
#         result.append(str_b)
#     return result


# def array_of_sets_to_str(input):
#     result = []
#     for i in input:
#         str_b = ''
#         a = []
#         for j in i:
#             if isinstance(j, str):
#                 str_b = ''.join(j)
#             else: 
#                 str_b = ''.join(str(j))
#             a.append(str_b)
#         result.append(a)
#     return result


# def sort_dict(lev_dict):
#     for key in lev_dict:
#         for i in range(len(lev_dict[key]) - 1):
#             if list(lev_dict[key][i])[0] > list(lev_dict[key][i+1])[0]:
#                 lev_dict[key][i], lev_dict[key][i+1] = lev_dict[key][i+1], lev_dict[key][i]
#     return lev_dict


# def create_hasse_diag_for_context(input_nodes, input_edges, lev_dict):
#     nodes = set_to_str(input_nodes)
#     edges = array_of_sets_to_str(input_edges)
#     levels = []
#     for key in lev_dict:
#         levels.append(set_to_str(lev_dict[key]))
#     print(levels)
#     print(nodes)
#     print(*edges)


# ContextMatrix = [[1,0,1,0],[1,1,0,0],[0,1,0,1],[0,1,0,1]]
# closure_system = get_sets(ContextMatrix)
# print(closure_system)
# levels = hasse_levels_for_context(closure_system)
# print(levels)
# relarions = hasse_relations_for_context(levels)
# print(relarions)
# sort_dict(levels)
# relations = hasse_relations_for_context(levels)
# print("\n\nОтношения диаграммы Хассе для заданной матрицы контекста:", *relations)
# create_hasse_diag_for_context(closure_system, relations, levels)

# print("\u2205")

# def get_sets(matrix):
#     empty_set = '\u2205'
#     setG = 'G'
#     arrayOfSets = [] # массив множеств
#     array = [] # массив множества
#     predArray = []
#     transposeMatrix = list(zip(*matrix)) # транспонируем матрицу
#     n = len(matrix)
#     for i in range(n): # проходимся по матрице
#         for j in range(n):
#             if transposeMatrix[i][j] == 1: # если элемент матрицы равен 1
#                 array.append(j + 1) # добавляем в массив множества j + 1
#         arrayOfSets.append(set(array)) # добавляем в массив множеств текущий массив множества
#         intersection = set(array).intersection(set(predArray))
#         if len(intersection) > 0:
#             arrayOfSets.append(set(intersection))
#         predArray = copy.deepcopy(array)
#         array = [] # обновляем массив множества
#     arrayOfSets.append(setG)
#     arrayOfSets.append(empty_set)
#     return arrayOfSets

# def get_sets(matrix):
#     empty_set = '\u2205'
#     setG = 'G'
#     result = []
#     set_array = []
#     transposeMatrix = list(zip(*matrix))
#     n = len(matrix)
#     for i in range(n): # проходимся по матрице
#         for j in range(n):
#             if transposeMatrix[i][j] == 1: # если элемент матрицы равен 1
#                 set_array.append(j + 1) # добавляем в массив множества j + 1
#         new_set = set(set_array)
#         if new_set not in result:
#             result.append(new_set)
#         for k in result:
#             if k != new_set:
#                 intersection = set(new_set).intersection(k)
#                 if len(intersection) > 0:
#                     if intersection not in result:
#                         result.append(intersection)
#                 else:
#                     if empty_set not in result:
#                         result.append(empty_set)
#         set_array.clear()
#     result.append(setG)
#     return result

# def hasse_levels_for_context(arrayOfSets):
#     lst = copy.deepcopy(arrayOfSets)
#     result = {}
#     index = 1
#     empty_set = '\u2205'
#     if empty_set in lst:
#         result[1] = [empty_set]
#         lst.remove('\u2205')
#         index+=1
#     lst.remove('G')
#     while len(lst) > 0:
#         level = []
#         for i in range(len(lst)):
#             fl = True
#             for j in range(len(lst)):
#                 if lst[j].issubset(lst[i]) and i != j:
#                     fl = False
#                     break
#             if fl:
#                 level.append(lst[i])
#         result[index] = level
#         for k in level:
#             lst.remove(k)
#         index+=1
#     result[index] = ['G']
#     return result 

# # ContextMatrix1 = [[1,0,1,0],[1,1,0,0],[0,1,0,1],[0,1,0,1]]
# # closure_system1 = get_sets(ContextMatrix1)
# # print(closure_system1,'\n\n')
# # ContextMatrix2 = [[0,0,1,1],[1,1,0,0],[0,0,1,0],[1,1,1,1]]
# # closure_system2 = get_sets(ContextMatrix2)
# # print(closure_system2,'\n\n')
# # print(hasse_levels_for_context(closure_system1))
# # print(hasse_levels_for_context(closure_system2))

# # 1 0 1 0
# # 1 1 0 0
# # 0 1 0 1
# # 0 1 0 1

# def concept_create(levels, matrix):
#     concept = {}
#     char_dict = {}
#     n = len(matrix)
#     for i in range(n):
#         a = set()
#         for j in range(n):
#             if matrix[i][j]:
#                 a.add(chr(j+97))
#         char_dict[i+1] = a
#     print(char_dict)
#     if levels[1] == ['\u2205']:
#             concept[1] = (('\u2205', 'M'))
#             del levels[1]
#     for key in levels:
#         array = []
#         if levels[key] == ['G']:
#             array.append(('G', '\u2205'))
#         else:
#             for i in levels[key]:
#                 char_set = set()
#                 for m in i:
#                     for j in char_dict:
#                         if set([j]) == set([m]):
#                             if len(char_set) == 0:
#                                 char_set = char_dict[j]
#                             else:
#                                 char_set = char_set.intersection(char_dict[j])
#                 char_list = list(char_set)
#                 char_list.sort()
#                 char_set = set(char_list)
#                 array.append(((i, char_set)))
#         concept[key] = array
#     return concept
            


# ContextMatrix1 = [[1,0,1,0],[1,1,0,0],[0,1,0,1],[0,1,0,1]]
# closure_system1 = get_sets(ContextMatrix1)
# print(closure_system1,'\n\n')
# levels = hasse_levels_for_context(closure_system1)
# print(levels,'\n\n')
# concept_create(levels, ContextMatrix1)

""" str1 = str(({1}, {'a', 'c'}))
print(str1)
str1 = str1.replace("'",'')
print(str1) """


""" def smallest_divisors(arr):
    def find_minimal_divisor(n):
        for i in arr:
            if n % i == 0:
                return i
        return n
    res = []
    for n in arr:
        res.append(find_minimal_divisor(n))
    result = list(set(res))
    return result


# функция возвращающая количество делителей числа n
def count_divisors(n, arr):
    count = 0 # количество делителей
    for i in arr:
        if n % i == 0: # если число делится на i
            count += 1 # увеличиваем число делителей
    return count


def min_divisors(arr):
    min_num_divisors = sys.maxsize # минимальное число делителей
    min_num_divisors_elem = [] # массив чисел с минимальным число делителей
    for elem in arr: # проходимся по всем числам в массиве
        num_divisors = count_divisors(elem, arr) # количество делителей текущего числа
        if num_divisors <= min_num_divisors: # если кол-во делителей числа <= минимального числа делителей
            min_num_divisors = num_divisors # обновляем минимальное кол-во делителей
            min_num_divisors_elem.append(elem) # добавляем элемент в массив чисел с минимальными делителями
    return min_num_divisors_elem


def max_divisors(arr):
    max_num_divisors = 0 # максимальное число делителей
    max_num_divisors_elem = [] # массив с максимальным числом делителей
    for elem in arr: # проходимся по всем числам в массиве
        num_divisors = count_divisors(elem, arr) # ищем кол-во делителей текущего числа
        if num_divisors > max_num_divisors: # если число делителей больше максимального числа делителей
            max_num_divisors = num_divisors # обновляем максимальное кол-во делителей
            if len(max_num_divisors_elem) > 0: # если в массиве чисел с макс. кол-ом делителей уже есть числа
                max_num_divisors_elem.remove(max_num_divisors_elem[0]) # убираем первый эл-т из массива
            max_num_divisors_elem.append(elem) # добавляем новый элемент в массив
    return max_num_divisors_elem """

def find_min_max(order_relation):
    max = 0
    min = 0
    max_lst = []
    min_lst = []
    min_max = {}
    for i in order_relation:
        count_max = 0
        count_min = 0
        for j in order_relation:
            if i != j:
                if i % j == 0:
                    count_max+=1
                else:
                    count_min+=1
        if count_max > max:
            max = count_max
            max_lst.clear()
            max_lst.append(i)
        elif count_max == max:
            max_lst.append(i)
        if count_min > min:
            min = count_min
            min_lst.clear()
            min_lst.append(i)
        elif count_min == min:
            min_lst.append(i)
    min_max['min'] = min_lst
    min_max['max'] = max_lst
    return min_max

print(find_min_max([2, 3, 5, 6, 7, 10, 11, 14, 15, 21, 22, 30, 33, 35, 42, 55, 66, 70, 77, 105, 110, 154, 165, 210, 231, 330, 385, 462, 770, 1155, 2310]))