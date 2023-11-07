test_array = [0, 1, 18, 345, 1000, 2017, 5089, 9999]
fatal_element = 2
compleat_element = 18


def binary_search(arr: list, element: int, start=0, end=None) -> int:
    """Метод осуществляет бинарный поиск элемента в массиве, возвращая индекс этого элемента или -1, если его нет."""

    if end is None:
        end = len(arr) - 1
    if start > end:
        return -1

    center = (start + end) // 2
    if element == arr[center]:
        return center

    if element < arr[center]:
        return binary_search(arr, element, start, center - 1)

    return binary_search(arr, element, center + 1, end)


print(binary_search(test_array, compleat_element))

