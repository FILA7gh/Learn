PEP 8 (Python Enhancement Proposal 8) — это документ, который предоставляет рекомендации
по написанию кода на языке программирования Python. Он был создан для того, чтобы коды,
написанные разными разработчиками, имели одинаковый стиль, что облегчает их чтение и сопровождение.

Вот основные правила и рекомендации из PEP 8:

    Стиль кодирования:

        Отступы:
            Используйте 4 пробела на один уровень отступа. Не используйте табуляцию.

            def my_function():
                if True:
                    print("Hello, world!")


    Максимальная длина строки:
        Строки не должны превышать 79 символов. Длина строки документации и комментариев не должна превышать 72 символа.


    Пустые строки:
        Используйте пустые строки для разделения классов и функций, а также для логического разделения больших блоков кода.

        class MyClass:
            """A simple example class"""

            def __init__(self, name):
                self.name = name

            def greet(self):
                print(f"Hello, {self.name}")


    Импорт:

        Импорты должны располагаться в начале файла, после комментариев и строк документации модуля.
        Импорты должны быть организованы в группы: стандартные библиотеки, сторонние библиотеки, модули проекта.
        Импорты должны быть по одному на строку.

        import os
        import sys

        from datetime import datetime
        from collections import defaultdict

        import requests


    Пробелы в выражениях и инструкциях:
        Не ставьте пробелы внутри скобок, за исключением случаев, когда этого требует стилистика.
        Ставьте пробелы вокруг операторов присваивания и других бинарных операторов.

        a = [1, 2, 3]
        b = (1, 2, 3)
        c = {'key': 1}

        x = 1
        y = x + 1


    Комментарии:
        Комментарии должны быть ясными и точными. Используйте пробел после символа #.

        # Это комментарий
        x = x + 1  # Инкремент переменной x


    Документирование:
        Используйте строки документации для описания модулей, классов и функций.
        Документирование должно начинаться и заканчиваться тройными кавычками.

        def add(a, b):
            """
            Возвращает сумму двух чисел.

            :param a: Первое число
            :param b: Второе число
            :return: Сумма a и b
            """
            return a + b


    Именование:
        Модули и пакеты: lower_case_with_underscores
        Классы: CapWords
        Функции и переменные: lower_case_with_underscores
        Константы: ALL_CAPS_WITH_UNDERSCORES

        class MyClass:
            MY_CONSTANT = 42

            def my_method(self):
                my_variable = 1
                return my_variable


Организация кода:

    Использование 4-х пробелов для отступов, не табуляций:

        for i in range(10):
            print(i)


    Импорты должны быть на отдельных строках:
        
        import os
        import sys


    Соблюдение порядка импорта:

        стандартные библиотеки, сторонние библиотеки, модули вашего проекта:
    
        import os
        import sys
        import numpy as np
        from myproject import mymodule


Практические примеры:

    Пример хорошего стиля (соответствует PEP 8):
        
        import os
        import sys
        
        class ExampleClass:
            """Документирование класса ExampleClass."""
        
            def __init__(self, name):
                self.name = name
        
            def greet(self):
                """Документирование метода greet."""
                print(f"Hello, {self.name}")
        
        def main():
            """Главная функция программы."""
            example = ExampleClass("World")
            example.greet()
        
        if __name__ == "__main__":
            main()


    Пример плохого стиля (не соответствует PEP 8):
        
        import os, sys
        
        class exampleClass():
          def __init__(self,name):
            self.name=name
          def greet(self):print('Hello, %s'% self.name)
        
        def main():
          example=exampleClass('World');example.greet()
        
        if __name__=='__main__':main()


Инструменты для проверки соответствия PEP 8:

    flake8:
    
        Комбинирует pyflakes, pycodestyle (бывший pep8) и mccabe для проверки стиля кода.
        
        pip install flake8
        flake8 your_script.py


    black:
        Форматтер кода, который автоматически преобразует ваш код в стиль, соответствующий PEP 8.
        
        pip install black
        black your_script.py


    pylint:
        Инструмент для статического анализа кода, который также проверяет соответствие PEP 8.
    
        pip install pylint
        pylint your_script.py


PEP 8 — это не набор жестких правил, а рекомендации, которые можно адаптировать под конкретный проект или команду. 
Главное — обеспечить согласованность стиля кода, чтобы сделать его более читаемым и поддерживаемым.
