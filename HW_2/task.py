# Условие
# На вход подается число n.
# ● Задача
# Написать скрипт в любой парадигме, который выводит на экран таблицу умножения всех чисел от 1 до n.
# Обоснуйте выбор парадигм.

num = 11
limit = int(input("Enter number: "))
START = 1
for i in range(START, num):
    for j in range(1, limit +1):
        print(f'{j:<2} x {i:>2} = {i * j:>2}', end="\t")
    print()

