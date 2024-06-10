Интеграционные тесты – это тип тестирования программного обеспечения, который проверяет взаимодействие
между различными модулями или компонентами системы. В отличие от юнит-тестов,
которые проверяют отдельные функции или методы в изоляции,
интеграционные тесты фокусируются на проверке правильности работы компонентов вместе.


Основные аспекты интеграционных тестов

    Взаимодействие компонентов: Проверка того, как разные части системы взаимодействуют друг с другом.

    Реалистичное окружение: Использование среды, приближенной к реальной, включая базы данных, веб-сервисы и другие внешние зависимости.

    Проверка сценариев: Тестирование полных сценариев использования, которые охватывают несколько компонентов системы.


Преимущества интеграционных тестов

    Обнаружение ошибок интерфейса: Выявление проблем на стыках различных модулей.

    Уверенность в целостности системы: Убедиться, что все части системы работают вместе правильно.

    Раннее обнаружение проблем: Обнаружение проблем, связанных с интеграцией, на ранних этапах разработки.


Пример интеграционного теста в Django REST Framework (DRF)

    Основной код

        models.py

            from django.db import models

            class Item(models.Model):
                name = models.CharField(max_length=100)
                description = models.TextField()

                def __str__(self):
                    return self.name


        serializers.py

            from rest_framework import serializers
            from .models import Item

            class ItemSerializer(serializers.ModelSerializer):
                class Meta:
                    model = Item
                    fields = ['id', 'name', 'description']


        views.py

            from rest_framework import generics
            from .models import Item
            from .serializers import ItemSerializer

            class ItemListCreateView(generics.ListCreateAPIView):
                queryset = Item.objects.all()
                serializer_class = ItemSerializer


        urls.py

            from django.urls import path
            from .views import ItemListCreateView

            urlpatterns = [
                path('items/', ItemListCreateView.as_view(), name='item-list-create'),
            ]


    Интеграционный тест

        tests.py

            from rest_framework.test import APITestCase
            from rest_framework import status
            from django.urls import reverse
            from .models import Item

            class ItemTests(APITestCase):

                def test_create_item(self):
                    url = reverse('item-list-create')
                    data = {'name': 'Test Item', 'description': 'Test Description'}
                    response = self.client.post(url, data, format='json')
                    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
                    self.assertEqual(Item.objects.count(), 1)
                    self.assertEqual(Item.objects.get().name, 'Test Item')

                def test_get_items(self):
                    Item.objects.create(name='Test Item 1', description='Description 1')
                    Item.objects.create(name='Test Item 2', description='Description 2')
                    url = reverse('item-list-create')
                    response = self.client.get(url, format='json')
                    self.assertEqual(response.status_code, status.HTTP_200_OK)
                    self.assertEqual(len(response.data), 2)
                    self.assertEqual(response.data[0]['name'], 'Test Item 1')
                    self.assertEqual(response.data[1]['name'], 'Test Item 2')



Запуск интеграционных тестов
    
    python manage.py test


Выводы

    Интеграционные тесты важны для обеспечения того, что все компоненты системы работают вместе правильно. 
    Они помогают обнаруживать ошибки, которые могут возникнуть на стыке различных модулей, 
    и обеспечивают уверенность в целостности системы.
