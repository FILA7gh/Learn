

Декораторы в Python — это функции, которые принимают другую функцию в качестве аргумента и расширяют 
или изменяют её поведение без изменения её исходного кода. 
Декораторы часто используются для добавления кода, который выполняется до или после основной функции. 
Это мощный инструмент для улучшения читаемости и повторного использования кода.


Основы декораторов

    Простейший декоратор — это функция, которая принимает другую функцию и возвращает новую функцию,
    добавляя дополнительное поведение.

    Пример простого декоратора:
    
        def my_decorator(func):
            def wrapper():
                print("Something is happening before the function is called.")
                func()
                print("Something is happening after the function is called.")
            return wrapper
        
        @my_decorator
        def say_hello():
            print("Hello!")
        
        say_hello()

    Вывод:
     
        Something is happening before the function is called.
        Hello!
        Something is happening after the function is called.
        
        В этом примере my_decorator принимает функцию say_hello и возвращает новую функцию wrapper,
        которая добавляет дополнительное поведение перед и после вызова say_hello.


Декораторы с аргументами
        
        Иногда необходимо создавать декораторы, которые принимают аргументы. 
        Для этого нужно создать функцию, которая возвращает декоратор.
    
    Пример декоратора с аргументами:
     
        def repeat(num_times):
            def decorator(func):
                def wrapper(*args, **kwargs):
                    for _ in range(num_times):
                        func(*args, **kwargs)
                return wrapper
            return decorator
        
        @repeat(num_times=3)
        def say_hello(name):
            print(f"Hello, {name}!")
        
        say_hello("Alice")
        

        Вывод:
        
            Hello, Alice!
            Hello, Alice!
            Hello, Alice!


Несколько декораторов

    Функции могут иметь несколько декораторов. Они применяются в порядке их объявления сверху вниз.

    Пример с несколькими декораторами:
     
    def bold(func):
        def wrapper(*args, **kwargs):
            return f"<b>{func(*args, **kwargs)}</b>"
        return wrapper
    
    def italic(func):
        def wrapper(*args, **kwargs):
            return f"<i>{func(*args, **kwargs)}</i>"
        return wrapper
    
    @bold
    @italic
    def greet(name):
        return f"Hello, {name}!"
    
    print(greet("Alice"))
    

    Вывод:
    
        <b><i>Hello, Alice!</i></b>


Декораторы классов

    Декораторы могут также применяться к классам. Это может быть полезно 
    для регистрации классов или изменения их поведения.

    Пример декоратора класса:
     
        def register_class(cls):
            cls.is_registered = True
            return cls
        
        @register_class
        class MyClass:
            pass
        
        print(MyClass.is_registered)  # Output: True
        

Пример более сложного декоратора

    Рассмотрим пример декоратора, который замеряет время выполнения функции:
        
        import time
        
        def timer(func):
            def wrapper(*args, **kwargs):
                start_time = time.time()
                result = func(*args, **kwargs)
                end_time = time.time()
                elapsed_time = end_time - start_time
                print(f"Function {func.__name__} took {elapsed_time:.4f} seconds to complete.")
                return result
            return wrapper
        
        @timer
        def slow_function():
            time.sleep(2)
            print("Function finished.")
        
        slow_function()
        

        Вывод:
         
            Function finished.
            Function slow_function took 2.0001 seconds to complete.



Использование декораторов для проверки прав доступа

    Декораторы также можно использовать для проверки прав доступа:
     
        def require_auth(func):
            def wrapper(*args, **kwargs):
                user = kwargs.get('user')
                if user and user.get('is_authenticated'):
                    return func(*args, **kwargs)
                else:
                    raise PermissionError("User is not authenticated")
            return wrapper
        
        @require_auth
        def get_data(user):
            return "Sensitive data"
        
        # Example usage
        user_authenticated = {'is_authenticated': True}
        user_unauthenticated = {'is_authenticated': False}
        
        print(get_data(user=user_authenticated))  # Output: Sensitive data
        print(get_data(user=user_unauthenticated))  # Raises PermissionError



Заключение

    Декораторы — это мощный инструмент в Python, который позволяет добавлять дополнительные поведения 
    к функциям и классам без изменения их исходного кода. Они полезны для логгирования, проверки прав доступа, 
    замера времени выполнения, кэширования и многих других задач. Понимание и умение использовать декораторы 
    помогает писать более чистый, модульный и повторно используемый код.
