

Конструкция match-case была введена в Python 3.10 и является мощным инструментом для сопоставления 
шаблонов (pattern matching). Она позволяет более чисто и выразительно обрабатывать различные случаи, 
аналогично switch-case в других языках программирования, но с дополнительной гибкостью.


Основные особенности match-case:

    Сопоставление значений: Сопоставление конкретных значений, как в традиционном switch-case.

    Сопоставление с шаблонами: Поддержка более сложных шаблонов, таких как кортежи, списки, классы и т.д.

    Гвардии (guards): Условия, которые можно добавлять к каждому случаю для дополнительной фильтрации.


Простой пример использования match-case

    Пример использования match-case для простого сопоставления значений:
        
        def switch_example(value):
            match value:
                case 1:
                    return "Value is 1"
                case 2:
                    return "Value is 2"
                case 3:
                    return "Value is 3"
                case _:
                    return "Value is unknown"
        
        print(switch_example(1))  # Output: Value is 1
        print(switch_example(4))  # Output: Value is unknown


    Использование шаблонов

        match-case позволяет сопоставлять сложные структуры данных. Рассмотрим пример с кортежами:
            
            def process_tuple(data):
                match data:
                    case (1, x):
                        return f"Tuple starts with 1, second element is {x}"
                    case (2, y):
                        return f"Tuple starts with 2, second element is {y}"
                    case (3, z):
                        return f"Tuple starts with 3, second element is {z}"
                    case _:
                        return "Tuple doesn't match any pattern"
            
            print(process_tuple((1, 'a')))  # Output: Tuple starts with 1, second element is a
            print(process_tuple((2, 'b')))  # Output: Tuple starts with 2, second element is b
            print(process_tuple((4, 'c')))  # Output: Tuple doesn't match any pattern

    
    Сопоставление с гвардиями

        Гвардии позволяют добавлять дополнительные условия к случаям:
            
            def process_value(value):
                match value:
                    case x if x > 0:
                        return f"Positive number: {x}"
                    case x if x < 0:
                        return f"Negative number: {x}"
                    case 0:
                        return "Zero"
                    case _:
                        return "Not a number"
            
            print(process_value(10))  # Output: Positive number: 10
            print(process_value(-5))  # Output: Negative number: -5
            print(process_value(0))   # Output: Zero


    Сопоставление с классами

        Вы также можете сопоставлять объекты классов и извлекать их атрибуты:
            
            class Point:
                def __init__(self, x, y):
                    self.x = x
                    self.y = y
            
            def process_point(point):
                match point:
                    case Point(x, y):
                        return f"Point with coordinates x: {x}, y: {y}"
            
            p = Point(1, 2)
            print(process_point(p))  # Output: Point with coordinates x: 1, y: 2



Преимущества match-case

    Читаемость: Код становится более читаемым и понятным.

    Выразительность: Возможность сопоставления сложных шаблонов и структур данных.

    Безопасность: Избегание ошибок, связанных с отсутствием обработчиков для некоторых случаев.



match-case является мощным инструментом, который делает Python еще более выразительным и удобным для написания кода,
который должен обрабатывать множество различных случаев и шаблонов.
