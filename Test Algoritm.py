# уровень C Артём Вагайцев ИИ-72
import random, time, numpy

def geekbech(func):
    def wrapper(*args, **kwargs):
        time1 = time.time()
        print(func(*args, **kwargs), func.__name__)
        print(int((time.time() - time1) * 1000000000), "наносек")
    return wrapper

# 1
# glob_arr = [random.randint(-10000, 10000) for i in range(100)]
# print(glob_arr)
# print()
# @geekbech
# def bubble_sort(arr):
#     for i in range(len(arr)-1):
#         for j in range(len(arr)-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     return arr
#
# @geekbech
# def default_sort(arr):
#     arr.sort()
#     return arr
#
# bubble_sort(list(glob_arr))
# default_sort(list(glob_arr))

'''Встроенная сортировка быстрее так как она написанна на Си и имеет алгоритм быстрой сортировки у
которого временная сложность меньше чем у сортировки пузырьком из-за кол-во for'''

# 2
# n = int(input("Введите размер матрицы: "))
# matrix = [[random.randint(-10000, 10000) for j in range(n)] for i in range(n)]
# for row in matrix:
#     for element in row:
#         print(element, end=" ")
#     print()
# while True:
#     direction = input("Куда сдвинуть список (право или лево): ")
#     try:
#         count = int(input("Насколько сдвинуть список (число): "))
#         if direction.lower() == "лево":
#             for y in range(n):
#                 matrix[y] = matrix[y][count:] + matrix[y][:count]
#             break
#         elif direction.lower() == "право":
#             for y in range(n):
#                 matrix[y] = matrix[y][-count:] + matrix[y][:-count]
#             break
#     except:
#         pass
#
# for row in matrix:
#     for element in row:
#         print(element, end=" ")
#     print()

# 3

# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i - 1
#         while j > -1 and key < arr[j]:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = key
#     return arr
#
# n = int(input("Введите размер матрицы: "))
# matrix = [[random.randint(-10000, 10000) for j in range(n)] for i in range(n)]
# for row in matrix:
#     for element in row:
#         print(element, end=" ")
#     print()
# print()
# matrix_t = numpy.transpose(matrix)
# for i in range(n):
#     matrix_t[i] = insertion_sort(matrix[i])
#
# matrix = numpy.transpose(matrix_t)
#
# for row in matrix:
#     for element in row:
#         print(element, end=" ")
#     print()

'''Я выбрал сортировку вставками так как она одна из самых быстрых и к тому же я ее знаю
так как писал про нее доклад и призентацию а так же она имеет в лучшем случае она имеет линейную сложность
а в худшем квадратичную'''

# 4

# arr = [random.randint(-10000, 10000) for i in range(100)]
# print(arr)
# max_num = arr[0]
#
# @geekbech
# def bubble_sort(arr):
#     global max_num
#     for i in range(len(arr)-1):
#         for j in range(len(arr)-i-1):
#             if arr[j] > arr[j+1]:
#                 arr[j], arr[j+1] = arr[j+1], arr[j]
#     return arr[-1]
#
# @geekbech
# def brought_force(arr):
#     global max_num
#     for i in range(len(arr)-1):
#         if max_num < arr[i]:
#             max_num = arr[i]
#     return max_num
#
# bubble_sort(list(arr))
# brought_force(list(arr))

'''Брут форс лучше так как у него используется один for и он быстрее по скорости'''
