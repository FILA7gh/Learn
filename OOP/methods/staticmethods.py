"""

staticmethod в Python - это встроенный декоратор, который позволяет определить метод класса,
который не требует ссылки на сам класс или его экземпляр в качестве первого аргумента.
 Этот метод может быть вызван как от экземпляра класса, так и от самого класса.


Основные концепции staticmethod

    Декоратор @staticmethod:

        @staticmethod применяется перед определением метода класса и указывает интерпретатору Python,
        что этот метод должен быть интерпретирован как статический метод.

        class MyClass:
            @staticmethod
            def static_method(arg1, arg2):
                # тело метода
                pass


    Отсутствие обязательного первого аргумента:

        В статическом методе отсутствует обязательный первый аргумент,
        который ссылается на класс (cls) или экземпляр (self).

        class MyClass:
            @staticmethod
            def static_method(arg1, arg2):
                # тело метода
                pass


    Использование статического метода:

        Статический метод может быть вызван как от экземпляра класса, так и от самого класса.

        obj = MyClass()
        obj.static_method(arg1, arg2)  # Вызов статического метода от экземпляра
        MyClass.static_method(arg1, arg2)  # Вызов статического метода от самого класса



Преимущества использования staticmethod

    Отсутствие зависимости от состояния экземпляра:

        Статические методы не зависят от состояния экземпляра класса и могут быть вызваны
        независимо от создания экземпляра.


    Изоляция логики, не связанной с экземпляром:

        Статические методы могут быть использованы для изоляции логики, которая не зависит от
        конкретного экземпляра класса и не требует доступа к его атрибутам или методам.


    Легкая читаемость и понимание кода:

        Использование статических методов может улучшить читаемость и понимание кода,
        так как они явно указывают, что логика метода не зависит от экземпляра.



Заключение

    staticmethod в Python предоставляет удобный способ определения методов класса,
    которые не зависят от состояния экземпляра класса. Он часто используется для изоляции логики,
    которая не требует доступа к атрибутам или методам экземпляра, и для улучшения читаемости и понимания кода.

"""