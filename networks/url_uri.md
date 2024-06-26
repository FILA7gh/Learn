
URL (Uniform Resource Locator) и URI (Uniform Resource Identifier) — это два термина,
которые часто используются в контексте веб-адресов, но они имеют разные значения и области применения.


URL (Uniform Resource Locator)

URL — это подмножество URI, которое предоставляет способ указания адреса ресурса и протокола для его доступа.
URL обычно используется для указания веб-страниц и других интернет-ресурсов.

Структура URL:

    scheme://userinfo@host:port/path?query#fragment

        scheme: Протокол для доступа к ресурсу (например, HTTP, HTTPS, FTP).

        userinfo: Опциональная часть, включающая имя пользователя и пароль, разделенные двоеточием (например, user:password).

        host: Доменное имя или IP-адрес сервера, на котором находится ресурс.

        port: Опциональная часть, указывающая номер порта для доступа к ресурсу (например, :80 для HTTP).

        path: Путь к ресурсу на сервере (например, /path/to/resource).

        query: Опциональная часть, включающая параметры запроса (например, ?key1=value1&key2=value2).

        fragment: Опциональная часть, включающая идентификатор фрагмента документа (например, #section1).


Пример URL:

    https://user:password@example.com:8080/path/to/resource?key1=value1&key2=value2#section1



URI (Uniform Resource Identifier)

URI — это более общий термин, который включает в себя и URL, и URN (Uniform Resource Name).
URI служит для уникальной идентификации ресурса. URI может быть URL (если указывает способ доступа к ресурсу)
или URN (если указывает уникальное имя ресурса без указания способа доступа).

Виды URI:

    URL (Uniform Resource Locator): Идентификатор, который указывает способ доступа к ресурсу.

    URN (Uniform Resource Name): Идентификатор, который указывает уникальное имя ресурса, не привязываясь к способу его получения.


Пример URN:

    urn:isbn:0451450523

    Этот URN указывает на уникальную книгу по ее международному стандартному номеру книги (ISBN).
    Отличия между URL и URI:
    
URL — это подмножество URI, которое содержит информацию о том, как и где получить доступ к ресурсу.
URI — это общий идентификатор ресурса, который может быть либо URL, либо URN.


Примеры использования:

    URL: Используется для указания веб-адресов, к которым можно получить доступ через браузер или другие клиентские приложения.

        https://www.example.com/index.html

    
    URN: Используется для указания уникальных имен, таких как ISBN для книг или DOI для научных статей.
    
        urn:ietf:rfc:2141


Заключение

    URL (Uniform Resource Locator) предоставляет способ указания местоположения ресурса и способа его доступа.
    
    URI (Uniform Resource Identifier) является более общим понятием, включающим как URL, так и URN, 
    и служит для уникальной идентификации ресурса.



Понимание разницы между URL и URI помогает лучше понять, 
как работают веб-адреса и как можно обращаться к ресурсам в интернете.
