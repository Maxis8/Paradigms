# Корреляция - статистическая мера, используемая для оценки
# связи между двумя случайными величинами.
# ● Ваша задача
# Написать скрипт для расчета корреляции Пирсона между
# двумя случайными величинами (двумя массивами). Можете
# использовать любую парадигму, но рекомендую использовать
# функциональную, т.к. в этом примере она значительно
# упростит вам жизнь.
# ● Формула корреляции Пирсона:

from statistics import mean


def calc(lst_x, lst_y):
    mean_lst1 = mean(lst_x)
    mean_lst2 = mean(lst_y)
    return sum(map(lambda x, y: (x - mean_lst1) * (y - mean_lst2), lst_x, lst_y)) / (
        sum(map(lambda x: (x - mean_lst1) ** 2, lst_x)) * sum(map(lambda y: (y - mean_lst2) ** 2, lst_y))) ** 0.5


lst1 = [3,5,2,1,6,7]
lst2 = [4,6,3,2,7,8]
print(calc(lst1, lst2))

