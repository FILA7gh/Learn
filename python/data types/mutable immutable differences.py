"""

В Python типы данных можно разделить на изменяемые и неизменяемые в зависимости от того,
можно ли изменять их значения после создания.


Вот основные отличия между изменяемыми и неизменяемыми типами данных:

    Неизменяемые типы данных:

        Не могут быть изменены после создания:

            Значение неизменяемого типа данных не может быть изменено после создания объекта.
            Если вы пытаетесь изменить значение
            неизменяемого объекта, будет создан новый объект с новым значением.


        Примеры неизменяемых типов данных:

            int, float, complex, str, tuple.


        Пример использования:

            Когда вам необходимо иметь уверенность в том, что значение не будет изменено,
            например, когда вы используете строку в качестве ключа в словаре.


    Изменяемые типы данных:

        Могут быть изменены после создания:

            Значение изменяемого типа данных может быть изменено напрямую после создания объекта.
            Изменение значения изменяемого объекта не создает новый объект.


        Примеры изменяемых типов данных:

            list, dict, set, bytearray.


        Пример использования:

            Когда вам нужно изменять структуру данных, например, добавлять или удалять элементы из списка или словаря.


    Создание новых объектов:

        Неизменяемые типы данных:

            При изменении значения неизменяемого объекта создается новый объект с новым значением.


        Изменяемые типы данных:

            Изменение значения изменяемого объекта не создает новый объект.


    Потенциальная опасность изменений:

        Неизменяемые типы данных:

            Предотвращает неожиданные изменения значений, что может быть полезно в некоторых сценариях.


        Изменяемые типы данных:

            Могут быть более гибкими, но требуют осторожности при использовании,
            чтобы избежать неожиданных изменений, особенно в многопоточной среде.



Важно выбирать подходящий тип данных в зависимости от требуемого поведения программы.
Изменяемые типы данных обычно более гибкие и удобны для модификации, но неизменяемые типы данных
могут быть полезны, когда важно сохранить значение неизменным после его создания.


"""