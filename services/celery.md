Celery — это асинхронная распределенная система для выполнения задач на базе очередей сообщений.
Она используется для выполнения задач в фоновом режиме, упрощения распределенных вычислений и организации планировок задач.
Основные сценарии применения Celery включают обработку фона, выполнение периодических задач,
масштабирование рабочих процессов и улучшение производительности приложений.


Основные компоненты Celery

    Брокер сообщений (Message Broker):
        Брокер сообщений используется для отправки и получения сообщений между клиентом и рабочими процессами.
        Самые популярные брокеры — это RabbitMQ и Redis.


    Рабочие процессы (Workers):
        Рабочие процессы выполняют задачи. Они могут быть распределены на нескольких серверах для масштабирования обработки.


    Задачи (Tasks):
        Задачи — это функции Python, которые выполняются асинхронно.
        Они определяются в коде вашего приложения и могут быть вызваны через Celery.


    Бэкэнд результатов (Result Backend):

        Бэкэнд результатов используется для хранения результатов выполнения задач.
        Это может быть база данных, кеш или другое хранилище.



Установка Celery

    Для установки Celery используйте pip:

        pip install celery


Настройка и использование Celery в проекте

    Пример минимального проекта с использованием Celery:

        Создание файла конфигурации Celery (celery.py):

        from celery import Celery

        app = Celery('my_app', broker='redis://localhost:6379/0', backend='redis://localhost:6379/0')

        app.conf.update(
            result_expires=3600,
        )

        @app.task
        def add(x, y):
            return x + y


    Определение задачи (tasks.py):

        from .celery import app

        @app.task
        def add(x, y):
            return x + y


    Запуск рабочего процесса:

        celery -A celery worker --loglevel=info


    Вызов задачи:

        from .tasks import add

        result = add.delay(4, 6)
        print(result.get(timeout=1))  # 10



Планирование периодических задач

    Для планирования периодических задач Celery использует расширение Celery Beat.

    Пример настройки периодической задачи:

        Обновление конфигурации Celery (celery.py):

            from celery.schedules import crontab

            app.conf.beat_schedule = {
                'add-every-30-seconds': {
                    'task': 'tasks.add',
                    'schedule': 30.0,
                    'args': (16, 16)
                },
                'add-at-specific-time': {
                    'task': 'tasks.add',
                    'schedule': crontab(hour=7, minute=30, day_of_week=1),
                    'args': (16, 16),
                },
            }


        Запуск Celery Beat:

            celery -A celery beat



Преимущества использования Celery

    Асинхронность: Позволяет выполнять задачи в фоновом режиме без блокировки основного потока выполнения.
    Масштабируемость: Возможность распределения рабочих процессов на нескольких серверах для повышения производительности.
    Гибкость: Поддержка различных брокеров сообщений и бэкэндов для хранения результатов.
    Планирование задач: Встроенная поддержка планирования периодических задач.


Советы и лучшие практики

    Используйте надежный брокер сообщений: RabbitMQ или Redis — популярные и надежные варианты.

    Следите за производительностью: 
        Мониторинг рабочих процессов и брокеров сообщений помогает своевременно выявлять и решать проблемы.

    Безопасность: Убедитесь, что ваши брокеры сообщений и бэкэнды защищены от несанкционированного доступа.

    Документирование задач: 
        Пишите документацию для задач, чтобы другие разработчики могли легко понимать их назначение и использование.


Celery — мощный инструмент для организации асинхронной работы и планирования задач в приложениях.