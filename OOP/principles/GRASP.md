

GRASP (General Responsibility Assignment Software Patterns или General Responsibility Assignment Software Principles)
— это набор шаблонов или принципов, помогающих определить распределение обязанностей и структурирование объектов
в объектно-ориентированном дизайне. Эти принципы разработаны для улучшения качества архитектуры 
программного обеспечения и помогают разработчикам принять решения о том, 
какие классы или объекты должны выполнять определенные задачи.


Вот основные принципы GRASP:
    
    1. Information Expert (Информационный эксперт)

        Определение: 
            
            Распределяйте ответственность так, чтобы операции выполнялись объектами, содержащими нужную информацию.
        
        Пример: 
            
            В системе управления библиотекой объект Book должен быть ответственным за предоставление 
            информации о названии и авторе книги, поскольку он содержит эти данные.
         
            class Book:
                def __init__(self, title, author):
                    self.title = title
                    self.author = author
            
                def get_book_info(self):
                    return f"{self.title} by {self.author}"


    2. Creator (Создатель)
    
        Определение: 
            
            Определяет, какой объект должен быть ответственен за создание других объектов.
            Создателем должен быть объект, который либо содержит, либо использует создаваемый объект.
        

        Пример: 
            
            В интернет-магазине объект Order может быть ответственным за создание OrderItem,
            поскольку он использует OrderItem.
         
            class OrderItem:
                def __init__(self, product, quantity):
                    self.product = product
                    self.quantity = quantity
                
            class Order:
                def __init__(self):
                    self.items = []
            
                def add_item(self, product, quantity):
                    item = OrderItem(product, quantity)
                    self.items.append(item)
        

    3. Controller (Контроллер)
    
        Определение: 
            
            Определяет объект, который управляет потоком событий в системе. Обычно это объект,
            представляющий собой посредника между пользователем и системой.
        

        Пример:
            
            В приложении для обработки заказов объект OrderController может обрабатывать 
            запросы пользователей на создание и управление заказами.
         
            class OrderController:
                def __init__(self, order_service):
                    self.order_service = order_service
            
                def create_order(self, customer_id, items):
                    order = self.order_service.create_order(customer_id, items)
                    return order

        
    4. Low Coupling (Низкая связанность)
    
        Определение: 
            
            Стремитесь минимизировать зависимости между объектами, чтобы изменения 
            в одном объекте минимально влияли на другие.
        
        Пример: 
                
            Использование интерфейсов для уменьшения зависимостей между компонентами.
         
            class EmailService:
                def send_email(self, recipient, message):
                    # Code to send email
                    pass
        
            class NotificationService:
                def __init__(self, email_service):
                    self.email_service = email_service
            
                def notify(self, recipient, message):
                    self.email_service.send_email(recipient, message)
        

    5. High Cohesion (Высокая связность)
    
        Определение: 
            
            Стремитесь к тому, чтобы методы и данные, объединенные в один класс, 
            были тесно связаны и направлены на выполнение одной задачи.
        

        Пример: 

            Класс Customer должен содержать только методы и данные, относящиеся к управлению информацией о клиенте.
         
            class Customer:
                def __init__(self, name, email):
                    self.name = name
                    self.email = email
            
                def update_email(self, new_email):
                    self.email = new_email
        

    6. Polymorphism (Полиморфизм)
    
        Определение: 

            Используйте полиморфизм для обработки различных типов объектов через единый интерфейс.
        

        Пример: 
            
            Использование интерфейса Shape для разных типов фигур (круг, квадрат).
         
            from abc import ABC, abstractmethod
            
            class Shape(ABC):
                @abstractmethod
                def draw(self):
                    pass
            
            class Circle(Shape):
                def draw(self):
                    print("Drawing a circle")
            
            class Square(Shape):
                def draw(self):
                    print("Drawing a square")
            
            def draw_shape(shape: Shape):
                shape.draw()
    

    7. Pure Fabrication (Чистая фабрикация)
    
        Определение: 
    
            Создание классов или методов, не основанных на реальных объектах предметной области, 
            для обеспечения низкой связанности и высокой связности.
        

        Пример: 

            Класс DatabaseConnection для управления соединением с базой данных.n
        
            class DatabaseConnection:
                def __init__(self, connection_string):
                    self.connection_string = connection_string
            
                def connect(self):
                    # Code to connect to database
                    pass
            
                def disconnect(self):
                    # Code to disconnect from database
                    pass
        

    8. Indirection (Посредничество)
    
        Определение: 

            Использование посредников для снижения прямых зависимостей между компонентами системы.
        

        Пример: 

            Использование шаблона Repository для доступа к данным.
            
            class ProductRepository:
                def __init__(self, database_connection):
                    self.database_connection = database_connection
            
                def get_product_by_id(self, product_id):
                    # Code to retrieve product from database
                    pass
    

    9. Protected Variations (Защищенные вариации)
    
        Определение: 

            Защита элементов системы от изменений в других элементах путем введения стабильных интерфейсов и абстракций.
        

        Пример: 

            Использование интерфейсов для защиты от изменений конкретных реализаций.
        
            class PaymentProcessor(ABC):
                @abstractmethod
                def process_payment(self, amount):
                    pass
            
            class PayPalPaymentProcessor(PaymentProcessor):
                def process_payment(self, amount):
                    # Code to process payment through PayPal
                    pass
            
            class StripePaymentProcessor(PaymentProcessor):
                def process_payment(self, amount):
                    # Code to process payment through Stripe
                    pass
    


Принципы GRASP помогают создавать архитектуры, которые легко изменять, расширять и поддерживать,
обеспечивая высокую качество и гибкость программного обеспечения.
