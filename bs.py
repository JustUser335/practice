""" Бинарный поиск """

# import time
# from  itertools import chain

# def binary_search_recursive(arr, target, left = 0, right = None):
#     if right is None:
#         right = len(arr) - 1
#     if left > right:
#         return -1
#     mid = (left + right) // 2
#     if arr[mid] == target:
#         return mid
#     elif arr[mid] < target:
#         return binary_search_recursive(arr, target, mid + 1, right)
#     else: 
#         return binary_search_recursive(arr, target, left, mid - 1)
#     # Время выполнения кода: 0.000005 секунд

# def bsr_2(arr, target, mid = 0):
#     arr_len = len(arr) - 1
#     if arr_len < 20:
#         mid = arr_len // 2
#         if target == arr[mid]:
#             return mid
#         elif target > arr[mid]:
#             return bsr_2(arr[mid:], target, mid + 1)
#         else:
#             return bsr_2(arr[0:mid], target, mid - 1)
#     else:
#         count_part = arr_len // 3
#         p2 = (p1 := arr_len - count_part) - count_part
#         part_1 = arr[0:p2]
#         part_2 = arr[p2:p1]
#         part_3 = arr[p1:-1]

#         if target <= part_1[-1]:
#             return bsr_2(part_1, target)
#         elif target <= part_2[-1]:
#             return bsr_2(part_2, target)
#         elif target <= part_3[-1]:
#             return bsr_2(part_3, target)

# def bsr_3(arr, target, left = 0, right = None):
#     # как не крути я прихожу к тому что бинарный поиск в стандартном виде оптимален
#     # всё что у меня получается это увеличивать размер функции и количество возможных ошибок
#     # то место где у меня получается работать со скриптом, исполняется за тоже время что и база
#     if right is None:
#         right = len(arr) - 1
#     if left > right:
#         return -1
#     if arr[right] == target:
#         return right
#     if arr[left] == target:
#         return left
    
#     edge = (mid := (length := left + right) // 2) // 2
#     left = mid - edge
#     right = len(arr) - 1 if (z := mid + edge) > len(arr) else z
#     # print('mid',arr[mid], target)
#     if arr[mid] == target:
#         return mid

#     # print('arr[left]',arr[left],target)
#     # print('arr[right]',arr[right],target)

#     if arr[left] > target: 
#         right = left - 1
#         left = 0
#         # print(f'вошел в первый left = {left}, right = {right}')
#         return bsr_3(arr, target, left, right )
#     elif arr[right] < target:
#         left = right + 1
#         right = length
#         # print(f'вошел во второй left = {left}, right = {right}')
#         return bsr_3(arr, target, left, right )  
#     else:
#         if target < arr[mid]:
#             right = mid - 1
#             return bsr_3(arr, target, left, right )
#         elif target > arr[mid]:
#             left = mid + 1
#             return bsr_3(arr, target, left, right )


# # итеративный бинарный поиск
# def binary_search(arr, target):
#     low = 0
#     high = len(arr) - 1

#     while low <= high:
#         mid = (low + high) // 2
        
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             low = mid + 1
#         else:
#             high = mid - 1
            
#     return -1
#     #Время выполнения кода: 0.0000021 секунд 150k

# def _bs(arr, target):
#     # задаём диапазон поиска
#     low = 0 # нижняя граница
#     high = len(arr) - 1 # верхняя граница
#     # вычитаем - 1 ибо с 0 счет

#     while low <= hight:
#         # low должен быть меньше hight, если не так то область поиска отсутствует
#         mid = (low + high) // 2 # получаем середину путём деления нацело, точнее забираем целую часть от деления

#         # условие поиска, задача искать цент и каждый раз смещаться
#         # если меньше середины обновить минимальное значение 
#         # если больше середины обновить максимально значение
#         if arr[mid] == target:
#             return mid
#         elif arr[mid] < target:
#             low = mid + 1
#         else:
#             hight = mid - 1
#     # если ничего не нашел выйти с -1
#     return -1

# def f():
#     numbers = list(range(10000000))
#     result = 0
#     start_time = time.perf_counter()
#     # result = binary_search_recursive(numbers, 8)
#     # result = bsr_2(numbers, 8)
#     # result = binary_search(numbers, 8)
#     # result = bsr_3(numbers, 8)
#     end_time = time.perf_counter()
#     print(f"found at index: {result}")
#     execution_time = end_time - start_time 
#     print(f"Время выполнения кода: {execution_time:.6f} секунд")

# f()

#########################################
#            # Бинарный поиск
#########################################
# def binary_search_recursive(arr, target, left = 0, right = None):
#     if right is None:
#         right = len(arr) - 1
#     if left > right:
#         return -1
#     mid = (left + right) // 2
#     if arr[mid] == target:
#         return mid
#     elif arr[mid] < target:
#         return binary_search_recursive(arr, target, mid + 1, right)
#     else: 
#         return binary_search_recursive(arr, target, left, mid - 1)

# def bsr(arr, target, left = 0, right = None):
#     if right is None:
#         right = len(arr) - 1
#     if left > right:
#         return -1 
#     mid = (left + right) // 2
#     if arr[mid] == target:
#         return mid
#     elif arr[mid] < target:
#         return bsr(arr, target, mid + 1, right)
#     else: 
#         return bsr(arr, target, left, mid -1)

# def bsr(arr, target, left = 0, right = None):
#     if right is None:
#         right = len(arr) - 1
#     if left > right:
#         return -1
#     mid = (left + right) // 2
#     if arr[mid] == target:
#         return mid
#     elif arr[mid] > target:
#         return bsr(arr, target, left, mid - 1)
#     else: 
#         return bsr(arr, target, mid + 1, right)

def bsr(arr, target, left = 0, right = None):
    if right is None:
        right = len(arr) - 1 
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return bsr(arr, target, left, mid - 1)
    elif arr[mid] < target:
        return bsr(arr, target, mid + 1, right)

n_list = list(range(25, 10000000, 10))
res = bsr(n_list, 65)
print(res, n_list[res])