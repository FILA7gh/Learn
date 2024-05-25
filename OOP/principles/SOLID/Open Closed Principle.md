
Принцип открытости/закрытости (Open/Closed Principle, OCP) - это принцип объектно-ориентированного программирования,
который определяет, что программные сущности должны быть открыты для расширения,
но закрыты для модификации. Суть принципа заключается в том, что после написания кода
существующие классы или модули должны быть готовы к расширению новой функциональностью
без необходимости изменения их исходного кода.


Основные идеи OCP:

    Открытость для расширения:

        Программные сущности (классы, модули, функции и т. д.) должны быть открыты для расширения
        новой функциональностью. Это означает, что их поведение можно изменить
        или расширить без необходимости изменения их исходного кода.


    Закрытость для модификации:

        Программные сущности должны быть закрыты для модификации. Это означает, что их исходный код
        не должен изменяться, когда требуется добавить новую функциональность или изменить поведение.


    Использование абстракций:

        Для достижения OCP часто используются абстракции, такие как интерфейсы,
        абстрактные классы или полиморфизм, которые позволяют программным сущностям быть открытыми
        для расширения и закрытыми для модификации.



Пример применения OCP:

    Предположим, у нас есть класс Shape, который представляет геометрическую фигуру,
    и мы хотим добавить возможность вычисления площади для новых типов фигур.

    class Shape:
        def __init__(self):
            pass

        def area(self):
            pass

    class Rectangle(Shape):
        def __init__(self, width, height):
            self.width = width
            self.height = height

        def area(self):
            return self.width * self.height

    class Circle(Shape):
        def __init__(self, radius):
            self.radius = radius

        def area(self):
            return 3.14 * self.radius ** 2

    Этот код нарушает OCP, потому что для добавления нового типа фигуры (например, треугольника)
    нам придется изменить существующий код, что противоречит принципу закрытости для модификации.


    Чтобы применить OCP, мы можем использовать полиморфизм и абстрактные классы:

        from abc import ABC, abstractmethod

        class Shape(ABC):
            @abstractmethod
            def area(self):
                pass

        class Rectangle(Shape):
            def __init__(self, width, height):
                self.width = width
                self.height = height

            def area(self):
                return self.width * self.height

        class Circle(Shape):
            def __init__(self, radius):
                self.radius = radius

            def area(self):
                return 3.14 * self.radius ** 2

    Теперь мы можем добавить новый тип фигуры, не изменяя существующий код:

        class Triangle(Shape):
            def __init__(self, base, height):
                self.base = base
                self.height = height

            def area(self):
                return 0.5 * self.base * self.height


    Этот пример демонстрирует, как применение принципа открытости/закрытости позволяет
    легко добавлять новую функциональность без необходимости изменения существующего кода.

