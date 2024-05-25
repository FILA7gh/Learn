

В Python dataclass — это декоратор и библиотека, представленные в версии 3.7, которые упрощают
создание классов для хранения данных. dataclass автоматически генерирует методы, такие как
__init__, __repr__, __eq__ и другие, основываясь на аннотациях типов, которые вы предоставляете в вашем классе.
Это делает код более компактным и удобочитаемым, устраняя необходимость в написании шаблонного кода вручную.


Основные возможности и использование dataclass

    Основы dataclass

        Для использования dataclass, нужно импортировать декоратор
        dataclass из модуля dataclasses и применять его к классу:

            from dataclasses import dataclass

            @dataclass
            class Point:
                x: int
                y: int

        Этот код создаст класс Point с двумя атрибутами x и y. dataclass автоматически добавит метод
        __init__ для инициализации этих атрибутов:

            point = Point(1, 2)
            print(point)  # Output: Point(x=1, y=2)


Автоматически сгенерированные методы

    dataclass генерирует несколько методов по умолчанию:

        __init__: Инициализирует экземпляр класса с аннотированными атрибутами.

        __repr__: Возвращает строковое представление объекта.

        __eq__: Определяет равенство двух объектов на основе их атрибутов.

        __hash__: Опционально генерирует метод для использования объекта в хеш-таблицах, если установлено frozen=True.


Параметры dataclass

    dataclass поддерживает несколько параметров, которые контролируют его поведение:

        init: Если False, то не генерирует метод __init__.

        repr: Если False, то не генерирует метод __repr__.

        eq: Если False, то не генерирует метод __eq__.

        order: Если True, генерирует методы сравнения (<, <=, >, >=).

        unsafe_hash: Если True, генерирует метод __hash__, даже если eq установлено в False.

        frozen: Если True, делает экземпляры неизменяемыми (аналогично неизменяемым типам данных).



Пример использования параметров:

    @dataclass(frozen=True, order=True)
    class Point:
        x: int
        y: int


Поля в dataclass

    Вы можете использовать функцию field для настройки атрибутов:

    from dataclasses import dataclass, field

    @dataclass
    class Point:
        x: int = field(default=0)
        y: int = field(default=0)
        z: int = field(default=0, repr=False)  # Не включать в __repr__


Дополнительные возможности

        Пост-инициализация

            Если нужно выполнить дополнительную инициализацию после создания объекта,
            можно использовать метод __post_init__:

            @dataclass
            class Point:
                x: int
                y: int

                def __post_init__(self):
                    self.distance_from_origin = (self.x ** 2 + self.y ** 2) ** 0.5


    Наследование

        dataclass поддерживает наследование:

            @dataclass
            class Shape:
                color: str

            @dataclass
            class Circle(Shape):
                radius: float

    Поля с типом default_factory

        Для атрибутов, которые требуют вызова функции для установки значения по умолчанию,
        можно использовать default_factory:

            from dataclasses import dataclass, field
            from typing import List

            @dataclass
            class PointCollection:
                points: List[Point] = field(default_factory=list)


    Пример полной реализации

        from dataclasses import dataclass, field
        from typing import List

        @dataclass
        class Point:
            x: int
            y: int

        @dataclass
        class Shape:
            color: str

        @dataclass
        class Circle(Shape):
            radius: float

        @dataclass
        class PointCollection:
            points: List[Point] = field(default_factory=list)
            label: str = "Default Label"

            def add_point(self, point: Point):
                self.points.append(point)

        # Пример использования
        circle = Circle(color="red", radius=5.0)
        print(circle)
    
        point_collection = PointCollection()
        point_collection.add_point(Point(1, 2))
        print(point_collection)



Этот код демонстрирует основные возможности dataclass и их применение для упрощения создания классов,
что делает код более читаемым и поддерживаемым.


