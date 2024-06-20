Функциональные тесты проверяют работу системы целиком, фокусируясь на проверке функциональности приложения по сценарию,
описанному в спецификациях или требованиях. Функциональные тесты часто проверяют пользовательские сценарии, эмулируя действия пользователя.


Пример функционального теста в FastAPI

    Предположим, у нас есть FastAPI-приложение с несколькими конечными точками для управления элементами,
    включая создание, получение списка, получение по ID и удаление элемента.

    Основной код

        main.py

            from fastapi import FastAPI, HTTPException
            from pydantic import BaseModel
            from typing import List, Optional

            app = FastAPI()

            class Item(BaseModel):
                id: int
                name: str
                description: str

            items = []

            @app.post("/items/", response_model=Item)
            def create_item(item: Item):
                items.append(item)
                return item

            @app.get("/items/", response_model=List[Item])
            def get_items():
                return items

            @app.get("/items/{item_id}", response_model=Item)
            def get_item(item_id: int):
                for item in items:
                    if item.id == item_id:
                        return item
                raise HTTPException(status_code=404, detail="Item not found")

            @app.delete("/items/{item_id}", response_model=Item)
            def delete_item(item_id: int):
                for item in items:
                    if item.id == item_id:
                        items.remove(item)
                        return item
                raise HTTPException(status_code=404, detail="Item not found")


Функциональные тесты
    
    test_main.py
        
        from fastapi.testclient import TestClient
        from main import app
        
        client = TestClient(app)
        
        def test_create_item():
            response = client.post("/items/", json={"id": 1, "name": "Test Item", "description": "Test Description"})
            assert response.status_code == 200
            assert response.json() == {"id": 1, "name": "Test Item", "description": "Test Description"}
        
        def test_get_items():
            client.post("/items/", json={"id": 1, "name": "Test Item 1", "description": "Description 1"})
            client.post("/items/", json={"id": 2, "name": "Test Item 2", "description": "Description 2"})
            response = client.get("/items/")
            assert response.status_code == 200
            assert len(response.json()) == 2
            assert response.json()[0] == {"id": 1, "name": "Test Item 1", "description": "Description 1"}
            assert response.json()[1] == {"id": 2, "name": "Test Item 2", "description": "Description 2"}
        
        def test_get_item():
            client.post("/items/", json={"id": 1, "name": "Test Item", "description": "Test Description"})
            response = client.get("/items/1")
            assert response.status_code == 200
            assert response.json() == {"id": 1, "name": "Test Item", "description": "Test Description"}
        
        def test_delete_item():
            client.post("/items/", json={"id": 1, "name": "Test Item", "description": "Test Description"})
            response = client.delete("/items/1")
            assert response.status_code == 200
            assert response.json() == {"id": 1, "name": "Test Item", "description": "Test Description"}
            response = client.get("/items/1")
            assert response.status_code == 404
    
    
    Объяснение кода
    
        Создание клиента для тестирования:
            TestClient используется для создания тестового клиента, 
            который будет взаимодействовать с нашим FastAPI-приложением.
    
    
        Тестирование создания элемента:

            test_create_item отправляет POST-запрос на конечную точку /items/ с данными элемента в формате JSON.
            Проверяется, что статус ответа равен 200 (успешный запрос).
            Проверяется, что результат создания элемента соответствует отправленным данным.
    
    
        Тестирование получения всех элементов:
    
            test_get_items отправляет два POST-запроса для создания двух элементов.
            Затем отправляется GET-запрос на конечную точку /items/, чтобы получить список всех элементов.
            Проверяется, что статус ответа равен 200.
            Проверяется, что в списке находятся два элемента и что их данные соответствуют ожидаемым.
    
    
        Тестирование получения элемента по ID:
    
            test_get_item отправляет POST-запрос для создания элемента, а затем GET-запрос для получения элемента по его ID.
            Проверяется, что статус ответа равен 200 и что данные элемента соответствуют ожидаемым.
    
    
        Тестирование удаления элемента:
    
            test_delete_item отправляет POST-запрос для создания элемента, затем DELETE-запрос для удаления элемента по его ID.
            Проверяется, что статус ответа равен 200 и что данные удаленного элемента соответствуют ожидаемым.
            Затем проверяется, что повторный GET-запрос для получения элемента по его ID возвращает статус 404 (не найден).



Запуск функциональных тестов

    Чтобы запустить тесты, выполните команду:
        
        pytest test_main.py

    Вывод
    
        Если все тесты проходят успешно, вы увидите сообщение:
        
        ....
        ----------------------------------------------------------------------
        Ran 4 tests in 0.001s
        
        OK
    
        Если какой-то тест не пройдет, вы получите сообщение об ошибке с указанием, какой именно тест не прошел и почему.



Выводы

    Функциональные тесты важны для проверки того, что приложение работает корректно в соответствии с требованиями и спецификациями. 
    Они эмулируют реальные сценарии использования и помогают убедиться, 
    что все функциональные возможности приложения работают правильно. В данном примере мы рассмотрели, 
    как писать и запускать функциональные тесты для API, используя FastAPI и TestClient из fastapi.testclient.
