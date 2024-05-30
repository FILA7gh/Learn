

Конструкция if __name__ == "__main__": в Python используется для проверки того, является ли скрипт основным модулем,
который выполняется. Это позволяет определить, был ли скрипт запущен напрямую или импортирован в другой модуль.
Если скрипт запущен напрямую, то значение переменной __name__ будет равно "__main__",
и код внутри этого блока будет выполнен. Если скрипт импортирован как модуль в другой файл,
то код внутри этого блока выполнен не будет.


Это полезно для создания скриптов, которые могут как выполняться самостоятельно, так и использоваться в качестве модулей.


Пример использования:

    def main():
        print("Этот код выполняется только при запуске скрипта напрямую.")
    
    if __name__ == "__main__":
        main()


Зачем использовать if __name__ == "__main__":

    Тестирование и отладка: Позволяет включить тестовый код, который не будет выполнен при импорте модуля.

    
    def test_function():
        print("Функция для тестирования.")
    
    if __name__ == "__main__":
        test_function()


    Создание многоразовых модулей: 
    
        Код может быть использован как библиотека, без выполнения дополнительных действий при импорте.
     
        def useful_function():
            print("Полезная функция!")
    
        if __name__ == "__main__":
            # Код для демонстрации работы функции
            useful_function()
    

    Организация кода: 
    
        Позволяет структурировать код, отделяя основную логику выполнения от определений функций и классов.



Пример использования с аргументами командной строки

    Если скрипт принимает аргументы командной строки, это также удобно размещать внутри if __name__ == "__main__":.

    import sys
    
    def main(args):
        print(f"Аргументы командной строки: {args}")
    
    if __name__ == "__main__":
        main(sys.argv[1:])


Пример более сложного кода

    Рассмотрим более сложный пример, включающий функции и классы:
        
        import math
        
        class Circle:
            def __init__(self, radius):
                self.radius = radius
        
            def area(self):
                return math.pi * self.radius ** 2
        
        def main():
            circle = Circle(5)
            print(f"Площадь круга: {circle.area()}")
        
        if __name__ == "__main__":
            main()


В этом примере класс Circle и функция main определены в модуле. Когда модуль запускается напрямую, 
создается экземпляр Circle и вычисляется его площадь.


Заключение

Конструкция if __name__ == "__main__": является стандартным и рекомендованным способом структурирования кода в Python,
обеспечивая гибкость и многоразовость модулей. Она позволяет использовать один и тот же файл как исполняемый скрипт 
и как импортируемый модуль, обеспечивая при этом правильное выполнение кода в зависимости от контекста.