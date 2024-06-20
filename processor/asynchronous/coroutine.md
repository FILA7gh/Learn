
Корутины в Python — это генераторы, которые могут приостанавливать и возобновлять свое выполнение,
что позволяет писать асинхронный код. Корутины позволяют выполнять многозадачность без необходимости использования
потоков или процессов, что делает их эффективным инструментом для ввода-вывода и других операций,
которые могут блокировать выполнение программы.


Основные понятия и использование корутин

    Асинхронные функции и async:
        Асинхронные функции определяются с использованием ключевого слова async, и они возвращают корутины.

        async def my_coroutine():
            print("Start coroutine")
            await asyncio.sleep(1)
            print("End coroutine")


    Ключевое слово await:
        await используется для ожидания завершения асинхронной операции,
        что позволяет корутине приостановиться до завершения этой операции.

        async def fetch_data():
            data = await some_async_function()
            return data


    Использование asyncio для запуска корутин:
        Модуль asyncio предоставляет цикл событий и функции для работы с корутинами.

        import asyncio

        async def main():
            print("Hello...")
            await asyncio.sleep(1)
            print("...world!")

        asyncio.run(main())


    Асинхронные задачи:
        asyncio.create_task() используется для запуска корутины в виде задачи,
        которая выполняется параллельно с другими задачами.

        import asyncio

        async def say_after(delay, message):
            await asyncio.sleep(delay)
            print(message)

        async def main():
            task1 = asyncio.create_task(say_after(1, "Hello"))
            task2 = asyncio.create_task(say_after(2, "World"))

            print("Tasks created")
            await task1
            await task2

        asyncio.run(main())


    Асинхронные генераторы:
        Асинхронные генераторы определяются с использованием async def и yield.

        async def async_generator():
            for i in range(3):
                await asyncio.sleep(1)
                yield i

        async def main():
            async for number in async_generator():
                print(number)

        asyncio.run(main())


    Асинхронные итераторы:
        Асинхронные итераторы позволяют использовать async for для асинхронного перебора.

        class AsyncIterator:
            def __init__(self):
                self.i = 0

            def __aiter__(self):
                return self

            async def __anext__(self):
                if self.i >= 3:
                    raise StopAsyncIteration
                self.i += 1
                await asyncio.sleep(1)
                return self.i

        async def main():
            async for number in AsyncIterator():
                print(number)

        asyncio.run(main())


    Асинхронные контекстные менеджеры:
        Асинхронные контекстные менеджеры позволяют использовать async with.

        class AsyncContextManager:
            async def __aenter__(self):
                print("Entering context")
                return self

            async def __aexit__(self, exc_type, exc, tb):
                print("Exiting context")

        async def main():
            async with AsyncContextManager():
                print("Inside context")

        asyncio.run(main())



Примеры реального использования

    Асинхронный HTTP-запрос:
        Использование библиотеки aiohttp для выполнения асинхронных HTTP-запросов.

        import aiohttp
        import asyncio

        async def fetch(session, url):
            async with session.get(url) as response:
                return await response.text()

        async def main():
            async with aiohttp.ClientSession() as session:
                html = await fetch(session, 'http://example.com')
                print(html)

        asyncio.run(main())


    Асинхронное чтение и запись файлов:
        Использование библиотеки aiofiles для асинхронного чтения и записи файлов.
        
        import aiofiles
        import asyncio
    
        async def write_file():
            async with aiofiles.open('example.txt', mode='w') as f:
                await f.write('Hello, world!')
    
        async def read_file():
            async with aiofiles.open('example.txt', mode='r') as f:
                contents = await f.read()
                print(contents)
    
        async def main():
            await write_file()
            await read_file()
    
        asyncio.run(main())


Заключение
    
    Корутины и асинхронное программирование в Python позволяют эффективно обрабатывать параллельные задачи,
    особенно когда дело касается ввода-вывода. Использование асинхронных функций, 
    генераторов и контекстных менеджеров помогает улучшить производительность и отзывчивость приложений, 
    избегая блокировки главного потока выполнения.
