
JSON Web Token (JWT) — это стандарт для создания токенов доступа, которые можно использовать для аутентификации
и передачи информации между различными частями системы.
JWT позволяет безопасно передавать данные между клиентом и сервером в JSON-формате.


Основные компоненты JWT

    JWT состоит из трех частей, разделенных точками (.):

        Header (Заголовок):
            Содержит метаинформацию о токене, например, используемый алгоритм шифрования.

            Пример:

                {
                  "alg": "HS256",
                  "typ": "JWT"
                }


    Payload (Полезная нагрузка):
        Содержит утверждения (claims), т.е. информацию, которую нужно передать и которая может быть закодирована в токен.

            {
              "sub": "1234567890",
              "name": "John Doe",
              "admin": true
            }


    Signature (Подпись):
        Используется для проверки подлинности отправителя токена и целостности данных.
        Создается путем подписания закодированного заголовка и полезной нагрузки секретным ключом.



Пример JWT

    Токен состоит из трех частей, закодированных в Base64Url и разделенных точками. Пример токена:

        eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.
        eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWV9.
        SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c

        Header: eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9

        Payload: eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWV9

        Signature: SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c


Использование JWT

    1. Аутентификация

    JWT часто используется для аутентификации пользователей. Процесс обычно выглядит следующим образом:

        Пользователь вводит свои учетные данные (логин и пароль).

        Сервер проверяет учетные данные и, если они верны, создает JWT и отправляет его клиенту.

        Клиент сохраняет JWT (обычно в локальном хранилище или cookies).

        Клиент отправляет JWT в заголовке HTTP-запросов к серверу для аутентификации.


    2. Авторизация

    JWT также используется для авторизации доступа к ресурсам. Сервер проверяет наличие и действительность JWT,
    чтобы определить, имеет ли пользователь доступ к запрашиваемому ресурсу.

    Преимущества JWT

        Компактность:
            Токены небольшого размера и могут легко передаваться в URL, заголовках HTTP или внутри тела запроса.


        Самодостаточность:
            JWT содержит всю необходимую информацию, что позволяет серверу не хранить состояние токена.


        Безопасность:
            Подпись токена позволяет проверить подлинность отправителя и целостность данных.


        Масштабируемость:
            JWT может использоваться в распределенных системах, так как нет необходимости хранить токены на сервере.


Недостатки и вызовы

    Безопасность хранения:
        JWT необходимо хранить безопасно на клиенте, чтобы предотвратить их кражу и использование злоумышленниками.


    Отзыв токенов:
        JWT трудно отозвать до истечения их срока действия, что может представлять проблему в случае компрометации токена.


    Размер токена:
        Большое количество утверждений в полезной нагрузке может увеличить размер токена, 
        что может повлиять на производительность.


        
Вот пример, демонстрирующий использование JWT в Django с помощью библиотеки djangorestframework-jwt. 
В этом примере мы реализуем простую систему аутентификации с использованием JWT токенов.

    Установите библиотеку djangorestframework-jwt:

        pip install djangorestframework-jwt

    
    Настройте Django проект для использования djangorestframework-jwt:
        
        # settings.py
        
        INSTALLED_APPS = [
            ...
            'rest_framework',
            'rest_framework_jwt',
        ]
        
        REST_FRAMEWORK = {
            'DEFAULT_AUTHENTICATION_CLASSES': (
                'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
                'rest_framework.authentication.SessionAuthentication',
                'rest_framework.authentication.BasicAuthentication',
            ),
        }
        
        JWT_AUTH = {
            'JWT_SECRET_KEY': 'your_secret_key',
            'JWT_EXPIRATION_DELTA': datetime.timedelta(days=1),
        }


    Создайте представления (views) для регистрации и аутентификации пользователей:
        
        # views.py
        
        from rest_framework.views import APIView
        from rest_framework.response import Response
        from rest_framework.permissions import AllowAny
        from django.contrib.auth.models import User
        from rest_framework_jwt.settings import api_settings
        
        class RegisterUser(APIView):
            permission_classes = (AllowAny,)
        
            def post(self, request):
                username = request.data.get('username')
                password = request.data.get('password')
                if not username or not password:
                    return Response({'error': 'Please provide both username and password'}, status=400)
                if User.objects.filter(username=username).exists():
                    return Response({'error': 'Username already exists'}, status=400)
                user = User.objects.create_user(username=username, password=password)
                return Response({'message': 'User registered successfully'}, status=201)
        
        class ObtainAuthToken(APIView):
            permission_classes = (AllowAny,)
        
            def post(self, request):
                username = request.data.get('username')
                password = request.data.get('password')
                user = authenticate(username=username, password=password)
                if user:
                    jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
                    jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
                    payload = jwt_payload_handler(user)
                    token = jwt_encode_handler(payload)
                    return Response({'token': token}, status=200)
                else:
                    return Response({'error': 'Invalid username or password'}, status=401)



    Настройте маршруты для ваших представлений:
        
        # urls.py
        
        from django.urls import path
        from .views import RegisterUser, ObtainAuthToken
        
        urlpatterns = [
            path('register/', RegisterUser.as_view(), name='register'),
            path('login/', ObtainAuthToken.as_view(), name='login'),
        ]


Это базовый пример использования JWT для аутентификации пользователей в Django. 
Обратите внимание, что этот пример предполагает использование SessionAuthentication и BasicAuthentication 
вместе с JWT для аутентификации пользователя в вашем API.
