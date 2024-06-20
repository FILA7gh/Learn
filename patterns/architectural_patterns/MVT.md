
MVT (Model-View-Template) - это паттерн проектирования, который широко используется в веб-разработке,
особенно в фреймворках MVC (Model-View-Controller), таких как Django.


MVT в Django:

    Model (Модель):
        Модель представляет данные вашего приложения и содержит логику работы с ними, включая взаимодействие с базой данных.
        В Django модель обычно представляется классами, наследующими от django.db.models.Model.


    View (Представление):
        Представление обрабатывает запросы от клиентов и возвращает ответы. В Django представления могут быть как функциями,
        так и классами. Они содержат логику для взаимодействия с моделью и формирования данных, которые будут отправлены в шаблон.


    Template (Шаблон):
        Шаблоны являются HTML-файлами с встроенной логикой для отображения данных. В Django шаблоны используют язык разметки
        Django (Django template language) для динамического формирования страниц на основе данных, полученных из представлений.


Особенности MVT в Django:

    Отсутствие явного контроллера:
        В отличие от MVC, в Django нет явного контроллера. Вместо этого логика обработки запросов 
        и формирования данных передается в представления.


    Использование шаблонов (Template):
        Django активно использует шаблоны для отображения данных.
        Они обеспечивают разделение логики представления и его отображения.


    Модель в качестве основы данных:
        Модель является основным компонентом для работы с данными в Django. 
        Она определяет структуру и взаимосвязи данных вашего приложения.


Пример MVT в Django:

    Модель (Model):

        from django.db import models

        class Product(models.Model):
            name = models.CharField(max_length=100)
            price = models.DecimalField(max_digits=10, decimal_places=2)
            description = models.TextField()


    Представление (View):

        from django.shortcuts import render
        from .models import Product

        def product_list(request):
            products = Product.objects.all()
            return render(request, 'product_list.html', {'products': products})


    Шаблон (Template):

        product_list.html:

            <!DOCTYPE html>
            <html>
            <head>
                <title>Product List</title>
            </head>
            <body>
                <h1>Products</h1>
                <ul>
                    {% for product in products %}
                    <li>{{ product.name }} - ${{ product.price }}</li>
                    {% endfor %}
                </ul>
            </body>
            </html>


В этом примере при обращении к URL /products/ будет вызвано представление product_list,
которое получит список всех продуктов из базы данных и передаст их в шаблон product_list.html для отображения.
