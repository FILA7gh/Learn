QuerySet - это коллекция объектов из базы данных Django. Он позволяет выполнять сложные запросы к базе данных
и манипулировать результатами. Каждый QuerySet построен на основе модели, и вы можете получать, фильтровать, изменять
и удалять объекты модели с его помощью.


Создание QuerySet

    Вы можете создать QuerySet, используя менеджер модели.
    По умолчанию Django предоставляет менеджер объектов objects для каждой модели.

    Пример:

        from myapp.models import MyModel

        # Получить все объекты модели
        all_objects = MyModel.objects.all()


Ленивая загрузка

    QuerySet в Django ленивый. Это означает, что запрос к базе данных не выполняется до тех пор,
    пока не произойдет обращение к данным. Это позволяет комбинировать фильтры
    и сортировки без выполнения промежуточных запросов.

        qs = MyModel.objects.filter(field_name='value')
        # Запрос к базе данных выполнится только здесь
        for obj in qs:
            print(obj)


Фильтрация данных

    Вы можете фильтровать данные с помощью методов filter() и exclude().
    
    Пример:
        
        # Фильтрация по полю
        filtered_objects = MyModel.objects.filter(field_name='value')
        
        # Исключение объектов
        excluded_objects = MyModel.objects.exclude(field_name='value')


    Вы также можете использовать сложные фильтры с использованием двойных подчеркиваний 
    для доступа к связанным объектам и выполнения операций.
    
    Пример:
        
        # Фильтрация объектов, где связанный объект имеет определенное значение поля
        filtered_objects = MyModel.objects.filter(related_model__related_field='value')
        
        # Фильтрация объектов, где значение поля больше определенного числа
        filtered_objects = MyModel.objects.filter(field_name__gt=10)


Сортировка данных

    Для сортировки данных используется метод order_by().
    
    Пример:
        
        # Сортировка по полю
        sorted_objects = MyModel.objects.order_by('field_name')
        
        # Обратная сортировка
        sorted_objects = MyModel.objects.order_by('-field_name')



Ограничение и смещение

    Вы можете ограничить количество возвращаемых объектов и смещать их с помощью операций среза Python.
    
    Пример:
        
        # Получить первые 10 объектов
        first_ten_objects = MyModel.objects.all()[:10]
        
        # Получить объекты с 10 по 20
        ten_to_twenty_objects = MyModel.objects.all()[10:20]



Агрегация данных

    Django предоставляет методы для выполнения агрегатных функций, таких как Count, Sum, Avg, Max, Min.
    
    Пример:
        
        from django.db.models import Count, Sum, Avg, Max, Min
        
        # Подсчет количества объектов
        object_count = MyModel.objects.count()
        
        # Суммирование значений поля
        total_sum = MyModel.objects.aggregate(Sum('field_name'))
        
        # Среднее значение поля
        average_value = MyModel.objects.aggregate(Avg('field_name'))
        
        # Максимальное значение поля
        max_value = MyModel.objects.aggregate(Max('field_name'))
        
        # Минимальное значение поля
        min_value = MyModel.objects.aggregate(Min('field_name'))



Аннотации

    Вы можете добавлять агрегированные значения к каждому объекту QuerySet с помощью метода annotate().
    
    Пример:
        
        from django.db.models import Count
        
        # Добавление количества связанных объектов к каждому объекту
        annotated_objects = MyModel.objects.annotate(num_related=Count('related_model'))



Комплексные запросы

    Django QuerySet поддерживает сложные запросы с помощью Q объектов, 
    которые позволяют комбинировать условия с помощью логических операторов & (AND) и | (OR).
    
    Пример:
        
        from django.db.models import Q
        
        # Получить объекты, где поле равно значению ИЛИ другое поле больше определенного числа
        complex_filter = MyModel.objects.filter(Q(field_name='value') | Q(other_field__gt=10))



Методы QuerySet

    all(): Возвращает все объекты QuerySet.
    filter(): Возвращает отфильтрованные объекты QuerySet.
    exclude(): Исключает объекты, соответствующие критериям.
    
    get(): 
        Возвращает один объект, соответствующий критериям 
        (если найдено более одного объекта или ни одного, будет вызвано исключение).
    
    order_by(): Сортирует объекты QuerySet.
    reverse(): Обратный порядок сортировки.
    distinct(): Возвращает уникальные объекты QuerySet.
    values() и values_list(): Возвращают QuerySet, содержащий только указанные поля.
    dates() и datetimes(): Возвращают даты и временные метки.
    none(): Возвращает пустой QuerySet.
    select_related() и prefetch_related(): Выполняют жадную загрузку для связанных объектов.
    
    Пример:
        
        # Получить уникальные значения поля
        distinct_values = MyModel.objects.values('field_name').distinct()
        
        # Жадная загрузка связанных объектов
        related_objects = MyModel.objects.select_related('related_model').all()
        


Кэширование

    QuerySet поддерживает кэширование. Запрос выполняется только один раз, и результаты кешируются 
    для повторного использования.
    
    Пример:
        
        qs = MyModel.objects.filter(field_name='value')
        # Запрос к базе данных выполнится здесь
        list(qs)
        # Повторное обращение использует кеш
        list(qs)
        


Работа с большими наборами данных

    Для работы с большими наборами данных можно использовать метод iterator(), 
    чтобы избежать загрузки всех объектов в память сразу.
    
    Пример:
        
        # Итерация по объектам без загрузки всех сразу в память
        for obj in MyModel.objects.all().iterator():
            print(obj)



Чтение и изменение данных

    QuerySet также поддерживает массовое обновление и удаление данных.
    
    Пример:

    # Массовое обновление
    MyModel.objects.filter(field_name='value').update(other_field='new_value')
    
    # Массовое удаление
    MyModel.objects.filter(field_name='value').delete()


    
Использование собственных методов менеджера 

    Вы можете создавать свои собственные методы менеджера, чтобы расширить функциональность QuerySet.

    Пример:
        
        class MyModelManager(models.Manager):
            def custom_filter(self):
                return self.filter(field_name='value')
        
        class MyModel(models.Model):
            # Объявление менеджера
            objects = MyModelManager()
        
        # Использование собственного метода менеджера
        custom_filtered_objects = MyModel.objects.custom_filter()

Заключение

    Django QuerySet - это мощный инструмент для работы с базой данных, позволяющий выполнять сложные запросы, 
    фильтрацию, сортировку, агрегацию и другие операции. Его ленивый характер и возможность комбинирования методов 
    делают его гибким и эффективным для использования в различных сценариях.
