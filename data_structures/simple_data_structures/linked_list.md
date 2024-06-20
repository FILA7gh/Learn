Связанный список — это динамическая структура данных, состоящая из элементов (узлов), 
каждый из которых содержит данные и ссылку (указатель) на следующий узел в списке. 
В отличие от массивов, связанные списки не требуют непрерывного блока памяти, 
что делает их эффективными для частых вставок и удалений элементов.


Типы связанных списков

    Односвязный список:
        Каждый узел содержит данные и указатель на следующий узел.
        
        [data|next] -> [data|next] -> [data|next] -> None

    
    Двусвязный список:
        Каждый узел содержит данные, указатель на следующий и предыдущий узлы.
        
        None <- [prev|data|next] <-> [prev|data|next] <-> [prev|data|next] -> None
        
        
    Кольцевой связанный список:
        Односвязный или двусвязный список, у которого последний узел указывает на первый, образуя кольцо.
    
        [data|next] -> [data|next] -> [data|next] --+
           ^                                       |
           +---------------------------------------+


Реализация односвязного списка в Python
 
    class Node:
        def __init__(self, data):
            self.data = data
            self.next = None
    
    class SinglyLinkedList:
        def __init__(self):
            self.head = None
    
        def append(self, data):
            new_node = Node(data)
            if not self.head:
                self.head = new_node
                return
            last = self.head
            while last.next:
                last = last.next
            last.next = new_node
    
        def prepend(self, data):
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
    
        def delete(self, key):
            temp = self.head
            if temp and temp.data == key:
                self.head = temp.next
                temp = None
                return
            prev = None
            while temp and temp.data != key:
                prev = temp
                temp = temp.next
            if temp is None:
                return
            prev.next = temp.next
            temp = None
    
        def display(self):
            elems = []
            current = self.head
            while current:
                elems.append(current.data)
                current = current.next
            print(elems)
    
    # Пример использования
    sll = SinglyLinkedList()
    sll.append(1)
    sll.append(2)
    sll.prepend(0)
    sll.display()  # Выведет [0, 1, 2]
    sll.delete(1)
    sll.display()  # Выведет [0, 2]


Преимущества и недостатки связанных списков

    Преимущества:
    
        Динамическое управление памятью: Размер списка может изменяться по мере необходимости.
        
        Эффективные вставки и удаления: Вставка и удаление элементов выполняются за O(1) время при условии, 
                                        что у вас есть ссылка на узел, где происходит операция.
    
    
    Недостатки:
    
        Медленный доступ по индексу: Для доступа к элементу нужно последовательно пройти от начала списка 
                                     до нужного узла, что занимает O(n) времени.

        Дополнительная память: Каждый узел требует дополнительной памяти для хранения указателя.


Примеры задач, где связанный список полезен:

    Реализация очередей и стеков.
    Управление памятью (например, в системах управления памятью).
    Создание сложных динамических структур данных (например, графов, деревьев).

