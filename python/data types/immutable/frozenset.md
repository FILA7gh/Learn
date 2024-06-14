

В Python frozenset — это неизменяемый вариант множества. Он предоставляет те же возможности
для хранения уникальных элементов и выполнения различных операций над множествами,
но при этом его содержимое нельзя изменять после создания.


Вот основные особенности frozenset:

    Неизменяемость (Immutable):

        Элементы frozenset нельзя добавлять, удалять или изменять после создания.
        Это делает frozenset хэшируемым, и его можно использовать в качестве ключа
        в словарях или элемента в других множествах.

        my_frozenset = frozenset([1, 2, 3])
        # my_frozenset.add(4)  # вызовет ошибку AttributeError


    Уникальность элементов (Unique Elements):

        Как и в обычных множествах, frozenset содержит только уникальные элементы.

        my_frozenset = frozenset([1, 2, 3, 3, 2])
        print(my_frozenset)  # выведет frozenset({1, 2, 3})


    Неупорядоченность (Unordered):

        Элементы frozenset не имеют фиксированного порядка.

        my_frozenset = frozenset([3, 1, 2])
        print(my_frozenset)  # порядок элементов может быть любым


    Высокая производительность (Performance):

        в словарях или элемента в других множествах.

        my_frozenset = frozenset([1, 2, 3])
        # my_frozenset.add(4)  # вызовет ошибку AttributeError


    Уникальность элементов (Unique Elements):

        Как и в обычных множествах, frozenset содержит только уникальные элементы
        frozenset обеспечивает быструю проверку на наличие элемента и поддержку
        множества операций благодаря использованию хэш-таблиц.


    Методы frozenset:

        frozenset поддерживает те же методы для работы с множествами,что и изменяемые множества (set),
        такие как union(), intersection(), difference(), symmetric_difference() и другие,
        но без методов изменения (таких как add(), remove(), discard()).

        my_frozenset = frozenset([1, 2, 3])
        another_frozenset = frozenset([3, 4, 5])

        union_frozenset = my_frozenset.union(another_frozenset)
        print(union_frozenset)  # выведет frozenset({1, 2, 3, 4, 5})

        intersection_frozenset = my_frozenset.intersection(another_frozenset)
        print(intersection_frozenset)  # выведет frozenset({3})

        difference_frozenset = my_frozenset.difference(another_frozenset)
        print(difference_frozenset)  # выведет frozenset({1, 2})


    Создание frozenset:

        frozenset можно создать с использованием функции frozenset()
        с любым итерируемым объектом в качестве аргумента.

        my_frozenset = frozenset([1, 2, 3])
        another_frozenset = frozenset('hello')
        print(another_frozenset)  # выведет frozenset({'e', 'h', 'l', 'o'})


    Использование в качестве ключей в словарях:

        Благодаря своей неизменяемости, frozenset можно использовать в качестве ключей
        в словарях и элементов в других множествах.

        my_dict = {frozenset([1, 2]): 'value'}
        print(my_dict[frozenset([1, 2])])  # выведет 'value'


frozenset полезен в тех случаях, когда нужно создать множество, которое
нельзя изменять после его создания, и когда важно использовать множество
в качестве ключа в словаре или элемента в другом множестве.
