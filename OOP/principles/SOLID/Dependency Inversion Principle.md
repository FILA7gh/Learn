
Принцип инверсии зависимостей (Dependency Inversion Principle, DIP) - это один из принципов SOLID
в объектно-ориентированном программировании, который утверждает, что модули верхнего уровня не должны зависеть
от модулей нижнего уровня. Оба типа модулей должны зависеть от абстракций.
Этот принцип также определяет, что конкретные реализации должны зависеть от абстракций, а не наоборот.
Суть принципа заключается в том, чтобы разделять интерфейсы и реализации, чтобы уменьшить связанность
между компонентами системы и сделать ее более гибкой и расширяемой.


Основные идеи DIP:

    Зависимость от абстракций:
        Модули верхнего уровня должны зависеть от абстракций, а не от конкретных реализаций.
        Это означает, что интерфейсы или абстрактные классы должны определять контракт между модулями,
        а конкретные реализации должны соответствовать этому контракту.


    Разделение интерфейсов и реализаций:
        Интерфейсы должны определять только то, что должен делать модуль, но не как это делать.
        Реализации должны обеспечивать конкретные способы выполнения задачи, но они не должны
        непосредственно зависеть от модулей верхнего уровня.


    Уменьшение связанности:
        Применение DIP помогает уменьшить связанность между компонентами системы,
        что делает ее более гибкой и расширяемой. Компоненты могут быть легко заменены
        или переиспользованы без необходимости изменения других компонентов.



Пример соблюдения DIP:

    Предположим, у нас есть класс NotificationService, который отвечает за отправку уведомлений,
    и класс EmailSender, который реализует отправку электронных писем.
    Класс NotificationService зависит от абстракции MessageSender, а не от конкретной реализации EmailSender.

    from abc import ABC, abstractmethod

    class MessageSender(ABC):
        @abstractmethod
        def send_message(self, message):
            pass

    class EmailSender(MessageSender):
        def send_message(self, message):
            print("Sending email:", message)

    class NotificationService:
        def __init__(self, message_sender: MessageSender):
            self.message_sender = message_sender

        def send_notification(self, message):
            self.message_sender.send_message(message)

    email_sender = EmailSender()
    notification_service = NotificationService(email_sender)
    notification_service.send_notification("Hello, world!")

    Этот код соблюдает DIP, потому что класс NotificationService зависит только от абстракции MessageSender,
    а не от конкретной реализации EmailSender. Это позволяет легко заменить EmailSender
    другой реализацией MessageSender, такой как SMSSender, без необходимости изменения кода NotificationService.


Пример нарушения DIP:

    class NotificationService:
        def __init__(self, email_sender):
            self.email_sender = email_sender

        def send_notification(self, message):
            self.email_sender.send_email(message)

    email_sender = EmailSender()
    notification_service = NotificationService(email_sender)
    notification_service.send_notification("Hello, world!")

    В этом примере класс NotificationService напрямую зависит от конкретной реализации EmailSender,
    что нарушает DIP. Если мы захотим использовать другую реализацию отправителя сообщений,
    нам придется изменить код NotificationService, что делает его менее гибким и трудным для поддержки.


