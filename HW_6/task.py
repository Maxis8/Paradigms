# Предположим, что мы хотим найти элемент в массиве (получить
# его индекс). Мы можем это сделать просто перебрав все элементы.
# Но что, если массив уже отсортирован? В этом случае можно
# использовать бинарный поиск. Принцип прост: сначала берём
# элемент находящийся посередине и сравниваем с тем, который мы
# хотим найти. Если центральный элемент больше нашего,
# рассматриваем массив слева от центрального, а если больше -
# справа и повторяем так до тех пор, пока не найдем наш элемент.
# ● Ваша задача
# Написать программу на любом языке в любой парадигме для
# бинарного поиска. На вход подаётся целочисленный массив и
# число. На выходе - индекс элемента или -1, в случае если искомого
# элемента нет в массиве.


def binary_search(num, lst):
    left = 0
    right = len(lst) - 1

    while left <= right:
        middle = (left + right) // 2

        if lst[middle] == num:
            return middle

        elif lst[middle] > num:
            right = middle - 1

        else:
            left = middle + 1

    else:
        return -1


my_lst = [1, 2, 3, 4, 5, 6, 7, 8]
print(binary_search(8, my_lst))

