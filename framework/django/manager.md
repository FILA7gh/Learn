
В Django, менеджер (manager) — это интерфейс для запросов к базе данных, который используется для взаимодействия с моделями. 
Менеджеры предоставляют методы для выполнения запросов, таких как получение всех объектов модели, фильтрация объектов, 
обновление или удаление объектов и другие операции.


Основной менеджер объектов

    По умолчанию, каждая модель Django имеет менеджер объектов objects, который является экземпляром класса 
    django.db.models.Manager. Этот менеджер предоставляет базовые методы для работы с базой данных, 
    такие как all(), filter(), get(), exclude() и другие.
    
    from django.db import models
    
    class Product(models.Model):
        name = models.CharField(max_length=100)
        price = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Использование стандартного менеджера для получения всех продуктов
    products = Product.objects.all()


Создание пользовательских менеджеров

    Вы можете создать свои собственные менеджеры, наследуясь от models.Manager, и добавлять в них свои методы. 
    Это полезно для инкапсуляции бизнес-логики, связанной с запросами.
    
    from django.db import models
    
    class ProductManager(models.Manager):
        def available(self):
            return self.filter(is_available=True)
    
    class Product(models.Model):
        name = models.CharField(max_length=100)
        price = models.DecimalField(max_digits=10, decimal_places=2)
        is_available = models.BooleanField(default=True)
    
        objects = ProductManager()
    
    # Использование пользовательского менеджера для получения доступных продуктов
    available_products = Product.objects.available()
    

Использование менеджеров в моделях

    Менеджеры позволяют вам создавать методы для выполнения сложных запросов, 
    которые могут быть повторно использованы в разных частях вашего кода.
    
    class ProductManager(models.Manager):
        def expensive_products(self):
            return self.filter(price__gt=100)
    
    class Product(models.Model):
        name = models.CharField(max_length=100)
        price = models.DecimalField(max_digits=10, decimal_places=2)
    
        objects = ProductManager()
    
    # Использование метода пользовательского менеджера для получения дорогих продуктов
    expensive_products = Product.objects.expensive_products()


Переопределение методов менеджера

    Вы можете переопределять методы менеджера, чтобы изменить их поведение. 
    Например, можно изменить поведение метода get_queryset().
    
    class PublishedManager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(is_published=True)
    
    class Article(models.Model):
        title = models.CharField(max_length=100)
        content = models.TextField()
        is_published = models.BooleanField(default=False)
    
        objects = PublishedManager()
    
    # Использование переопределенного менеджера для получения только опубликованных статей
    published_articles = Article.objects.all()



Заключение

    Менеджеры в Django предоставляют мощный способ взаимодействия с базой данных. 
    Они позволяют вам инкапсулировать логику запросов и повторно использовать ее в разных частях вашего приложения. 
    Пользовательские менеджеры особенно полезны для создания сложных запросов и обеспечения чистоты и логичности кода.
    