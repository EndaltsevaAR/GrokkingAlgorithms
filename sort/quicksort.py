"""Быстрая сортировка - Выбирается опорный элемент (элемент массива). Весь массив сравнивается с ним: меньше левее,
больше - правееот него. Смысл в том, чтобы каждую часть уменьшить до массива в 0 или 1 элемент. Рекурсивно уменьшаем
массивы с каждой из стороны, а потом соединяем. Худшее: O(n *n) , лучшее (среднее): O(n * log n) """


def quicksort(arr):  # based at the recursion
    if len(arr) < 2:  # base
        return arr
    else:  # recursion
        pivot = arr[0]
        less = [i for i in arr[1:] if i <= pivot]
        greater = [i for i in arr[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)


print(quicksort([10, 5, 2, 3, 10]))
