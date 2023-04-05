import copy
import lr1
import lr2


def menu():
    print("0 - Выход;\n"
          "1 - Лабораторная работа 1 (Классификация бинарных отношений и системы замыканий);\n"
          "2 - Лабораторная работа 2 (Отношение порядка и упорядоченные множества);\n")


#global BinMatrix
fl = True
create_check = False


menu()
while fl:
    lr_num = input("Введите номер лабораторной работы: ")
    match lr_num:
        case "0":
            print("Выход")
            break

        case "1":
            print("Лабораторная работа 1 (Классификация бинарных отношений и системы замыканий):\n")
            fl1 = True
            global BinMatrix
            while fl1:
                task_num = input("Введите номер для выполнения: ")
                match task_num:

                    case "info":
                        print("info - Возможные действия;\n"
                              "0 - Выход;\n"
                              "1 - Создание матрицы бинарного отношения;\n"
                              "2 - Вывод заданной матрицы;\n"
                              "3 - Поиск свойств бинарного отношения;\n"
                              "4 - Нахождение матриц основных замыканий заданного бинарного отношения;\n"
                              "5 - Нахождение матрицы эквивалентного замыкания заданного бинарного отношения;\n"
                              "6 - Нахождение фактор-множества заданного бинарного отношения;\n"
                              "7 - Построение системы представителей фактор-множества;\n")

                    case "0":
                        print("Выход в меню\n")
                        menu()
                        create_check = False
                        break

                    case "1":
                        n = int(input('Размерность матрицы бинарного отношения n = '))
                        print("Создание матрицы бинарного отношения: ")
                        BinMatrix = lr1.create_matrix(n)
                        lr1.print_matrix(BinMatrix)
                        create_check = True

                    case "2":
                        if not create_check:
                            print("Матрица бинарного отношения не задана!")
                        else:
                            print("Заданная матрица бинарного отношения: ")
                            lr1.print_matrix(BinMatrix)

                    case "3":
                        if not create_check:
                            print("Матрица бинарного отношения не задана!")
                        else:
                            print("Найденные свойства данного бинарного отношения: ")
                            lr1.reflex_check(BinMatrix)
                            lr1.symmetry_check(BinMatrix)
                            lr1.antisimmetry_check(BinMatrix)
                            lr1.tranzit_check(BinMatrix)

                    case "4":
                        if not create_check:
                            print("Матрица бинарного отношения не задана!")
                        else:
                            print("Матрицы основных замыканий заданного бинарного отношения: ")
                            BinMatrix1 = copy.deepcopy(BinMatrix)
                            BinMatrix2 = copy.deepcopy(BinMatrix)
                            BinMatrix3 = copy.deepcopy(BinMatrix)
                            print("Матрица рефлексивного замыкания: ")
                            lr1.print_matrix(lr1.reflex_closure(BinMatrix1))
                            print("Матрица симметричного замыкания: ")
                            lr1.print_matrix(lr1.symmetry_closure(BinMatrix2))
                            print("Матрица транзитивного замыкания: ")
                            lr1.print_matrix(lr1.tranzit_closure(BinMatrix3))

                    case "5":
                        if not create_check:
                            print("Матрица бинарного отношения не задана!")
                        else:
                            print("Матрица эквивалентного замыкания заданного бинарного отношения: ")
                            BinMatrix4 = copy.deepcopy(BinMatrix)
                            lr1.print_matrix(lr1.closure(BinMatrix4))

                    case "6":
                        if not create_check:
                            print("Матрица бинарного отношения не задана!")
                        else:
                            print("Фактор-множество:", *lr1.factor_set(BinMatrix))

                    case "7":
                        if not create_check:
                            print("Матрица бинарного отношения не задана!")
                        else:
                            print("Система представителей фактор-множества: ", *lr1.system(lr1.factor_set(BinMatrix)))

                    case _:
                        print("Введена неправильная команда! ")

        case "2":
            print("Лабораторная работа 2 (Отношение порядка и упорядоченные множества):\n")
            fl2 = True
            global ord_rel
            global level1
            context_check = False
            global ContextMatrix
            while fl2:
                task_num = input("Введите номер для выполнения: ")
                match task_num:

                    case "info":
                        print("info - Возможные действия;\n"
                              "0 - Выход;\n"
                              "1 - Создание отношения порядка;\n"
                              "2 - Нахождение минимальных (максимальных) и наименьших (наибольших) элементов заданного отношения порядка;\n"
                              "3 - Построение решетки концептов заданного контекста и ее диаграммы Хассе;\n"
                              "4 - Создание матрицы контекста;\n"
                              "5 - Вывод матрицы контекста на экран;\n"
                              "6 - Построение системы замыканий для введенной матрицы контекста и её диаграмма Хассе;"
                              "7 - Построение решетки концептов для введенной матрицы контекста и её диаграмма Хассе;")

                    case "0":
                        print("Выход в меню\n")
                        menu()
                        break

                    case "1":
                        num = input("Введите число для построения отношения порядка: ")
                        ord_rel = lr2.create_relation(int(num))
                        create_check = True

                    case "2":
                        if not create_check:
                            print("Отношение порядка не задано!")
                        else:
                            min_max = lr2.find_min_max(ord_rel)
                            if len(min_max['min']) == 1:
                                print(("Наименьший элемент заданного отношения порядка равен", *min_max['min']))
                            else:
                                print("Минимальные элементы заданного отношения порядка:", ", ".join(str(i) for i in min_max['min']))
                            if len(min_max['max']) == 1:
                                 print("Наибольший элемент заданного отношения порядка равен", *min_max['max'])
                            else:
                                print("Максимальные элементы заданного отношения порядка:", ", ".join(str(i) for i in min_max['max']))
                            
                    case "3":
                        if not create_check:
                            print("Отношение порядка не задано!")
                        else:
                            hl = lr2.hasse_levels(ord_rel)
                            print("Уровни диаграммы Хассе:", *hl)
                            hr = lr2.hasse_relations(hl)
                            print("Отношения диаграммы Хассе:", *hr)
                            lr2.create_hasse_diag(ord_rel, hr, hl)

                    case "4":
                        n = int(input('Размерность матрицы контекста n = '))
                        print("Создание матрицы контекста:")
                        ContextMatrix = lr2.create_matrix(n)
                        context_check = True
                        print("\nЗаданная матрица контекста K = (G, M, p):\n")
                        lr2.print_matrix(ContextMatrix)

                    case "5":
                        if not context_check:
                            print("Матрица контекста не задана!")
                            # 1 0 1 0
                            # 1 1 0 0
                            # 0 1 0 1
                            # 0 1 0 1
                        else:
                             print("\nЗаданная матрица контекста K = (G, M, p):\n")
                             lr2.print_matrix(ContextMatrix)

                    case "6":
                        if not context_check:
                            print("Матрица контекста не задана!")
                        else:
                            closure_system = lr2.get_sets(ContextMatrix)
                            print("\nМножества контекста заданной матрицы контекста:", closure_system)
                            print("\nУровни диаграммы Хассе: ")
                            levels = lr2.hasse_levels_for_context(closure_system)
                            lr2.sort_dict(levels)
                            for key, value in levels.items():
                                print(key, ": ", *value)
                            relations = lr2.hasse_relations_for_context(levels)
                            print("Отношения диаграммы Хассе для заданной матрицы контекста:", *relations)
                            lr2.create_hasse_diag_for_context(closure_system, relations, levels)

                    case "7":
                        if not context_check:
                             print("Матрица контекста не задана!")
                        else:
                            closure_system = lr2.get_sets(ContextMatrix)
                            levels1 = lr2.hasse_levels_for_context(closure_system)
                            lr2.sort_dict(levels1)
                            relations = lr2.hasse_relations_for_context(levels1)
                            levels2 = lr2.concept_create(levels1, ContextMatrix)
                            lr2.create_hasse_diag_for_concept(closure_system, relations, levels2 )

                    case _:
                        print("Введена неправильная команда! ")
                        
        case _:
            print("Введена неправильная команда! ")
