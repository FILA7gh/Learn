
Схема базы данных (Database Schema) — это логическая структура, которая определяет организацию данных в базе данных.
Она описывает структуру таблиц, их поля и связи между ними. Схема базы данных определяет,
какие типы данных могут храниться в каждом поле, какие ограничения применяются к данным,
а также какие связи существуют между различными таблицами.


Основные компоненты схемы базы данных:

    Таблицы (Tables):
        Определяются в схеме для хранения конкретных типов данных.
        Каждая таблица имеет уникальное имя и состоит из столбцов и строк (записей).


    Столбцы (Columns):
        Определяют типы данных, которые могут быть сохранены в каждом поле таблицы. Каждый столбец имеет имя,
        тип данных и, возможно, другие атрибуты, такие как ограничения, уникальность или внешние ключи.


    Связи (Relationships):
        Определяют отношения между таблицами в базе данных. Эти отношения определяются через внешние ключи,
        которые связывают одно поле таблицы с другим полем в другой таблице.


    Ограничения (Constraints):
        Определяют правила, которые данные должны соответствовать при добавлении или обновлении в базу данных.
        Например, ограничения могут включать проверку уникальности значений в столбцах или требование,
        чтобы определенное поле не было пустым.


Пример схемы базы данных в SQL:

    CREATE TABLE Users (
        id INT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        email VARCHAR(100) UNIQUE,
        age INT
    );

    CREATE TABLE Posts (
        id INT PRIMARY KEY,
        title VARCHAR(255) NOT NULL,
        content TEXT,
        user_id INT,
        FOREIGN KEY (user_id) REFERENCES Users(id)
    );


    В этом примере схема базы данных определяет две таблицы: "Users" и "Posts".
    "Users" содержит информацию о пользователях, такую как их идентификатор, имя, электронная почта и возраст. "Posts"
    содержит записи пользователей, каждая из которых связана с определенным пользователем через внешний ключ "user_id".
    Это обеспечивает связь между таблицами "Users" и "Posts".
