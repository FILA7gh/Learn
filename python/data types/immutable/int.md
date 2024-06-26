

В Python int (целое число) — это встроенный тип данных, представляющий собой целое число.


Вот основные особенности и возможности работы с целыми числами (int):

    Неизменяемость (Immutable):
        Объекты типа int являются неизменяемыми,
        то есть любое изменение значения приводит к созданию нового объекта.

        a = 10
        b = a
        a = 20
        print(b)  # выведет 10


    Произвольная точность (Arbitrary Precision):
        Целые числа в Python имеют произвольную точность, то есть могут быть сколь
        угодно большими, ограничиваясь только объемом доступной памяти.

        large_num = 1234567890123456789012345678901234567890
        print(large_num)  # выведет 1234567890123456789012345678901234567890


    Базовые арифметические операции:
        Целые числа поддерживают все стандартные арифметические операции:
        сложение (+), вычитание (-), умножение (*), деление (/),
        целочисленное деление (//), взятие остатка (%), возведение в степень (**).

        a = 10
        b = 3

        print(a + b)  # выведет 13
        print(a - b)  # выведет 7
        print(a * b)  # выведет 30
        print(a / b)  # выведет 3.3333333333333335
        print(a // b) # выведет 3
        print(a % b)  # выведет 1
        print(a ** b) # выведет 1000


    Битовые операции:
        Целые числа поддерживают битовые операции, такие как побитовое И (&), побитовое ИЛИ (|),
        побитовое исключающее ИЛИ (^), побитовый сдвиг влево (<<), побитовый сдвиг вправо (>>), побитовое НЕ (~).

        a = 5  # 0b0101
        b = 3  # 0b0011

        print(a & b)  # выведет 1 (0b0001)
        print(a | b)  # выведет 7 (0b0111)
        print(a ^ b)  # выведет 6 (0b0110)
        print(a << 1) # выведет 10 (0b1010)
        print(a >> 1) # выведет 2 (0b0010)
        print(~a)     # выведет -6 (0b...1010)


    Встроенные функции для работы с целыми числами:

        abs(x): Возвращает абсолютное значение числа x.
        pow(x, y[, z]): Возвращает x в степени y, если указан третий аргумент z, то результат делится по модулю z.
        divmod(a, b): Возвращает пару чисел (a // b, a % b).
        int(x): Преобразует значение x в целое число.

        print(abs(-10))       # выведет 10
        print(pow(2, 3))      # выведет 8
        print(pow(2, 3, 3))   # выведет 2
        print(divmod(10, 3))  # выведет (3, 1)
        print(int(3.14))      # выведет 3


    Форматирование целых чисел:
        Целые числа можно форматировать различными способами, например, в десятичной,
        шестнадцатеричной, восьмеричной или двоичной системах счисления.

        num = 255

        print(f"{num}")    # выведет 255 (десятичное представление)
        print(f"{num:x}")  # выведет ff (шестнадцатеричное представление)
        print(f"{num:o}")  # выведет 377 (восьмеричное представление)
        print(f"{num:b}")  # выведет 11111111 (двоичное представление)


    Преобразование строк в целые числа:
        Строки можно преобразовать в целые числа с использованием функции int().

        num_str = "12345"
        num = int(num_str)
        print(num)  # выведет 12345


Целые числа (int) в Python являются мощным и гибким инструментом
для выполнения различных арифметических и битовых операций,
и они поддерживают широкий набор встроенных функций и методов для работы с ними.

