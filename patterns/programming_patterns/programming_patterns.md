
Паттерны программирования, или шаблоны проектирования (design patterns), представляют собой типовые решения
часто встречающихся проблем в программировании. Они являются проверенными на практике и повторно используемыми решениями,
которые помогают разработчикам создавать более гибкие, масштабируемые и поддерживаемые программные системы.


Классификация паттернов программирования

Паттерны проектирования делятся на три основные категории:

    Порождающие паттерны (Creational Patterns):
      
        Фабричный метод (Factory Method): Определяет интерфейс для создания объектов, но позволяет подклассам изменять тип создаваемых объектов.
      
        Абстрактная фабрика (Abstract Factory): Создаёт семейства связанных или зависимых объектов без указания их конкретных классов.
      
        Строитель (Builder): Разделяет процесс создания сложного объекта от его представления, 
                             так что один и тот же процесс создания может приводить к разным представлениям.
      
        Прототип (Prototype): Создаёт новые объекты, копируя существующие.
      
        Одиночка (Singleton): Гарантирует, что у класса есть только один экземпляр, и предоставляет глобальную точку доступа к нему.


    Структурные паттерны (Structural Patterns):

        Адаптер (Adapter): Преобразует интерфейс класса в другой интерфейс, который ожидают клиенты.

        Мост (Bridge): Разделяет абстракцию и реализацию, позволяя им изменяться независимо.

        Компоновщик (Composite): Объединяет объекты в древовидную структуру для представления иерархий часть-целое.

        Декоратор (Decorator): Динамически добавляет новые обязанности объекту.

        Фасад (Facade): Предоставляет унифицированный интерфейс для набора интерфейсов в подсистеме.

        Легковес (Flyweight): Позволяет использовать большое количество мелких объектов эффективно, разделяя общий внутренний статус.

        Заместитель (Proxy): Предоставляет суррогат или заместитель для другого объекта, чтобы контролировать доступ к нему.


    Паттерны поведения (Behavioral Patterns):

        Цепочка обязанностей (Chain of Responsibility): Передаёт запрос по цепочке обработчиков, где каждый обработчик решает, 
                                                        обработать ли запрос или передать его дальше.

        Команда (Command): Инкапсулирует запрос как объект, позволяя параметризовать клиентов с различными запросами, очередями или логами запросов.

        Итератор (Iterator): Предоставляет способ последовательного доступа ко всем элементам агрегатного объекта, 
                             не раскрывая его внутреннего представления.

        Посредник (Mediator): Определяет объект, который инкапсулирует взаимодействие множества объектов.

        Снимок (Memento): Сохраняет и восстанавливает состояние объекта, не раскрывая его внутреннего представления.

        Наблюдатель (Observer): Определяет зависимость типа "один ко многим" между объектами, так что при 
                                изменении состояния одного объекта все зависимые объекты уведомляются и обновляются автоматически.

        Состояние (State): Позволяет объекту изменять своё поведение в зависимости от его состояния.

        Стратегия (Strategy): Определяет семейство алгоритмов, инкапсулирует каждый из них и делает их взаимозаменяемыми.

        Шаблонный метод (Template Method): Определяет скелет алгоритма в методе, оставляя некоторые шаги подклассам.

        Посетитель (Visitor): Операции, которые применяются к элементам структуры объектов, не изменяя их классы.



Примеры использования паттернов

    Порождающие паттерны
        
        Пример: Одиночка (Singleton)
            
            class Singleton:
                _instance = None
            
                def __new__(cls):
                    if cls._instance is None:
                        cls._instance = super(Singleton, cls).__new__(cls)
                    return cls._instance
            
            # Использование
            s1 = Singleton()
            s2 = Singleton()
            print(s1 is s2)  # True

    
    Структурные паттерны
    
        Пример: Адаптер (Adapter)
                    
            class Target:
                def request(self):
                    return "Target request"
            
            class Adaptee:
                def specific_request(self):
                    return "Adaptee specific request"
            
            class Adapter(Target):
                def __init__(self, adaptee):
                    self.adaptee = adaptee
            
                def request(self):
                    return self.adaptee.specific_request()
            
            # Использование
            adaptee = Adaptee()
            adapter = Adapter(adaptee)
            print(adapter.request())  # Adaptee specific request
            
                
    Паттерны поведения
    
    Пример: Наблюдатель (Observer)
  
    
        class Subject:
            def __init__(self):
                self._observers = []
        
            def attach(self, observer):
                self._observers.append(observer)
        
            def detach(self, observer):
                self._observers.remove(observer)
        
            def notify(self):
                for observer in self._observers:
                    observer.update()
        
        class ConcreteSubject(Subject):
            def __init__(self, state):
                super().__init__()
                self._state = state
        
            @property
            def state(self):
                return self._state
        
            @state.setter
            def state(self, state):
                self._state = state
                self.notify()
        
        class Observer:
            def update(self):
                pass
        
        class ConcreteObserver(Observer):
            def __init__(self, subject):
                self._subject = subject
        
            def update(self):
                print(f"Observer: subject's state is {self._subject.state}")
        
        # Использование
        subject = ConcreteSubject(0)
        observer1 = ConcreteObserver(subject)
        observer2 = ConcreteObserver(subject)
        subject.attach(observer1)
        subject.attach(observer2)
        
        subject.state = 1
        # Output:
        # Observer: subject's state is 1
        # Observer: subject's state is 1



Заключение

    Паттерны программирования предоставляют решения для типичных задач проектирования программных систем. 
    Они помогают разработчикам создавать более гибкий и легко поддерживаемый код. 
    Изучение и использование паттернов позволяет улучшить архитектуру программ и повысить качество программного обеспечения.
