#Мы уже видели множество решений этой задачи в различных
#стилях. Пришло время решить её с помощью логической
#парадигмы.
#● Ваша задача
#Написать программу на языке Prolog для вычисления суммы
#элементов списка. На вход подаётся целочисленный массив.
#На выходе - сумма элементов массива.


sum_list([], 0).

sum_list([C|T], Sum) :-
    sum_list(T, Sum1), Sum is Sum1 + C.

?- sum_list([1,2,3,4,5,6,7,8,9,10], X),

    write('Sum of list elements: '),
    writeln(X),
    write('List: '),
    write([1,2,3,4,5,6,7,8,9,10]).

