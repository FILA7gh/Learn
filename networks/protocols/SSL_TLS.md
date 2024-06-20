
SSL (Secure Sockets Layer) и TLS (Transport Layer Security) — это криптографические протоколы,
которые обеспечивают защиту данных, передаваемых по сети, за счет шифрования.
TLS является преемником SSL и включает в себя улучшенные механизмы безопасности.
На сегодняшний день используется именно TLS, хотя термин "SSL" часто применяется как обобщение.


Основные функции SSL/TLS

    Шифрование:
        Обеспечивает конфиденциальность данных, предотвращая их перехват и чтение третьими лицами.


    Аутентификация:
        Подтверждает подлинность сервера и клиента, обеспечивая защиту от атак типа "человек посередине" (MITM).


    Целостность данных:
        Гарантирует, что данные не были изменены или повреждены в процессе передачи.



Как работает SSL/TLS

    Handshake (рукопожатие):
        Клиент и сервер обмениваются сообщениями для установления параметров защищенного соединения.
        Этот процесс включает:

            Аутентификацию сервера (и клиента, если требуется).

            Согласование алгоритмов шифрования и MAC (Message Authentication Code).

            Генерацию симметричного ключа шифрования.


    Сеансовое шифрование:
        После установления защищенного соединения клиент и сервер используют симметричное шифрование для обмена данными.
        Это обеспечивает высокую производительность шифрования.


Установка и настройка SSL/TLS на веб-сервере (Nginx)

    Получение SSL-сертификата:
        SSL-сертификат можно получить у доверенного центра сертификации (CA), такого как Let's Encrypt, Comodo, DigiCert и т.д.


    Установка SSL-сертификата:
        Поместите файлы сертификата и приватного ключа на сервер (например, в /etc/nginx/ssl/).


    Настройка Nginx:

        Откройте файл конфигурации вашего сайта (например, /etc/nginx/sites-available/your_site):

            server {
                listen 80;
                server_name example.com;
                return 301 https://$host$request_uri;  # Перенаправление HTTP на HTTPS
            }

            server {
                listen 443 ssl;
                server_name example.com;

                ssl_certificate /etc/nginx/ssl/nginx.crt;
                ssl_certificate_key /etc/nginx/ssl/nginx.key;

                ssl_protocols TLSv1.2 TLSv1.3;
                ssl_prefer_server_ciphers on;
                ssl_ciphers 'ECDHE-ECDSA-AES256-GCM-SHA384:ECDHE-RSA-AES256-GCM-SHA384:ECDHE-ECDSA-CHACHA20-POLY1305:
                ECDHE-RSA-CHACHA20-POLY1305:ECDHE-ECDSA-AES128-GCM-SHA256:ECDHE-RSA-AES128-GCM-SHA256';

                location / {
                    proxy_pass http://127.0.0.1:8080;
                    proxy_set_header Host $host;
                    proxy_set_header X-Real-IP $remote_addr;
                    proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
                    proxy_set_header X-Forwarded-Proto $scheme;
                }
            }

Перезапуск Nginx:

    Проверьте конфигурацию на наличие синтаксических ошибок:

        sudo nginx -t


    Перезапустите Nginx для применения изменений:

        sudo systemctl restart nginx



Безопасные практики использования SSL/TLS

    Использование современных протоколов:
        Отключите старые версии протоколов SSL и TLS (например, SSLv3, TLSv1.0, TLSv1.1) и используйте только TLSv1.2 и TLSv1.3.


    Обновление сертификатов:
        Регулярно обновляйте SSL-сертификаты, чтобы избежать их истечения.


    Сильные шифры:
        Используйте только современные и сильные алгоритмы шифрования.


    HTTP Strict Transport Security (HSTS):
        Включите HSTS для защиты от атак с понижением уровня безопасности (downgrade attacks):

            add_header Strict-Transport-Security "max-age=31536000; includeSubDomains" always;

    
    OCSP Stapling:
    
        Включите OCSP Stapling для проверки статуса SSL-сертификата:

            ssl_stapling on;
            ssl_stapling_verify on;
            resolver 8.8.8.8 8.8.4.4 valid=300s;
            resolver_timeout 5s;



Заключение

    SSL/TLS является важным компонентом безопасности веб-приложений и сетевых взаимодействий. 
    Правильная настройка и использование SSL/TLS обеспечивают конфиденциальность, целостность и аутентификацию данных, 
    передаваемых по сети. Nginx предлагает мощные инструменты для настройки и управления SSL/TLS, 
    что делает его отличным выбором для обеспечения безопасности веб-сайтов и приложений.

