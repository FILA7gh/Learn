

В Python complex — это тип данных, представляющий комплексные числа.
Комплексные числа имеют реальную и мнимую части, и используются
для математических вычислений, включающих комплексные числа.


Вот основные особенности и возможности работы с комплексными числами в Python:

    Представление:
        Комплексное число записывается в формате a + bj, где a — это реальная часть,
        а b — мнимая часть. j в Python используется для обозначения мнимой единицы
        (в отличие от стандартного математического обозначения i).

        z = 3 + 4j


    Доступ к реальной и мнимой частям:
        Можно получить доступ к реальной и мнимой частям комплексного числа с помощью атрибутов .real и .imag.

        z = 3 + 4j
        print(z.real)  # выведет 3.0
        print(z.imag)  # выведет 4.0


    Арифметические операции:
        Комплексные числа поддерживают все стандартные арифметические операции:
        сложение (+), вычитание (-), умножение (*), деление (/), возведение в степень (**).

        z1 = 1 + 2j
        z2 = 3 + 4j

        print(z1 + z2)  # выведет (4+6j)
        print(z1 - z2)  # выведет (-2-2j)
        print(z1 * z2)  # выведет (-5+10j)
        print(z1 / z2)  # выведет (0.44+0.08j)
        print(z1 ** 2)  # выведет (-3+4j)


    Модуль и аргумент:
        Для вычисления модуля и аргумента (угла) комплексного числа можно использовать функции из модуля cmath.

        import cmath

        z = 3 + 4j
        modulus = abs(z)
        argument = cmath.phase(z)

        print(modulus)  # выведет 5.0
        print(argument) # выведет 0.9272952180016122 (радианы)


    Преобразование в алгебраическую форму:
        Модуль и аргумент можно использовать для получения алгебраической формы комплексного числа
        с помощью функции rect из модуля cmath.

        import cmath

        modulus = 5.0
        argument = cmath.pi / 4
        z = cmath.rect(modulus, argument)

        print(z)  # выведет (3.5355339059327378+3.5355339059327378j)


    Конъюгат:
        Комплексное число имеет комплексно-сопряженное число, которое можно получить с помощью метода .conjugate().

        z = 3 + 4j
        z_conjugate = z.conjugate()

        print(z_conjugate)  # выведет (3-4j)


    Создание комплексных чисел:
        Комплексные числа можно создавать с использованием литералов или функции complex().

        z1 = 3 + 4j
        z2 = complex(3, 4)

        print(z1)  # выведет (3+4j)
        print(z2)  # выведет (3+4j)


    Функции из модуля cmath:
        Для работы с комплексными числами Python предоставляет модуль cmath,
        который включает такие функции, как sqrt(), exp(), log(), sin(), cos() и многие другие.

        import cmath

        z = 1 + 1j
        sqrt_z = cmath.sqrt(z)
        exp_z = cmath.exp(z)
        log_z = cmath.log(z)
        sin_z = cmath.sin(z)
        cos_z = cmath.cos(z)

        print(sqrt_z)  # выведет (1.09868411346781+0.45508986056222733j)
        print(exp_z)   # выведет (1.4686939399158851+2.2873552871788423j)
        print(log_z)   # выведет (0.34657359027997264+0.7853981633974483j)
        print(sin_z)   # выведет (1.2984575814159773+0.6349639147847361j)
        print(cos_z)   # выведет (0.8337300251311491-0.9888977057628651j)


Комплексные числа (complex) в Python предоставляют мощный и удобный способ выполнения
математических операций и вычислений, связанных с комплексными числами,
благодаря поддержке широкого набора встроенных методов и функций.

