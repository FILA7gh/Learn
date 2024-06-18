Стек (stack) — это структура данных, работающая по принципу LIFO (Last In, First Out — «последним пришел, первым ушел»). 
Это означает, что последний добавленный элемент будет первым удалён.

Основные операции со стеком

    push (вставка): Добавляет элемент на вершину стека.
    pop (удаление): Удаляет элемент с вершины стека и возвращает его.
    peek (или top, верхний элемент): Возвращает элемент на вершине стека, не удаляя его.
    isEmpty (проверка на пустоту): Проверяет, пуст ли стек.
    size (размер): Возвращает количество элементов в стеке.


Реализация стека в Python

    Стек можно реализовать с помощью списка или модуля collections.deque.

    Реализация с использованием списка
        
        class Stack:
            def __init__(self):
                self.items = []
        
            def isEmpty(self):
                return len(self.items) == 0
        
            def push(self, item):
                self.items.append(item)
        
            def pop(self):
                if self.isEmpty():
                    raise IndexError("pop from empty stack")
                return self.items.pop()
        
            def peek(self):
                if self.isEmpty():
                    raise IndexError("peek from empty stack")
                return self.items[-1]
        
            def size(self):
                return len(self.items)
        
            def display(self):
                print(self.items)
        
        # Пример использования
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.display()  # Выведет [1, 2, 3]
        print(stack.pop())  # Выведет 3
        stack.display()  # Выведет [1, 2]
        print(stack.peek())  # Выведет 2
        stack.display()  # Выведет [1, 2]


    Реализация с использованием collections.deque
    
        from collections import deque
        
        class Stack:
            def __init__(self):
                self.items = deque()
        
            def isEmpty(self):
                return len(self.items) == 0
        
            def push(self, item):
                self.items.append(item)
        
            def pop(self):
                if self.isEmpty():
                    raise IndexError("pop from empty stack")
                return self.items.pop()
        
            def peek(self):
                if self.isEmpty():
                    raise IndexError("peek from empty stack")
                return self.items[-1]
        
            def size(self):
                return len(self.items)
        
            def display(self):
                print(list(self.items))
        
        # Пример использования
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        stack.display()  # Выведет [1, 2, 3]
        print(stack.pop())  # Выведет 3
        stack.display()  # Выведет [1, 2]
        print(stack.peek())  # Выведет 2
        stack.display()  # Выведет [1, 2]


Преимущества и недостатки стека

    Преимущества:
    
        Простота: Легко реализуется и понятна.
        Эффективность: Операции добавления и удаления выполняются за O(1) время.
    
    Недостатки:
    
        Ограниченная функциональность: Нет произвольного доступа к элементам, доступен только верхний элемент.
        
        Потенциальный риск переполнения: При использовании ограниченной памяти или фиксированных размеров стека 
                                         (в системах с ограниченными ресурсами).
    
    
Примеры задач, где стек полезен:

    Управление вызовами функций (стек вызовов).
    Обратный порядок выполнения задач.
    Обратный порядок строки или списка.
    Реализация алгоритмов обхода деревьев и графов (например, глубинный обход — DFS).
    Парсинг выражений (например, обратная польская нотация).

