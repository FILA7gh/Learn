Dockerfile — это текстовый файл, содержащий набор инструкций для сборки образа Docker.
Каждая инструкция в Dockerfile выполняется последовательно, создавая новый слой в конечном образе.
Dockerfile позволяет автоматизировать процесс создания образов, обеспечивая воспроизводимость и удобство управления.


Основные инструкции Dockerfile:

    FROM:

        Указывает базовый образ, от которого будет строиться текущий образ. Например:

            FROM ubuntu:20.04

    WORKDIR:

        Устанавливает рабочую директорию для последующих инструкций. Если директория не существует, она будет создана. Например:

            WORKDIR /app

    COPY:

        Копирует файлы и директории с хоста в контейнер. Например:

            COPY . /app


    RUN:

        Выполняет команду в контейнере на этапе сборки образа. Например:

            RUN apt-get update && apt-get install -y python3


    CMD:

        Задает команду, которая будет выполнена при запуске контейнера. В отличие от RUN,
        CMD выполняется на этапе выполнения контейнера, а не при его создании. Например:

            CMD ["python3", "app.py"]


    ENTRYPOINT:

        Устанавливает команду, которая будет выполняться при запуске контейнера, и позволяет добавлять аргументы к этой команде. Например:

            ENTRYPOINT ["python3", "app.py"]


    ENV:

        Устанавливает переменные окружения. Например:

            ENV APP_ENV=production


    EXPOSE:

        Указывает, что контейнер будет прослушивать указанный порт во время выполнения. Например:

            EXPOSE 8080


    VOLUME:

        Создает точку монтирования для хранения данных, которые должны быть сохранены вне контейнера. Например:

            VOLUME /data


    USER:

        Задает пользователя, от имени которого будут выполняться команды внутри контейнера. Например:

            USER appuser

Пример Dockerfile для Python приложения:

dockerfile

# Используем базовый образ Python
FROM python:3.9-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файлы зависимостей (requirements.txt) в рабочую директорию
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем весь исходный код приложения в рабочую директорию
COPY . .

# Открываем порт 5000 для доступа к приложению (предположим, что используем Flask)
EXPOSE 5000

# Устанавливаем команду для запуска приложения
CMD ["python", "app.py"]

Пошаговое объяснение примера:

    FROM python:3.9-slim:
    Указывает использовать официальный образ Python версии 3.9 в облегченной версии (slim) в качестве базового образа.

    WORKDIR /app:
    Устанавливает рабочую директорию /app. Все последующие инструкции будут относительны этой директории.

    COPY requirements.txt .:
    Копирует файл requirements.txt из текущей директории на хосте в рабочую директорию контейнера.

    RUN pip install --no-cache-dir -r requirements.txt:
    Выполняет установку зависимостей, указанных в requirements.txt.

    COPY . .:
    Копирует весь исходный код приложения в рабочую директорию контейнера.

    EXPOSE 5000:
    Указывает, что приложение будет доступно на порту 5000 (предположим, что используется Flask, который по умолчанию запускается на этом порту).

    CMD ["python", "app.py"]:
    Устанавливает команду, которая будет выполнена при запуске контейнера, в данном случае — запуск Python-приложения.

Сборка и запуск контейнера:

    Сборка образа:

        Выполните команду для сборки образа на основе Dockerfile:

            docker build -t my-python-app .


    Запуск контейнера:

        Запустите контейнер на основе созданного образа:

            docker run -p 5000:5000 my-python-app

        Эта команда запускает контейнер и перенаправляет порт 5000 на хосте на порт 5000 внутри контейнера,
        что позволяет получить доступ к приложению через http://localhost:5000.
        
        
Советы по написанию Dockerfile:

    Минимизируйте количество слоев:
    
        Объединяйте команды RUN, чтобы уменьшить количество слоев в образе и уменьшить его размер.


    Используйте кэширование:
    
        Инструкции COPY и ADD должны быть расположены как можно выше в Dockerfile, 
        чтобы использовать кэширование на этапах, которые редко изменяются.


    Избегайте ненужных файлов:
    
        Используйте файл .dockerignore для исключения ненужных файлов и директорий из сборки образа.


Пример .dockerignore:

    markdown
    
    __pycache__
    *.pyc
    *.pyo
    *.pyd
    venv
    