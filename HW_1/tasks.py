import random

# Дан список целых чисел numbers. Необходимо написать в императивном стиле процедуру для
# сортировки числа в списке в порядке убывания. Можно использовать любой алгоритм сортировки.
def quicksort_imperative(nums):
    if len(nums) <= 1:
        return nums
    else:
        q = random.choice(nums)
    l_nums = [n for n in nums if n < q]

    e_nums = [q] * nums.count(q)
    b_nums = [n for n in nums if n > q]
    return quicksort_imperative(b_nums) + e_nums + quicksort_imperative(l_nums)


num_list = [-4,5,5,6,-9,-4,3,4,7,0,0]
print(quicksort_imperative(num_list))

#Написать точно такую же процедуру, но в декларативном стиле
print(sorted(num_list, reverse=True))

