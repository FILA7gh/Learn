MVC (Model-View-Controller) — это архитектурный паттерн, используемый для разделения приложения
на три взаимосвязанные компоненты: модель, представление и контроллер. Этот паттерн способствует разбиению приложения
на логические части с целью облегчения разработки, тестирования и поддержки.


Компоненты MVC

    Модель (Model):

        Отвечает за управление данными, бизнес-логикой и правилами приложения.
        В модели реализуется взаимодействие с базой данных и манипуляция данными.


    Представление (View):

        Отвечает за отображение данных пользователю.
        Представление генерирует интерфейс пользователя на основе данных из модели.


    Контроллер (Controller):
        Управляет взаимодействием между моделью и представлением.
        Получает входные данные от пользователя, обрабатывает их (включая вызовы методов модели) и определяет, какое представление нужно отобразить.


Пример MVC на Python с использованием Flask

    Рассмотрим пример реализации MVC паттерна на языке Python с использованием веб-фреймворка Flask.
    1. Установка Flask

        pip install Flask


    2. Структура проекта

        project/
        │
        ├── app.py
        ├── models.py
        ├── views.py
        └── controllers.py


    3. Реализация компонентов

        Модель (models.py)

        class Item:
            def __init__(self, id, name, description):
                self.id = id
                self.name = name
                self.description = description

        # Пример данных
        items = [
            Item(1, 'Item1', 'Description of Item1'),
            Item(2, 'Item2', 'Description of Item2'),
        ]

        def get_all_items():
            return items

        def get_item_by_id(item_id):
            for item in items:
                if item.id == item_id:
                    return item
            return None


        Контроллер (controllers.py)

            from flask import request, redirect, url_for
            from models import get_all_items, get_item_by_id

            def show_items():
                items = get_all_items()
                return items

            def show_item(item_id):
                item = get_item_by_id(item_id)
                return item

            def add_item():
                new_id = len(get_all_items()) + 1
                new_item = Item(new_id, request.form['name'], request.form['description'])
                items.append(new_item)
                return redirect(url_for('item_list'))


        Представление (views.py)

            from flask import Flask, render_template
            from controllers import show_items, show_item

            app = Flask(__name__)

            @app.route('/')
            def item_list():
                items = show_items()
                return render_template('item_list.html', items=items)

            @app.route('/item/<int:item_id>')
            def item_detail(item_id):
                item = show_item(item_id)
                return render_template('item_detail.html', item=item)

            if __name__ == '__main__':
                app.run(debug=True)


        Шаблоны HTML (templates)

            item_list.html:

                <!doctype html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <title>Item List</title>
                </head>
                <body>
                    <h1>Item List</h1>
                    <ul>
                        {% for item in items %}
                        <li><a href="{{ url_for('item_detail', item_id=item.id) }}">{{ item.name }}</a></li>
                        {% endfor %}
                    </ul>
                </body>
                </html>


            item_detail.html:

                <!doctype html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <title>Item Detail</title>
                </head>
                <body>
                    <h1>{{ item.name }}</h1>
                    <