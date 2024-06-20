Docker Compose — это инструмент для определения и управления многоконтейнерными Docker-приложениями.
С его помощью можно описывать конфигурации контейнеров в файле docker-compose.yml,
а затем запускать и управлять ими с помощью одной команды. Docker Compose упрощает процесс разработки, тестирования
и развертывания приложений, состоящих из нескольких контейнеров.


Основные концепции Docker Compose:

    Сервисы (Services):
        Сервисы представляют собой контейнеры в Compose. Каждый сервис определяет контейнер, 
        который будет запущен, и его конфигурацию.


    Тома (Volumes):
        Тома используются для хранения данных, которые должны сохраняться между запусками контейнеров.


    Сети (Networks):
        Сети позволяют контейнерам общаться друг с другом.


Основные команды Docker Compose:

    Запуск всех сервисов, определенных в docker-compose.yml:

        docker-compose up


    Запуск всех сервисов в фоновом режиме (detached mode):

        docker-compose up -d


    Остановка и удаление всех контейнеров и сетей, созданных с помощью Docker Compose:

        docker-compose down


    Показать статус всех контейнеров:

        docker-compose ps


    Просмотр логов всех контейнеров:

        docker-compose logs


    Запуск команды внутри контейнера:

        docker-compose exec <service_name> <command>


Пример использования Docker Compose:

    Предположим, у нас есть приложение на Flask и база данных PostgreSQL. Мы хотим запустить их вместе, 
    используя Docker Compose.

    Структура проекта:

        myapp/
        │
        ├── app.py
        ├── requirements.txt
        ├── Dockerfile
        └── docker-compose.yml

        app.py:

            from flask import Flask
            import psycopg2

            app = Flask(__name__)

            @app.route('/')
            def hello_world():
                return 'Hello, World!'

            if __name__ == '__main__':
                app.run(host='0.0.0.0')


        requirements.txt:

            Flask==2.0.1
            psycopg2-binary==2.9.1


        Dockerfile:

            FROM python:3.9-slim

            WORKDIR /app

            COPY requirements.txt .

            RUN pip install --no-cache-dir -r requirements.txt

            COPY . .

            EXPOSE 5000

            CMD ["python", "app.py"]


        docker-compose.yml:

            version: '3.8'

            services:
              web:
                build: .
                ports:
                  - "5000:5000"
                depends_on:
                  - db

              db:
                image: postgres:13
                environment:
                  POSTGRES_USER: example
                  POSTGRES_PASSWORD: example
                  POSTGRES_DB: example
                volumes:
                  - pgdata:/var/lib/postgresql/data
            
            volumes:
              pgdata:


Пошаговое объяснение docker-compose.yml:

    version:
        Определяет версию синтаксиса Docker Compose. В данном случае используется версия 3.8.

    
    services:
        Определяет два сервиса: web и db.

        web:

            build: Определяет, что нужно собрать образ из текущей директории (.).
            ports: Пробрасывает порт 5000 на хост-машине на порт 5000 внутри контейнера.
            depends_on: Указывает, что сервис web зависит от сервиса db, и он будет запущен после запуска db.


        db:

            image: Использует официальный образ PostgreSQL версии 13.
            environment: Определяет переменные окружения для настройки базы данных.
            volumes: Монтирует том pgdata в директорию /var/lib/postgresql/data внутри контейнера
                     для постоянного хранения данных.


    volumes:
        Определяет том pgdata, который будет использоваться для хранения данных PostgreSQL.


Запуск приложения с Docker Compose:

    Запуск всех сервисов:
        
        docker-compose up

        Эта команда создаст и запустит контейнеры для каждого сервиса, определенного в docker-compose.yml.

    
    Доступ к приложению:
        Приложение Flask будет доступно по адресу http://localhost:5000.


    Остановка и удаление всех сервисов:
    
        docker-compose down
    
        Эта команда остановит и удалит все контейнеры, сети и тома, созданные Docker Compose.



Использование переменных окружения в Docker Compose:

    Можно использовать файл .env для определения переменных окружения, которые будут использоваться в docker-compose.yml.

    Пример .env:
        
        POSTGRES_USER=example
        POSTGRES_PASSWORD=example
        POSTGRES_DB=example


    Обновленный docker-compose.yml:
        
        version: '3.8'
        
        services:
          web:
            build: .
            ports:
              - "5000:5000"
            depends_on:
              - db
        
          db:
            image: postgres:13
            environment:
              POSTGRES_USER: ${POSTGRES_USER}
              POSTGRES_PASSWORD: ${POSTGRES_PASSWORD}
              POSTGRES_DB: ${POSTGRES_DB}
            volumes:
              - pgdata:/var/lib/postgresql/data
        
        volumes:
          pgdata:


Основные преимущества использования Docker Compose:

    Упрощение управления многоконтейнерными приложениями:
        Легко запускать, останавливать и управлять всеми контейнерами с помощью одной команды.


    Повторяемость среды:
        Определение конфигурации в docker-compose.yml позволяет легко воспроизводить 
        ту же самую среду на разных машинах.


    Сетевое взаимодействие:
        Docker Compose автоматически создает изолированные сети для сервисов, 
        что упрощает их взаимодействие и улучшает безопасность.


    Облегчение разработки:
        Локальная разработка становится проще, так как все зависимости и сервисы можно запускать с помощью одной команды.


    Масштабирование:
        Легко масштабировать сервисы, добавляя больше экземпляров с помощью команды docker-compose up --scale.


Docker Compose — мощный инструмент для управления многоконтейнерными приложениями, 
который значительно упрощает процессы разработки и развертывания.