Очередь — это структура данных, работающая по принципу FIFO (First In, First Out — «первым пришел, первым ушел»). 
Это означает, что элементы добавляются в конец очереди и удаляются из начала.

Основные операции с очередью

    enqueue (вставка в очередь): Добавляет элемент в конец очереди.
    dequeue (удаление из очереди): Удаляет элемент из начала очереди.
    front (передний элемент): Возвращает элемент, находящийся в начале очереди, без удаления.
    rear (задний элемент): Возвращает элемент, находящийся в конце очереди, без удаления.
    isEmpty (проверка на пустоту): Проверяет, пуста ли очередь.
    size (размер): Возвращает количество элементов в очереди.


Реализация очереди в Python

    Очередь можно реализовать с помощью списка или модуля collections.deque для более эффективного выполнения операций. 
    Рассмотрим оба подхода.

    Реализация с использованием списка
        
        class Queue:
            def __init__(self):
                self.items = []
        
            def isEmpty(self):
                return len(self.items) == 0
        
            def enqueue(self, item):
                self.items.append(item)
        
            def dequeue(self):
                if self.isEmpty():
                    raise IndexError("dequeue from empty queue")
                return self.items.pop(0)
        
            def front(self):
                if self.isEmpty():
                    raise IndexError("front from empty queue")
                return self.items[0]
        
            def rear(self):
                if self.isEmpty():
                    raise IndexError("rear from empty queue")
                return self.items[-1]
        
            def size(self):
                return len(self.items)
        
            def display(self):
                print(self.items)
        
        # Пример использования
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        q.display()  # Выведет [1, 2, 3]
        print(q.dequeue())  # Выведет 1
        q.display()  # Выведет [2, 3]



    Реализация с использованием collections.deque
        
        from collections import deque
        
        class Queue:
            def __init__(self):
                self.items = deque()
        
            def isEmpty(self):
                return len(self.items) == 0
        
            def enqueue(self, item):
                self.items.append(item)
        
            def dequeue(self):
                if self.isEmpty():
                    raise IndexError("dequeue from empty queue")
                return self.items.popleft()
        
            def front(self):
                if self.isEmpty():
                    raise IndexError("front from empty queue")
                return self.items[0]
        
            def rear(self):
                if self.isEmpty():
                    raise IndexError("rear from empty queue")
                return self.items[-1]
        
            def size(self):
                return len(self.items)
        
            def display(self):
                print(list(self.items))
        
        # Пример использования
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        q.enqueue(3)
        q.display()  # Выведет [1, 2, 3]
        print(q.dequeue())  # Выведет 1
        q.display()  # Выведет [2, 3]
    
    
Преимущества и недостатки очереди
    
    Преимущества:
    
        Простая структура: Легко реализуется и понятна.
        Очередность обработки: Гарантирует, что элементы обрабатываются в порядке их поступления.
    
    Недостатки:
    
        Ограниченная функциональность: Очереди не позволяют произвольный доступ к элементам.
        
        Имеет ограничение по производительности при использовании списка: 
            Вставка и удаление из начала списка требуют сдвига элементов, что занимает O(n) времени. 
            Использование deque из collections решает эту проблему, предоставляя O(1) время для всех операций.


Примеры задач, где очередь полезна:

    Управление задачами в операционных системах.
    Обработка запросов в сетевых приложениях.
    Службы печати и другие системы, где нужно соблюдать порядок обработки задач.
    Имитация реальных очередей (например, очередь в банке или супермаркете).

