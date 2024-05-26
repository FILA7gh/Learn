

Обработка исключений в Python - это механизм, который позволяет программистам обрабатывать и управлять ошибками,
возникающими во время выполнения программы, чтобы избежать аварийного завершения приложения.


Основные конструкции для обработки исключений в Python:

    Блок try-except:

        Используется для обработки исключений. Код, который может вызвать исключение,
        помещается в блок try, а код обработки исключения - в блок except.

        Пример:

            try:
                num = int(input("Введите число: "))
                result = 10 / num
                print("Результат:", result)
            except ZeroDivisionError:
                print("Деление на ноль недопустимо.")
            except ValueError:
                print("Некорректный ввод. Введите целое число.")


    Блок try-except-finally:

        Позволяет выполнить код независимо от того, возникло исключение или нет. Блок finally используется
        для выполнения завершающих операций, например, закрытия файлов или освобождения ресурсов.

        Пример:

            try:
                file = open("example.txt", "r")
                data = file.read()
                print(data)
            except FileNotFoundError:
                print("Файл не найден.")
            finally:
                file.close()  # Файл будет закрыт независимо от исключения


    Блок try-except-else:

        Используется, когда код должен быть выполнен только в случае отсутствия исключений.
        Блок else содержит код, который будет выполнен, если в блоке try не возникло исключений.

        Пример:

            try:
                num = int(input("Введите число: "))
                result = 10 / num
            except ZeroDivisionError:
                print("Деление на ноль недопустимо.")
            else:
                print("Результат деления:", result)



В Python можно использовать вложенные блоки try-except, что позволяет более гибко обрабатывать исключения 
в различных частях кода. Вложенные блоки try-except позволяют обрабатывать исключения на разных уровнях вложенности.


Пример вложенного блока try-except:
    
    try:
        try:
            num = int(input("Введите число: "))
            result = 10 / num
            print("Результат деления на", num, ":", result)
        except ValueError:
            print("Некорректный ввод. Введите целое число.")
    except ZeroDivisionError:
        print("Деление на ноль недопустимо.")

    
    В этом примере внешний блок try-except обрабатывает возможные ошибки, возникающие внутри 
    вложенного блока try-except. Если внутренний блок сгенерирует исключение, 
    и его не будет обработано внутри, оно будет передано во внешний блок try-except.


Вложенные блоки try-except можно использовать, например, для обработки исключений на разных 
уровнях вложенности функций или для более точной обработки различных видов ошибок в разных частях кода. 
Однако следует помнить о читаемости кода и избегать избыточного использования вложенных блоков,
чтобы код оставался понятным и поддерживаемым.



Обработка исключений позволяет программистам создавать более надежные и устойчивые программы,
которые могут корректно обрабатывать различные сценарии ошибок.