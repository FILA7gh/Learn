
В Python с использованием библиотеки asyncio задачи (tasks) позволяют выполнять корутины параллельно. 
Это мощный инструмент для управления асинхронными операциями, позволяющий запускать, 
приостанавливать и возобновлять выполнение корутин. 


Вот основные аспекты работы с задачами в asyncio:

    Основные концепции и примеры
    
        Создание задач:
            Используйте asyncio.create_task() для запуска корутины в виде задачи, 
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
            

    Ожидание завершения задач:
        Вы можете ожидать завершения задач, используя await, 
        что приостанавливает выполнение до тех пор, пока задача не завершится.
     
        async def task_example():
            task = asyncio.create_task(say_after(1, "Hello"))
            await task
        

    Запуск нескольких задач параллельно:
        asyncio.gather() позволяет запускать несколько задач параллельно и ожидать их завершения.
    
        import asyncio
        
        async def say_after(delay, message):
            await asyncio.sleep(delay)
            print(message)
        
        async def main():
            await asyncio.gather(
                say_after(1, "Hello"),
                say_after(2, "World")
            )
        
        asyncio.run(main())
        

    Отмена задач:
        Задачи могут быть отменены с помощью метода cancel(), что приводит к генерации исключения asyncio.CancelledError.
     
        async def long_running_task():
            try:
                while True:
                    print("Running...")
                    await asyncio.sleep(1)
            except asyncio.CancelledError:
                print("Task was cancelled")
        
        async def main():
            task = asyncio.create_task(long_running_task())
            await asyncio.sleep(3)
            task.cancel()
            await task
        
        asyncio.run(main())
    

    Ожидание завершения всех задач с asyncio.wait():
        asyncio.wait() может быть использован для ожидания завершения множества задач.
     
        import asyncio
        
        async def say_after(delay, message):
            await asyncio.sleep(delay)
            print(message)
        
        async def main():
            tasks = [
                asyncio.create_task(say_after(1, "Hello")),
                asyncio.create_task(say_after(2, "World"))
            ]
            await asyncio.wait(tasks)
        
        asyncio.run(main())
    

    Получение результатов задач:
        Используя asyncio.gather(), вы можете получить результаты выполнения задач.
     
        import asyncio
        
        async def add(a, b):
            await asyncio.sleep(1)
            return a + b
        
        async def main():
            result1, result2 = await asyncio.gather(
                add(1, 2),
                add(3, 4)
            )
            print(result1)  # Output: 3
            print(result2)  # Output: 7
        
        asyncio.run(main())
    

    Обработка исключений в задачах:
        Исключения, возникающие внутри задач, могут быть обработаны как обычно.
     
        import asyncio
    
        async def faulty_task():
            await asyncio.sleep(1)
            raise ValueError("An error occurred")
    
        async def main():
            task = asyncio.create_task(faulty_task())
            try:
                await task
            except ValueError as e:
                print(f"Caught an exception: {e}")
    
        asyncio.run(main())



Практические примеры

    Асинхронный веб-скрейпер:
        Пример использования задач для асинхронного веб-скрейпинга с использованием библиотеки aiohttp.
        
        import aiohttp
        import asyncio
        
        async def fetch(session, url):
            async with session.get(url) as response:
                return await response.text()
        
        async def main(urls):
            async with aiohttp.ClientSession() as session:
                tasks = [asyncio.create_task(fetch(session, url)) for url in urls]
                results = await asyncio.gather(*tasks)
                for result in results:
                    print(result)
        
        urls = ['http://example.com', 'http://example.org']
        asyncio.run(main(urls))


Асинхронная работа с базой данных:

    Пример использования задач для выполнения нескольких запросов к базе данных параллельно.

    import asyncio
    import asyncpg

    async def fetch_data(query):
        conn = await asyncpg.connect(user='user', password='password', database='test', host='127.0.0.1')
        data = await conn.fetch(query)
        await conn.close()
        return data

    async def main():
        queries = ["SELECT * FROM table1", "SELECT * FROM table2"]
        tasks = [asyncio.create_task(fetch_data(query)) for query in queries]
        results = await asyncio.gather(*tasks)
        for result in results:
            print(result)

    asyncio.run(main())


Заключение

    Задачи (tasks) в asyncio обеспечивают мощный способ выполнения асинхронных операций параллельно. 
    Они позволяют эффективно управлять выполнением корутин, обрабатывать результаты и исключения, 
    а также отменять задачи по мере необходимости. Использование задач в асинхронном программировании 
    помогает улучшить производительность и отзывчивость приложений, 
    особенно при работе с вводом-выводом и другими асинхронными операциями.