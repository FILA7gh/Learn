
В Python float — это тип данных, представляющий числа с плавающей запятой,
которые используются для хранения вещественных чисел.


Вот основные особенности и возможности работы с числами типа float:

    Представление:

        Числа с плавающей запятой используются для представления вещественных чисел,
        которые включают дробную часть. Они хранятся в формате двойной точности (64 бита).

        a = 3.14
        b = -2.718


    Арифметические операции:

        Тип float поддерживает все стандартные арифметические операции:
        сложение (+), вычитание (-), умножение (*), деление (/), возведение в степень (**).

        a = 5.0
        b = 2.0
        print(a + b)  # выведет 7.0
        print(a - b)  # выведет 3.0
        print(a * b)  # выведет 10.0
        print(a / b)  # выведет 2.5
        print(a ** b) # выведет 25.0


    Деление:

        Деление двух целых чисел в Python всегда возвращает float.

        c = 7
        d = 2
        print(c / d)  # выведет 3.5


    Специальные значения:

        float поддерживает специальные значения, такие как inf (бесконечность) и nan (не число).

        positive_inf = float('inf')
        negative_inf = float('-inf')
        not_a_number = float('nan')

        print(positive_inf)  # выведет inf
        print(negative_inf)  # выведет -inf
        print(not_a_number)  # выведет nan


    Функции для работы с числами float:

        abs(x): Возвращает абсолютное значение числа x.
        round(x[, n]): Округляет число x до n знаков после запятой.
        math.floor(x): Возвращает наибольшее целое число, не превышающее x.
        math.ceil(x): Возвращает наименьшее целое число, не меньшее x.
        math.sqrt(x): Возвращает квадратный корень из x.

        import math

        print(abs(-3.14))       # выведет 3.14
        print(round(3.14159, 2)) # выведет 3.14
        print(math.floor(2.7))  # выведет 2
        print(math.ceil(2.7))   # выведет 3
        print(math.sqrt(16))    # выведет 4.0


    Форматирование чисел float:

        Числа с плавающей запятой можно форматировать с использованием различных методов.

        num = 3.14159
        print(f"{num:.2f}")  # выведет 3.14 (округление до двух знаков после запятой)
        print(f"{num:e}")    # выведет 3.141590e+00 (экспоненциальное представление)


    Преобразование строк в float:

        Строки можно преобразовать в числа с плавающей запятой с использованием функции float().

        num_str = "123.45"
        num = float(num_str)
        print(num)  # выведет 123.45


    Точность вычислений:

        Числа с плавающей запятой могут иметь проблемы
        с точностью из-за ограниченного количества бит, используемых для их представления.

        print(0.1 + 0.2)  # может не выдать ровно 0.3 из-за особенностей представления чисел с плавающей запятой

        Для высокоточных вычислений можно использовать модуль decimal,
        который предоставляет десятичные числа с произвольной точностью:

        from decimal import Decimal

        a = Decimal('0.1')
        b = Decimal('0.2')
        print(a + b)  # выведет 0.3 с точностью, заданной модулем Decimal


Числа с плавающей запятой (float) в Python обеспечивают гибкость и мощные возможности для работы
с вещественными числами, поддерживая широкий набор операций и методов для их обработки.
