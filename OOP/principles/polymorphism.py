"""

Полиморфизм — это один из ключевых принципов объектно-ориентированного программирования (ООП),
который позволяет объектам разных классов быть обработанными через один и тот же интерфейс.
Полиморфизм означает "многообразие форм", и в контексте ООП это означает, что один и тот же метод может работать
по-разному в зависимости от объекта, который его вызывает.


Виды полиморфизма

    Полиморфизм через наследование:

        Методы базового класса переопределяются в производных классах.

        class Animal:
            def speak(self):
                pass

        class Dog(Animal):
            def speak(self):
                return "Woof!"

        class Cat(Animal):
            def speak(self):
                return "Meow!"

        def make_animal_speak(animal):
            print(animal.speak())

        dog = Dog()
        cat = Cat()

        make_animal_speak(dog)  # Вывод: Woof!
        make_animal_speak(cat)  # Вывод: Meow!


    Полиморфизм через интерфейсы:

        Разные классы реализуют одни и те же методы, определенные в абстрактном базовом классе.

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
                return 3.14 * (self.radius ** 2)

        shapes = [Rectangle(4, 5), Circle(3)]
        for shape in shapes:
            print(shape.area())


    Полиморфизм через перегрузку операторов:

        Методы, такие как __add__, __sub__ и другие магические методы, позволяют изменять поведение
        стандартных операторов для пользовательских классов.

        class Vector:
            def __init__(self, x, y):
                self.x = x
                self.y = y

            def __add__(self, other):
                return Vector(self.x + other.x, self.y + other.y)

            def __repr__(self):
                return f"Vector({self.x}, {self.y})"

        v1 = Vector(2, 3)
        v2 = Vector(5, 7)
        print(v1 + v2)  # Вывод: Vector(7, 10)



Преимущества полиморфизма

    Упрощение кода:

        Полиморфизм позволяет писать код, который работает с любыми объектами, реализующими нужный интерфейс,
        без знания конкретного типа объекта.

        def process_shapes(shapes):
            for shape in shapes:
                print(shape.area())

        shapes = [Rectangle(4, 5), Circle(3)]
        process_shapes(shapes)


    Расширяемость:

        Новые классы можно добавлять без изменения существующего кода. Достаточно просто реализовать
        нужные методы в новом классе.

        class Triangle(Shape):
            def __init__(self, base, height):
                self.base = base
                self.height = height

            def area(self):
                return 0.5 * self.base * self.height

        shapes.append(Triangle(6, 8))
        process_shapes(shapes)  # Теперь функция обработает и треугольник


    Гибкость и поддерживаемость:

        Полиморфизм делает системы более гибкими и легко поддерживаемыми, так как добавление новых типов объектов
        или изменение поведения существующих типов не требует изменения основного кода.



Заключение

    Полиморфизм является мощным средством для написания гибкого, повторно используемого и расширяемого кода.
    Он позволяет разработчикам создавать универсальные интерфейсы для работы с различными типами объектов,
    что значительно упрощает сопровождение и развитие программных систем. Полиморфизм через наследование,
    интерфейсы и перегрузку операторов позволяет решать широкий спектр задач, делая код более читаемым и управляемым.



"""