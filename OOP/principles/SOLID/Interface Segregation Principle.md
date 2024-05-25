
Принцип разделения интерфейса (Interface Segregation Principle, ISP) - это один из принципов SOLID
в объектно-ориентированном программировании, который утверждает,
что клиенты не должны зависеть от интерфейсов, которые они не используют.
Суть принципа заключается в том, чтобы интерфейсы были маленькими, специфичными и предоставляли
только те методы, которые нужны клиентам, чтобы избежать нарушения принципа единственной ответственности
и уменьшить зависимости между компонентами системы.


Основные идеи ISP:

    Специфичные интерфейсы:

        Интерфейсы должны быть специфичными для потребностей и возможностей клиентов.
        Лучше иметь несколько маленьких интерфейсов, чем один большой, общий интерфейс.


    Избегание избыточности:

        Интерфейсы не должны содержать избыточные методы, которые не используются всеми клиентами.
        Клиенты должны иметь возможность реализовать только те методы, которые им нужны.

    Уменьшение зависимостей:

        Использование маленьких и специфичных интерфейсов помогает уменьшить зависимости между
        компонентами системы, что делает ее более гибкой и устойчивой к изменениям.



Пример соблюдения ISP:

    Предположим, у нас есть интерфейс Printable, который используется для печати документов,
    и классы Document и Photo, которые могут быть напечатаны.

    from abc import ABC, abstractmethod

    class Printable(ABC):
        @abstractmethod
        def print(self):
            pass

    class Document(Printable):
        def print(self):
            print("Printing document...")

    class Photo(Printable):
        def print(self):
            print("Printing photo...")

    В этом примере интерфейс Printable является маленьким и специфичным, предоставляя только один метод print(),
    который используется клиентами для печати. Клиенты могут реализовать этот метод по-разному,
    в зависимости от своих потребностей.


Пример нарушения ISP:

    Предположим, у нас есть интерфейс Worker, который определяет методы для работы с данными и отправки уведомлений.

    from abc import ABC, abstractmethod

    class Worker(ABC):
        @abstractmethod
        def work(self):
            pass

        @abstractmethod
        def notify(self):
            pass

    Этот интерфейс нарушает ISP, потому что клиенты, которым нужно только выполнение работы,
    должны реализовать и метод notify(), хотя им это не нужно. Лучше разделить этот интерфейс
    на два более специфичных интерфейса: Workable и Notifiable, чтобы избежать избыточности.
