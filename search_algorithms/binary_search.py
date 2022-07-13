import math
"""Бинарный поиск - Нахождение элемента в отсортированном массиве. Ищется серединное значение, потом переход в левую 
или правую часть, в зависимости от того, больше или меньше элемент. О(n) = log n"""

def binary_search(list_for_search, item):
    low = 0  # low initial boundary
    high = len(list_for_search) - 1  # high initial boundary
    while low <= high:
        mid = math.ceil((low + high) / 2)  # index at the middle between low and hugh boundaries
        guess = list_for_search[mid]  # element of list with this index
        if guess == item:  # found
            return mid
        if guess > item:  # items at the left part about this current middle element, we can cut right part of this list
            high = mid - 1
        else:  # items at the right part about this current middle element, we can cut left part of this list
            low = mid + 1
    return None


my_list = [1, 3, 5, 7, 9]
print(binary_search(my_list, -1))
print(binary_search(my_list, 3))

