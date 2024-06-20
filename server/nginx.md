Nginx (произносится как "Engine-X") — это веб-сервер с открытым исходным кодом, который также может работать 
как обратный прокси-сервер, балансировщик нагрузки и HTTP-кэш. 
Он был разработан для обеспечения высокой производительности и масштабируемости.


Основные функции Nginx

    Веб-сервер:
        Обслуживание статического контента (HTML, CSS, JavaScript, изображения и т.д.).
        Поддержка динамических приложений через FastCGI, SCGI, uWSGI и другие протоколы.

    Обратный прокси-сервер:
        Перенаправление запросов на один или несколько серверов приложений для обработки.
        Агрегация ответов от различных серверов приложений.

    Балансировка нагрузки:
        Распределение входящего трафика между несколькими серверами для повышения производительности и надежности.
        Поддержка различных алгоритмов балансировки нагрузки (round-robin, least connections, IP hash и т.д.).

    Кэширование:
        Кэширование ответов для уменьшения нагрузки на серверы приложений и улучшения времени отклика.


    SSL/TLS терминатор:
        Обработка SSL/TLS соединений для шифрования данных между клиентами и серверами.



Установка и базовая настройка Nginx

    Установка на Ubuntu

        Установка Nginx:
            
            sudo apt update
            sudo apt install nginx
    

    Запуск и проверка статуса:
    
        sudo systemctl start nginx
        sudo systemctl enable nginx
        sudo systemctl status nginx
    

    Проверка установки:
        Откройте веб-браузер и перейдите по адресу http://your_server_ip. Вы должны увидеть приветственную страницу Nginx.



Базовая настройка Nginx

    Файл конфигурации:
        Основной файл конфигурации Nginx находится по пути /etc/nginx/nginx.conf.


    Настройка сайта:
        Конфигурационные файлы сайтов обычно находятся в директории /etc/nginx/sites-available/, 
        а активные сайты символически связаны в /etc/nginx/sites-enabled/.


    Пример конфигурации сайта:
        Создайте новый конфигурационный файл для вашего сайта в /etc/nginx/sites-available/:
        
            server {
                listen 80;
                server_name example.com www.example.com;
        
                location / {
                    proxy_pass http://127.0.0.1:8080;  # Прокси-передача на внутренний сервер
                    proxy_set_header Host $host;
                    proxy_set_header X-Real-IP $remote_addr;
                    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                    proxy_set_header X-Forwarded-Proto $scheme;
                }
            }
    
    Активация сайта:
        Создайте символическую ссылку на файл конфигурации в директории sites-enabled:
     
           sudo ln -s /etc/nginx/sites-available/your_site /etc/nginx/sites-enabled/



    Проверка конфигурации и перезапуск Nginx:
        Проверьте конфигурацию на наличие синтаксических ошибок:
                
            sudo nginx -t
            

    Перезапустите Nginx для применения изменений:

        sudo systemctl restart nginx



Расширенные функции Nginx

    Балансировка нагрузки:

        Добавьте несколько серверов для распределения нагрузки:
        
            upstream backend {
                server backend1.example.com;
                server backend2.example.com;
            }
        
            server {
                listen 80;
                server_name example.com;
        
                location / {
                    proxy_pass http://backend;
                    proxy_set_header Host $host;
                    proxy_set_header X-Real-IP $remote_addr;
                    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                    proxy_set_header X-Forwarded-Proto $scheme;
                }
            }


    Кэширование:

        Включите кэширование на прокси-сервере для улучшения производительности:
        
            proxy_cache_path /data/nginx/cache levels=1:2 keys_zone=my_cache:10m max_size=1g inactive=60m use_temp_path=off;
        
            server {
                listen 80;
                server_name example.com;
        
                location / {
                    proxy_cache my_cache;
                    proxy_pass http://127.0.0.1:8080;
                    proxy_set_header Host $host;
                    proxy_set_header X-Real-IP $remote_addr;
                    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                    proxy_set_header X-Forwarded-Proto $scheme;
                }
            }


SSL/TLS настройка:

    Добавьте поддержку HTTPS с помощью SSL/TLS:

        server {
            listen 443 ssl;
            server_name example.com;

            ssl_certificate /etc/nginx/ssl/nginx.crt;
            ssl_certificate_key /etc/nginx/ssl/nginx.key;

            location / {
                proxy_pass http://127.0.0.1:8080;
                proxy_set_header Host $host;
                proxy_set_header X-Real-IP $remote_addr;
                proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                proxy_set_header X-Forwarded-Proto $scheme;
            }
        }



Заключение

    Nginx — это мощный и гибкий инструмент для управления веб-трафиком. Он может быть использован 
    в качестве веб-сервера, обратного прокси-сервера, балансировщика нагрузки и кэширующего прокси. 
    Благодаря своей высокой производительности и надежности, 
    Nginx является популярным выбором для современных веб-приложений.
