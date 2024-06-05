Gitflow — это рабочий процесс, разработанный Винсентом Дриссеном, который обеспечивает структурированный подход
к использованию Git в процессе разработки программного обеспечения. Gitflow помогает упорядочить работу над проектом
и организовать работу с ветками для различных этапов разработки и релизов.


Основные компоненты Gitflow

    Основные ветки:

        main (или master): Основная ветка, содержащая стабильную версию продукта, готовую к развертыванию.

        develop: Ветка для интеграции новых функций. Сюда сливаются все изменения из feature-веток.


    Поддерживающие ветки:

        Feature-ветки: Используются для разработки новых функций.

            Именование: feature/<имя-функции>

            Создание: git checkout -b feature/имя-функции develop

            Завершение: Слияние в develop (git checkout develop и git merge feature/имя-функции)


        Release-ветки: Используются для подготовки релиза, включают финальные исправления и тестирование.

            Именование: release/<версия>

            Создание: git checkout -b release/версия develop

            Завершение: Слияние в main и develop (git checkout main, git merge release/версия,
                        git checkout develop, git merge release/версия)


        Hotfix-ветки: Используются для срочного исправления ошибок в релизной версии.

            Именование: hotfix/<имя-исправления>

            Создание: git checkout -b hotfix/имя-исправления main

            Завершение: Слияние в main и develop (git checkout main, git merge hotfix/имя-исправления,
                        git checkout develop, git merge hotfix/имя-исправления)

Подробный рабочий процесс Gitflow

    Инициализация

        git init
        git checkout -b develop


    Разработка новой функции

        Создание feature-ветки:

            git checkout -b feature/awesome-feature develop


        Разработка и коммиты в feature-ветке:

            git add .
            git commit -m "Implement awesome feature"


        Слияние feature-ветки в develop:

            git checkout develop
            git merge feature/awesome-feature


    Подготовка релиза

        Создание release-ветки:

            git checkout -b release/1.0 develop


        Фиксация мелких исправлений и тестирование:

            git add .
            git commit -m "Prepare release 1.0"


        Слияние release-ветки в main и develop:

            git checkout main
            git merge release/1.0
            git tag -a 1.0 -m "Release version 1.0"
            git checkout develop
            git merge release/1.0


    Срочное исправление ошибок

        Создание hotfix-ветки:

            git checkout -b hotfix/urgent-fix main


        Исправление ошибки и коммит:

            git add .
            git commit -m "Fix urgent bug"


        Слияние hotfix-ветки в main и develop:

            git checkout main
            git merge hotfix/urgent-fix
            git tag -a 1.0.1 -m "Hotfix version 1.0.1"
            git checkout develop
            git merge hotfix/urgent-fix


Преимущества и недостатки Gitflow

    Преимущества:

        Структурированный процесс управления версиями.
        Чётко определённые роли веток для разработки, релизов и исправлений.
        Улучшенная управляемость большого числа функций и исправлений.


    Недостатки:

        Может быть избыточен для небольших проектов или команд.
        Требует дисциплины и понимания принципов работы с ветками.


Gitflow — это мощный и гибкий рабочий процесс, который помогает командам организовать работу
над проектом и улучшить управление версиями.
