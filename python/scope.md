

Области видимости в Python

В Python области видимости (scope) определяют контекст, в котором переменные и имена функций могут быть доступными.
Понимание областей видимости важно для управления доступом к переменным и избегания конфликтов имен.


Типы областей видимости

    Локальная область видимости (Local Scope)

    Область видимости вложенных функций (Enclosing Scope)

    Глобальная область видимости (Global Scope)

    Область видимости встроенных имен (Built-in Scope)


    Эти области видимости можно запомнить с помощью акронима LEGB (Local, Enclosing, Global, Built-in).


Локальная область видимости (Local Scope)

    Переменные, объявленные внутри функции, находятся в локальной области видимости и доступны только внутри этой функции.

    def my_function():
        local_var = 10
        print(local_var)  # 10

    my_function()
    # print(local_var)  # Ошибка, переменная local_var не доступна вне функции


Область видимости вложенных функций (Enclosing Scope)

    Область видимости вложенных функций касается переменных, которые объявлены
    в объемлющей (outer) функции и доступны во вложенных (inner) функциях.

    def outer_function():
        enclosing_var = 'outer'

        def inner_function():
            print(enclosing_var)  # Доступ к enclosing_var из внешней функции

        inner_function()

    outer_function()  # 'outer'


Глобальная область видимости (Global Scope)

    Переменные, объявленные на уровне модуля (вне всех функций), находятся в
    глобальной области видимости и доступны в любом месте модуля.

    global_var = 'global'

    def my_function():
        print(global_var)  # Доступ к глобальной переменной внутри функции

    my_function()  # 'global'
    print(global_var)  # 'global'


    Использование ключевого слова global

        Чтобы изменить глобальную переменную внутри функции, нужно использовать ключевое слово global.

        counter = 0

        def increment_counter():
            global counter
            counter += 1

        increment_counter()
        print(counter)  # 1


Область видимости встроенных имен (Built-in Scope)

    Эта область видимости содержит встроенные функции и исключения Python.
    Эти имена всегда доступны, если они не переопределены в локальной или глобальной области видимости.

    print(len("Hello"))  # Вызов встроенной функции len()


Примеры для лучшего понимания
    
    Пример с локальной и глобальной областью видимости
    
        x = 25
        
        def my_function():
            x = 50
            print(x)  # Локальная переменная x
        
        my_function()  # 50
        print(x)  # Глобальная переменная x: 25

    
    Пример с вложенными функциями
    
        def outer_function():
            x = 'outer x'
        
            def inner_function():
                nonlocal x
                x = 'inner x'
                print(x)  # 'inner x'
        
            inner_function()
            print(x)  # 'inner x', так как nonlocal изменил значение в объемлющей области
        
        outer_function()


    Пример с global и nonlocal
        
        x = 'global x'
        
        def outer_function():
            x = 'outer x'
        
            def inner_function():
                global x
                x = 'inner x'
        
            inner_function()
            print(x)  # 'outer x', так как global изменил глобальную переменную
        
        outer_function()
        print(x)  # 'inner x', глобальная переменная была изменена



Заключение

    Понимание областей видимости важно для управления переменными и избегания ошибок при программировании. 
    Используйте локальные переменные для временных данных, глобальные переменные — для данных, 
    которые должны быть доступны во всем модуле, и внимательно работайте с вложенными функциями 
    для управления доступом к переменным из внешних функций.
