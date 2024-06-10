Фабричный метод (Factory Method) - это порождающий паттерн проектирования, который используется для создания
объектов без указания их конкретных классов. Вместо этого, он определяет интерфейс для создания объекта,
но делегирует сам процесс создания подклассам. Таким образом, каждый подкласс может переопределить фабричный метод
и создавать объекты своего собственного класса.


Давайте рассмотрим пример использования фабричного метода на Python:

    from abc import ABC, abstractmethod

    # Абстрактный класс Creator
    class Creator(ABC):
        @abstractmethod
        def factory_method(self):
            pass

        def some_operation(self):
            product = self.factory_method()
            result = f"Creator: The same creator's code has just worked with {product.operation()}"
            return result


    # Конкретные классы Creator
    class ConcreteCreator1(Creator):
        def factory_method(self):
            return ConcreteProduct1()


    class ConcreteCreator2(Creator):
        def factory_method(self):
            return ConcreteProduct2()


    # Абстрактный класс Product
    class Product(ABC):
        @abstractmethod
        def operation(self):
            pass


    # Конкретные классы Product
    class ConcreteProduct1(Product):
        def operation(self):
            return "{Result of ConcreteProduct1}"


    class ConcreteProduct2(Product):
        def operation(self):
            return "{Result of ConcreteProduct2}"


    # Использование
    def client_code(creator):
        print(f"Client: I'm not aware of the creator's class, but it still works.\n"
              f"{creator.some_operation()}")


    if __name__ == "__main__":
        print("App: Launched with the ConcreteCreator1.")
        client_code(ConcreteCreator1())

        print("\n")

        print("App: Launched with the ConcreteCreator2.")
        client_code(ConcreteCreator2())


    В этом примере Creator - это абстрактный класс, который определяет фабричный метод factory_method().
    ConcreteCreator1 и ConcreteCreator2 - это конкретные классы, которые наследуют Creator
    и переопределяют метод factory_method(), чтобы создавать соответствующие продукты.
    Product - это абстрактный класс, который определяет метод operation(). ConcreteProduct1
    и ConcreteProduct2 - это конкретные классы продуктов, которые реализуют метод operation().


При использовании паттерна фабричного метода клиентский код работает с объектами через общий интерфейс создания,
что позволяет ему оставаться независимым от конкретных классов создаваемых объектов.
