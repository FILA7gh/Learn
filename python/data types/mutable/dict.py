"""

В Python словарь (dict) — это изменяемый неупорядоченный контейнер,
который хранит пары ключ-значение. Словари позволяют быстро получать доступ
к значениям по их ключам.


Вот основные особенности словарей:

    Изменяемость (Mutable):

        Словари можно изменять после их создания. Можно добавлять,
        удалять или изменять пары ключ-значение.

        my_dict = {'name': 'Alice', 'age': 25}
        my_dict['age'] = 26  # теперь my_dict станет {'name': 'Alice', 'age': 26}


    Неупорядоченность (Unordered):

        В версиях Python до 3.7 словари не гарантировали сохранение порядка
        добавления элементов. Начиная с Python 3.7, словари сохраняют порядок добавления элементов,
        но это считается реализационной деталью.

        my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
        print(my_dict)  # {'name': 'Alice', 'age': 25, 'city': 'New York'} (порядок сохранен)


    Ключи должны быть хэшируемыми (Keys must be hashable):

        Ключи словаря должны быть неизменяемыми типами данных, такими как строки,
        числа или кортежи. Значения могут быть любого типа.

        my_dict = {1: 'one', (2, 3): 'tuple', 'name': 'Alice'}


    Быстрый доступ (Fast Lookups):

        Словари обеспечивают быстрый доступ к значениям по ключам благодаря хэш-таблице.

        my_dict = {'name': 'Alice', 'age': 25}
        print(my_dict['name'])  # выведет 'Alice'


    Методы словарей:

        Python предоставляет множество встроенных методов для работы со словарями,
         таких как get(), keys(), values(), items(), pop(), popitem(), update() и другие.

        my_dict = {'name': 'Alice', 'age': 25}
        print(my_dict.get('name'))  # выведет 'Alice'
        print(my_dict.keys())       # выведет dict_keys(['name', 'age'])
        print(my_dict.values())     # выведет dict_values(['Alice', 25])
        print(my_dict.items())      # выведет dict_items([('name', 'Alice'), ('age', 25)])


    Добавление и удаление элементов:

        Новые пары ключ-значение можно добавлять путем присваивания значения по новому ключу.
        Удалять элементы можно с помощью метода pop(), оператора del или метода popitem().

        my_dict = {'name': 'Alice', 'age': 25}
        my_dict['city'] = 'New York'  # добавление нового элемента
        print(my_dict)  # {'name': 'Alice', 'age': 25, 'city': 'New York'}

        my_dict.pop('age')  # удаление элемента по ключу
        print(my_dict)  # {'name': 'Alice', 'city': 'New York'}

        del my_dict['city']  # удаление элемента с использованием del
        print(my_dict)  # {'name': 'Alice'}

        my_dict.popitem()  # удаляет последнюю добавленную пару ключ-значение


    Создание словарей:

        Словари можно создавать с использованием литералов ({}), функции dict(), и генераторов словарей.

        my_dict = {'name': 'Alice', 'age': 25}
        my_dict2 = dict(name='Bob', age=30)
        my_dict3 = {k: v for k, v in [('name', 'Alice'), ('age', 25)]}


Словари являются мощным инструментом для работы с ассоциативными массивами или
хэш-таблицами, позволяя эффективно организовывать и обрабатывать данные
с использованием ключей для быстрого доступа к значениям.

"""
