

Кортеж (tuple) в Python — это неизменяемый упорядоченный контейнер, который может
содержать элементы любого типа.


Вот несколько ключевых особенностей кортежей:

    Неизменяемость (Immutable):
        Кортежи не могут быть изменены после их создания. Это значит,
        что элементы кортежа нельзя добавлять, удалять или изменять.

        my_tuple = (1, 2, 3)
        # my_tuple[0] = 10  # вызовет ошибку TypeError


    Упорядоченность (Ordered):
        Элементы в кортеже сохраняют порядок, в котором они были добавлены.
        Можно получить доступ к элементам кортежа, используя индекс.

        my_tuple = ('apple', 'banana', 'cherry')
        print(my_tuple[1])  # выведет 'banana'


    Разнотипность (Heterogeneous):
        В кортеже могут храниться элементы разных типов данных.

        my_tuple = (1, "hello", 3.14, True)


    Поддержка вложенности (Nested Tuples):
        Кортежи могут содержать другие кортежи в качестве элементов,
        что позволяет создавать многомерные структуры данных.

        nested_tuple = ((1, 2, 3), (4, 5, 6), (7, 8, 9))


    Меньший объем памяти и высокая скорость (Memory Efficiency and Speed):
        Кортежи занимают меньше памяти и быстрее работают по сравнению
        со списками благодаря своей неизменяемости.


    Использование в качестве ключей в словарях (Hashability):
        Поскольку кортежи неизменяемы, они могут использоваться в качестве ключей
        в словарях и элементов множеств (если все их элементы также хэшируемы).

        my_dict = {(1, 2): 'value'}
        print(my_dict[(1, 2)])  # выведет 'value'


    Методы кортежей:
        Кортежи поддерживают меньше методов по сравнению со списками.
        Основные методы включают count() и index().

        my_tuple = (1, 2, 3, 1, 1)
        print(my_tuple.count(1))  # выведет 3
        print(my_tuple.index(3))  # выведет 2


    Доступ по индексу и срезы (Indexing and Slicing):
        Как и списки, к элементам кортежа можно обращаться по индексу,
        а также можно извлекать части кортежа с помощью срезов.

        my_tuple = (0, 1, 2, 3, 4, 5)
        print(my_tuple[2:5])  # выведет (2, 3, 4)
        print(my_tuple[:3])   # выведет (0, 1, 2)
        print(my_tuple[3:])   # выведет (3, 4, 5)


Кортежи часто используются для группировки данных, которые логически связаны
и не должны изменяться на протяжении выполнения программы. Благодаря неизменяемости
они могут использоваться в качестве ключей в словарях и элементов множеств, что делает их
полезными в определенных сценариях.


