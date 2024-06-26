

В Python str (строка) — это неизменяемый последовательный тип данных, используемый для хранения и обработки текста.


Вот основные особенности и возможности работы со строками в Python:

    Создание строк:
        Строки создаются с помощью одинарных ('...'), двойных ("..."),
        тройных одинарных ('''...''') или тройных двойных (\"""...\""") кавычек.

        single_quote_str = 'Hello, World!'
        double_quote_str = "Hello, World!"
        triple_single_quote_str = '''Hello,
        World!'''
        triple_double_quote_str = \"""Hello, World!\"""


    Доступ к символам:
        Строки поддерживают индексирование и извлечение срезов. Индексация начинается с нуля,
        также поддерживается отрицательная индексация.

        s = "Hello, World!"
        print(s[0])   # выведет 'H'
        print(s[-1])  # выведет '!'
        print(s[7:12]) # выведет 'World'


    Неизменяемость (Immutable):
        Строки неизменяемы, что означает, что после создания строку нельзя изменить.
        Любое изменение создаст новую строку.

        s = "Hello"
        s = s + ", World!"  # создается новая строка
        print(s)  # выведет 'Hello, World!'


    Длина строки:
        Функция len() возвращает количество символов в строке.

        s = "Hello, World!"
        print(len(s))  # выведет 13


    Методы строк:
        Строки имеют множество встроенных методов для обработки текста, такие как:

            str.lower():
                Преобразует все символы строки в нижний регистр.
            

            str.upper():
                Преобразует все символы строки в верхний регистр.
            

            str.strip():
                Удаляет пробелы в начале и в конце строки.
            

            str.split(sep=None):
                Разбивает строку по указанному разделителю и возвращает список подстрок.
            

            str.join(iterable):
                Объединяет элементы из итерируемого объекта в одну строку, используя строку-разделитель.
            

            str.find(sub):
                Возвращает индекс первого вхождения подстроки, или -1, если подстрока не найдена.
            

            str.replace(old, new):
                Заменяет все вхождения подстроки old на new.


        s = " Hello, World! "

        print(s.lower())  # выведет ' hello, world! '
        print(s.upper())  # выведет ' HELLO, WORLD! '
        print(s.strip())  # выведет 'Hello, World!'
        print(s.split(','))  # выведет [' Hello', ' World! ']
        print('-'.join(['Hello', 'World']))  # выведет 'Hello-World'
        print(s.find('World'))  # выведет 8
        print(s.replace('World', 'Python'))  # выведет ' Hello, Python! '


    Форматирование строк:
        Python поддерживает несколько способов форматирования строк:

            Старый стиль: Оператор %.
            Новый стиль: Метод str.format().
            f-строки (f-strings): Начиная с Python 3.6, строки,
            начинающиеся с f или F, позволяют включать выражения Python внутри строк.

            name = "Alice"
            age = 30
    
            # Старый стиль
            print("My name is %s and I am %d years old." % (name, age))
    
            # Новый стиль
            print("My name is {} and I am {} years old.".format(name, age))
    
            # f-строки
            print(f"My name is {name} and I am {age} years old.")


    Экранирование символов:
        Специальные символы могут быть экранированы с помощью обратной косой черты (\).

        s = "He said, \"Hello, World!\""
        print(s)  # выведет 'He said, "Hello, World!"'


    Многострочные строки:
        Многострочные строки создаются с использованием тройных кавычек.

        multi_line_str = \"""This is a
        multi-line string.\"""
        print(multi_line_str)


    Проверочные методы: Строки имеют методы для проверки их свойств, такие как:

        str.isdigit(): Проверяет, состоит ли строка только из цифр.
        str.isalpha(): Проверяет, состоит ли строка только из букв.
        str.isspace(): Проверяет, состоит ли строка только из пробельных символов.
        str.startswith(prefix): Проверяет, начинается ли строка с указанного префикса.
        str.endswith(suffix): Проверяет, заканчивается ли строка указанным суффиксом.

        s = "Hello123"
        print(s.isdigit())  # выведет False
        print(s.isalpha())  # выведет False
        print(s.startswith("He"))  # выведет True
        print(s.endswith("123"))  # выведет True



Строки (str) в Python предоставляют мощные и гибкие возможности для работы с текстом,
поддерживая множество методов и функций для обработки, форматирования и анализа строковых данных.

