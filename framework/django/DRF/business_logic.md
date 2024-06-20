В Django REST Framework (DRF) бизнес-логику следует структурировать так, чтобы код был легко поддерживаемым, 
тестируемым и расширяемым. Вот ключевые места, где можно писать бизнес-логику в DRF:


Модели (Models)
    
    Модели определяют структуру данных и простую бизнес-логику, связанную с данными.
    
    from django.db import models
    
    class Product(models.Model):
        name = models.CharField(max_length=100)
        price = models.DecimalField(max_digits=10, decimal_places=2)
        
        def apply_discount(self, discount_percentage):
            self.price = self.price * (1 - discount_percentage / 100)
            self.save()
    

Менеджеры (Managers)

    Менеджеры моделей используются для выполнения более сложных операций с базой данных.
    
    from django.db import models
    
    class ProductManager(models.Manager):
        def available(self):
            return self.filter(is_available=True)
    
    class Product(models.Model):
        name = models.CharField(max_length=100)
        price = models.DecimalField(max_digits=10, decimal_places=2)
        is_available = models.BooleanField(default=True)
        
        objects = ProductManager()


Сервисы (Services)

    Для более сложной и многослойной бизнес-логики используются сервисные классы.
    
    class OrderService:
        @staticmethod
        def create_order(user, product):
            order = Order(user=user, product=product)
            order.save()
            return order


Сигналы (Signals)

    Сигналы позволяют выполнять бизнес-логику в ответ на определенные события, такие как создание или обновление модели.
    
    from django.db.models.signals import post_save
    from django.dispatch import receiver
    
    @receiver(post_save, sender=Product)
    def update_stock(sender, instance, **kwargs):
        if instance.stock == 0:
            instance.is_available = False
            instance.save()


Middleware

    Middleware используется для выполнения бизнес-логики, связанной с обработкой запросов или ответов.
    
    from django.utils.deprecation import MiddlewareMixin
    
    class CustomMiddleware(MiddlewareMixin):
        def process_request(self, request):
            # Выполнить логику перед обработкой запроса представлением
            pass
    
        def process_response(self, request, response):
            # Выполнить логику перед отправкой ответа клиенту
            return response


Сериалайзеры (Serializers)

    Сериалайзеры преобразуют данные и выполняют валидацию, что особенно важно при работе с API.
    
    from rest_framework import serializers
    
    class ProductSerializer(serializers.ModelSerializer):
        class Meta:
            model = Product
            fields = ['id', 'name', 'price', 'is_available']
        
        def validate_price(self, value):
            if value < 0:
                raise serializers.ValidationError("Price cannot be negative")
            return value


Представления (Views)

    Представления обрабатывают запросы и возвращают ответы. DRF предоставляет Generic Views и ViewSets для упрощения работы с API.
    
    from rest_framework.views import APIView
    from rest_framework.response import Response
    from rest_framework import status
    
    class ProductAPIView(APIView):
        def get(self, request):
            products = Product.objects.available()
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data)
    
        def post(self, request):
            serializer = ProductSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


ViewSets

    ViewSets упрощают создание API и объединяют логику для различных действий (CRUD).
    
    from rest_framework import viewsets
    
    class ProductViewSet(viewsets.ModelViewSet):
        queryset = Product.objects.all()
        serializer_class = ProductSerializer
    
        def perform_create(self, serializer):
            # Дополнительная бизнес-логика при создании объекта
            serializer.save()


Функции представления (Function-Based Views)

    Для простых сценариев можно использовать функции представления.
    
    from rest_framework.decorators import api_view
    from rest_framework.response import Response
    
    @api_view(['GET', 'POST'])
    def product_list(request):
        if request.method == 'GET':
            products = Product.objects.available()
            serializer = ProductSerializer(products, many=True)
            return Response(serializer.data)
        elif request.method == 'POST':
            serializer = ProductSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


Заключение

    Оптимальное размещение бизнес-логики в DRF зависит от конкретной задачи. 
    Для простых операций логика может находиться в моделях и менеджерах. 
    Для более сложных сценариев рекомендуется использовать сервисы, сигналы и сериалайзеры для управления валидацией 
    и преобразованием данных. Представления и ViewSets помогают управлять запросами и ответами, 
    обеспечивая разделение обязанностей и делая код более чистым и поддерживаемым.
