
Работа с файлами в Python

Работа с файлами — одна из основных задач в программировании.
Python предоставляет удобные инструменты для открытия, чтения, записи и закрытия файлов.


Открытие и закрытие файлов

    Для работы с файлами используется функция open(), которая возвращает файловый объект.
    Файл нужно закрывать после завершения работы с ним с помощью метода close().


    Пример

        # Открытие файла для чтения (режим 'r')
        file = open('example.txt', 'r')
        # Чтение содержимого файла
        content = file.read()
        print(content)
        # Закрытие файла
        file.close()


Режимы открытия файлов

    'r' — чтение (по умолчанию, если не указан режим).

    'w' — запись (создает новый файл или обрезает существующий).

    'a' — добавление (открывает файл для записи в конец).

    'b' — бинарный режим (используется в сочетании с другими режимами, например, 'rb' или 'wb').

    'x' — эксклюзивное создание (создает новый файл, если файл уже существует, вызывает ошибку).

    't' — текстовый режим (по умолчанию, используется в сочетании с другими режимами, например, 'rt' или 'wt').


Чтение из файла

    Чтение всего содержимого файла:

        with open('example.txt', 'r') as file:
            content = file.read()
            print(content)


    Чтение файла построчно:

        with open('example.txt', 'r') as file:
            for line in file:
                print(line.strip())  # .strip() удаляет символы новой строки


    Чтение определенного количества символов:

        with open('example.txt', 'r') as file:
            content = file.read(10)  # Чтение первых 10 символов
            print(content)


    Чтение всех строк в список:

        with open('example.txt', 'r') as file:
            lines = file.readlines()
            for line in lines:
                print(line.strip())


Запись в файл

    Запись строки в файл:

        with open('example.txt', 'w') as file:
            file.write("Hello, World!\n")


    Запись нескольких строк в файл:

        with open('example.txt', 'w') as file:
            lines = ["First line\n", "Second line\n", "Third line\n"]
            file.writelines(lines)


    Добавление строки в конец файла:

        with open('example.txt', 'a') as file:
            file.write("This is an appended line.\n")


Работа с бинарными файлами

    Для работы с бинарными файлами используйте режимы 'rb', 'wb' или 'ab'.

    Чтение бинарного файла:

        with open('example.jpg', 'rb') as file:
            data = file.read()
            print(data)


    Запись в бинарный файл:

        with open('example.bin', 'wb') as file:
            data = b'\x00\x01\x02\x03'
            file.write(data)


Менеджер контекста with

    Использование менеджера контекста with для работы с файлами автоматически закрывает файл после
    завершения работы с ним, даже если возникло исключение.


    with open('example.txt', 'r') as file:
        content = file.read()
        print(content)


    Чтение из одного файла и запись в другой:

        input_file = 'input.txt'
        output_file = 'output.txt'

        with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
            for line in infile:
                outfile.write(line.upper())


    Проверка существования файла и создание нового файла:

        import os

        file_path = 'example.txt'

        if not os.path.exists(file_path):
            with open(file_path, 'x') as file:
                file.write("This is a newly created file.\n")
        else:
            print(f"File {file_path} already exists.")



Заключение

    Работа с файлами в Python — это мощный инструмент для чтения, записи и обработки данных. 
    Используя режимы открытия файлов, менеджер контекста with и различные методы чтения и записи, 
    вы можете эффективно управлять файлами в ваших приложениях.
