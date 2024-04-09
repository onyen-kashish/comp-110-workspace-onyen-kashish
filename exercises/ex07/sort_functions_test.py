from exercises.ex07.sort_functions import selection_sort, insertion_sort


def test_selection_sort():
    list1: list[int] = [2, 4, 3, 6]
    selection_sort(list1)
    print(list1)

    list2: list[int] = [-7, -8, -9, -10]
    selection_sort(list2)
    print(list2)


def test_insertion_sort():
    list1: list[int] = [2, 4, 3, 6]
    insertion_sort(list1)
    print(list1)

    list2: list[int] = [-7, -8, -9, -10]
    insertion_sort(list2)
    print(list2)