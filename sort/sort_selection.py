"""Сортировка выбором - Проходится по всему списку и выбирается, например, самый больший элемент и добавляется в новый
временный список, а из старого списка удаляется. И так для всех элементов. O(n*n)"""


def sort_selection(arr):
    new_arr = []
    for i in range(len(arr)):
        smallest = find_smallest(arr)
        # each step find the smallest element, add to new array and remove from origin array
        new_arr.append(arr.pop(smallest))
    return new_arr


def find_smallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index


print(sort_selection([1, 5, 3, 2]))
