Миграции базы данных — это инструмент для управления изменениями схемы базы данных в проекте. 
Они позволяют разработчикам описывать изменения в структуре базы данных 
(например, добавление новых таблиц или столбцов, изменение типов данных, удаление таблиц) 
в виде кода и применять их последовательно, отслеживая все изменения в репозитории проекта. 
Миграции обеспечивают согласованность базы данных с моделями данных и упрощают 
обновление схемы при развертывании новых версий приложения.


Основные концепции миграций

    Миграция: 

        Описание изменения в структуре базы данных. Обычно миграция включает инструкции для внесения изменений 
        (вперед) и отката изменений (назад).


    Ревизия: 
    
            Идентификатор, присваиваемый каждой миграции, позволяющий отслеживать последовательность изменений.

    
    Автогенерация миграций: 

        Процесс автоматического создания миграций на основе различий между текущим 
        состоянием базы данных и определением моделей данных в коде.



Пример миграций в Django ORM

    Django ORM имеет встроенную систему миграций, которая автоматически отслеживает изменения в моделях и создает файлы миграций.
    
    Основные команды
    
        Создание миграций:
            
            python manage.py makemigrations
            
            Эта команда анализирует изменения в моделях и создает файлы миграций.
  
          
        Применение миграций:
            
            python manage.py migrate
            
            Эта команда применяет все непримененные миграции к базе данных.
        

        Просмотр состояния миграций:
        
            python manage.py showmigrations
        
            Эта команда отображает все миграции и их статус (применены или нет).
    

    Пример
    
        Создание моделей:
             
            # models.py
            from django.db import models
            
            class Author(models.Model):
                name = models.CharField(max_length=100)
                age = models.IntegerField()
            
            class Book(models.Model):
                title = models.CharField(max_length=100)
                author = models.ForeignKey(Author, on_delete=models.CASCADE)
                published_date = models.DateField()
            

        Создание миграций:
        
            python manage.py makemigrations

        
        Применение миграций:
             
            python manage.py migrate
            

        Добавление нового поля:
             
            # models.py
            class Book(models.Model):
                title = models.CharField(max_length=100)
                author = models.ForeignKey(Author, on_delete=models.CASCADE)
                published_date = models.DateField()
                isbn = models.CharField(max_length=13, null=True)  # Новое поле
        

        Создание и применение миграций для нового поля:
         
            python manage.py makemigrations
            python manage.py migrate



Пример миграций в SQLAlchemy с Alembic

    SQLAlchemy не имеет встроенной системы миграций, поэтому используется 
    Alembic — сторонний инструмент для управления миграциями.
    
    Основные команды
    
        Инициализация Alembic:
        
            alembic init alembic
            
            Эта команда создает директорию с настройками Alembic.
            

    Автоматическое создание миграций:
         
        alembic revision --autogenerate -m "Create tables"
        
        Эта команда создает файл миграции на основе изменений в моделях.
    

    Применение миграций:
         
        alembic upgrade head
        
        Эта команда применяет миграции к базе данных.
    

    Просмотр состояния миграций:
    
        alembic current
    
        Эта команда отображает текущий статус миграций.
    
    Пример
    
        Создание моделей:
             
            # models.py
            from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Date
            from sqlalchemy.ext.declarative import declarative_base
            from sqlalchemy.orm import relationship, sessionmaker
            
            Base = declarative_base()
            
            class Author(Base):
                __tablename__ = 'authors'
                id = Column(Integer, primary_key=True)
                name = Column(String)
                age = Column(Integer)
            
                books = relationship('Book', back_populates='author')
            
            class Book(Base):
                __tablename__ = 'books'
                id = Column(Integer, primary_key=True)
                title = Column(String)
                author_id = Column(Integer, ForeignKey('authors.id'))
                published_date = Column(Date)
            
                author = relationship('Author', back_populates='books')
            
            engine = create_engine('sqlite:///example.db')
            Base.metadata.create_all(engine)
            

        Инициализация Alembic:
             
            alembic init alembic
            

        Настройка подключения к базе данных:
        
            Измените строку подключения в alembic.ini и настройте env.py.
        

        Автогенерация миграций:
             
            alembic revision --autogenerate -m "Initial migration"
        
    
        Применение миграций:
 
            alembic upgrade head
 
           
        Добавление нового поля:
             
            # models.py
            class Book(Base):
                __tablename__ = 'books'
                id = Column(Integer, primary_key=True)
                title = Column(String)
                author_id = Column(Integer, ForeignKey('authors.id'))
                published_date = Column(Date)
                isbn = Column(String, nullable=True)  # Новое поле
            
                author = relationship('Author', back_populates='books')
            
    
        Автогенерация и применение новой миграции:
         
            alembic revision --autogenerate -m "Add isbn to books"
            alembic upgrade head



Заключение

    Миграции позволяют управлять изменениями в схеме базы данных последовательно и безопасно. 
    Они особенно полезны в проектах, где структура данных изменяется с течением времени. 
    Встроенная система миграций Django упрощает этот процесс для проектов на Django. SQLAlchemy, с помощью Alembic, 
    предоставляет мощные инструменты для управления миграциями, подходящие для проектов, 
    требующих высокой степени контроля над базой данных.
