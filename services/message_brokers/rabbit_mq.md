RabbitMQ — это популярная система управления сообщениями (Message Broker), которая реализует протокол AMQP
(Advanced Message Queuing Protocol). Она позволяет приложениям общаться между собой посредством обмена сообщениями,
что делает ее идеальной для построения асинхронных, распределенных и масштабируемых систем.


Основные компоненты RabbitMQ

    Producer (Производитель):

        Производитель отправляет сообщения в RabbitMQ.


    Queue (Очередь):

        Очередь — это буфер, куда RabbitMQ сохраняет сообщения. Сообщения остаются в очереди, пока их не заберет Consumer.


    Consumer (Потребитель):

        Потребитель получает сообщения из очереди и обрабатывает их.


    Exchange (Обменник):

        Обменник принимает сообщения от производителя и направляет их в одну или несколько очередей на основе правил привязки (Binding Rules).


    Binding (Привязка):

        Привязка связывает очередь с обменником с определенным правилом, которое решает, какие сообщения должны быть отправлены в очередь.


Типы обменников

    Direct Exchange:

        Сообщение направляется в очередь с конкретным ключом маршрутизации (routing key).


    Fanout Exchange:

        Сообщение направляется во все очереди, привязанные к этому обменнику.


    Topic Exchange:

        Сообщение направляется в очереди на основе шаблонов ключей маршрутизации (например, *.info, kern.*).


    Headers Exchange:

        Сообщение направляется в очереди на основе заголовков сообщений.


Установка RabbitMQ

    Установка на Ubuntu:

        # Обновление пакетов
        sudo apt update

        # Установка RabbitMQ
        sudo apt install rabbitmq-server -y

        # Запуск службы RabbitMQ
        sudo systemctl start rabbitmq-server

        # Включение службы при запуске системы
        sudo systemctl enable rabbitmq-server


    Включение веб-интерфейса управления RabbitMQ:

        sudo rabbitmq-plugins enable rabbitmq_management

        Веб-интерфейс будет доступен по адресу: http://localhost:15672/


Основные команды управления RabbitMQ

    Запуск RabbitMQ:

        sudo systemctl start rabbitmq-server


    Остановка RabbitMQ:

        sudo systemctl stop rabbitmq-server


    Перезапуск RabbitMQ:

        sudo systemctl restart rabbitmq-server



Использование RabbitMQ с Python (pika)

    pika — это популярная библиотека Python для работы с RabbitMQ.

    Установка pika:

        pip install pika


    Пример использования RabbitMQ с Python

        Отправка сообщения (Producer):

            import pika

            # Установка соединения с RabbitMQ
            connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
            channel = connection.channel()

            # Объявление очереди
            channel.queue_declare(queue='hello')

            # Отправка сообщения
            channel.basic_publish(exchange='',
                                  routing_key='hello',
                                  body='Hello World!')
            print(" [x] Sent 'Hello World!'")

            # Закрытие соединения
            connection.close()


        Получение сообщения (Consumer):

            import pika

            # Установка соединения с RabbitMQ
            connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
            channel = connection.channel()

            # Объявление очереди
            channel.queue_declare(queue='hello')

            # Callback функция для обработки сообщений
            def callback(ch, method, properties, body):
                print(f" [x] Received {body}")

            # Установка потребителя
            channel.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)

            print(' [*] Waiting for messages. To exit press CTRL+C')
            channel.start_consuming()


Управление пользователями и разрешениями

    Создание нового пользователя:

        sudo rabbitmqctl add_user myuser mypassword


    Назначение пользователя администратором:

        sudo rabbitmqctl set_user_tags myuser administrator


    Назначение разрешений пользователю:

        sudo rabbitmqctl set_permissions -p / myuser ".*" ".*" ".*"


Преимущества RabbitMQ

    Надежность: Поддержка подтверждений доставки, надежных очередей и механизма повторной попытки доставки.
    Масштабируемость: Возможность масштабирования как в горизонтальном, так и в вертикальном направлении.
    Гибкость: Поддержка различных типов обменников и широкого спектра сценариев использования.
    Сообщество и поддержка: Широкая экосистема, множество библиотек и инструментов для интеграции.


Заключение

    RabbitMQ является мощным инструментом для построения распределенных систем и обработки сообщений.
    Он позволяет организовать надежную и масштабируемую систему обмена сообщениями между различными компонентами приложения.
