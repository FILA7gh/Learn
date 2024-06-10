Паттерн Прототип (Prototype) - это порождающий паттерн проектирования,
который позволяет создавать новые объекты путем копирования существующих объектов-прототипов.
Таким образом, он позволяет избежать сложного процесса создания объектов с нуля,
предоставляя возможность клонировать существующие объекты и настраивать их по необходимости.


Давайте рассмотрим пример использования паттерна Прототип на Python:

    import copy

    # Класс Прототипа
    class Prototype:
        def __init__(self):
            self._objects = {}

        def register_object(self, name, obj):
            self._objects[name] = obj

        def unregister_object(self, name):
            del self._objects[name]

        def clone(self, name, **attrs):
            obj = copy.deepcopy(self._objects.get(name))
            obj.__dict__.update(attrs)
            return obj


    # Пример класса, который будет использоваться в качестве Прототипа
    class Car:
        def __init__(self):
            self.make = "Toyota"
            self.model = "Corolla"
            self.year = 2020

        def __str__(self):
            return f"{self.year} {self.make} {self.model}"


    if __name__ == "__main__":
        prototype = Prototype()

        car = Car()
        prototype.register_object("Car", car)

        car_clone = prototype.clone("Car", year=2021)
        print(car_clone)  # Вывод: 2021 Toyota Corolla


    В этом примере Prototype - это класс, который предоставляет методы для регистрации, удаления
    и клонирования объектов-прототипов. Car - это класс, который мы хотим использовать в качестве прототипа.
    Мы регистрируем объект Car в прототипе и затем создаем его клон с помощью метода clone,
    передавая имя объекта и атрибуты, которые мы хотим изменить в клоне.


Паттерн Прототип полезен, когда создание объекта путем копирования существующего объекта более эффективно,
чем создание его с нуля, или когда конкретная реализация создания объекта должна быть скрыта от клиентского кода.
