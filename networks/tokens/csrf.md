

CSRF токен (Cross-Site Request Forgery token) — это уникальный, случайно сгенерированный токен, 
который используется для защиты веб-приложений от атак типа CSRF. Атака CSRF происходит, 
когда злоумышленник обманным путем заставляет пользователя выполнить нежелательные действия на веб-сайте, 
на котором он авторизован.


Как работает CSRF токен

    Генерация токена:

        При загрузке страницы, которая содержит форму, сервер генерирует уникальный CSRF токен.
        Этот токен встраивается в HTML-форму как скрытое поле или передается как значение куки.


    Отправка запроса:

        Когда пользователь отправляет форму, CSRF токен отправляется вместе с данными формы.
        Токен может быть передан в теле запроса (POST) или в заголовке HTTP.


    Проверка токена на сервере:

        При получении запроса сервер проверяет наличие и корректность CSRF токена.
        Если токен отсутствует или недействителен, сервер отклоняет запрос.


Пример использования CSRF токена в Django

    Django автоматически предоставляет защиту от CSRF для всех POST-запросов, если включено соответствующее middleware.

    Включение CSRF защиты:

        Убедитесь, что django.middleware.csrf.CsrfViewMiddleware включено в MIDDLEWARE в вашем settings.py.
        
        # settings.py
        MIDDLEWARE = [
            ...
            'django.middleware.csrf.CsrfViewMiddleware',
            ...
        ]


    Использование CSRF токена в шаблонах:

        Django автоматически добавляет CSRF токен в шаблоны, когда используется тег {% csrf_token %}.
    
        <form method="post" action="/submit-form/">
            {% csrf_token %}
            <input type="text" name="name">
            <button type="submit">Submit</button>
        </form>


    Обработка запросов в представлениях:

        При использовании классических представлений Django или Django REST framework, 
        CSRF токен будет автоматически проверяться.
        Для API, где нужно вручную добавлять токен, например, в AJAX-запросах, 
        CSRF токен можно получить и передать через JavaScript.



Пример передачи CSRF токена в AJAX-запросах

    Получение CSRF токена:

        В шаблоне HTML, CSRF токен можно добавить в мета-тег:
            
            <meta name="csrf-token" content="{{ csrf_token }}">


    Передача CSRF токена в JavaScript:

        Используйте JavaScript для извлечения и передачи CSRF токена в заголовке AJAX-запроса.
    
        function getCookie(name) {
            let cookieValue = null;
            if (document.cookie && document.cookie !== '') {
                const cookies = document.cookie.split(';');
                for (let i = 0; i < cookies.length; i++) {
                    const cookie = cookies[i].trim();
                    if (cookie.substring(0, name.length + 1) === (name + '=')) {
                        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                        break;
                    }
                }
            }
            return cookieValue;
        }
    
        const csrfToken = getCookie('csrftoken');
    
        fetch('/submit-form/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
                'X-CSRFToken': csrfToken
            },
            body: JSON.stringify({name: 'John Doe'})
        }).then(response => response.json())
          .then(data => console.log(data));
    
    
    
Заключение

    CSRF токен — это важный элемент защиты веб-приложений от атак типа Cross-Site Request Forgery. 
    Использование CSRF токенов позволяет убедиться, что запросы, выполняемые от имени пользователя, 
    действительно исходят из доверенного источника и защищают веб-приложения от потенциально вредоносных действий.
    