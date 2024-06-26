Коллизии в контексте баз данных (БД) возникают, когда несколько транзакций одновременно пытаются изменить
одни и те же данные. Эти коллизии могут привести к неконсистентности данных, потере данных или другим проблемам,
если не управлять ими должным образом. Рассмотрим основные виды коллизий в базах данных и механизмы их разрешения.


Виды коллизий в базах данных

    Коллизия записи (Write-Write Conflict):
        Происходит, когда две транзакции пытаются одновременно записать (изменить) одни и те же данные.

        Пример:

            Транзакция A читает значение X.
            Транзакция B читает значение X.
            Транзакция A изменяет значение X и записывает его.
            Транзакция B изменяет старое значение X и записывает его.

        Результат: Изменения, внесённые транзакцией A, будут потеряны.


    Коллизия чтения-записи (Read-Write Conflict):
        Происходит, когда одна транзакция читает данные, которые затем изменяются другой транзакцией.

        Пример:

            Транзакция A читает значение X.
            Транзакция B изменяет значение X и записывает его.
            Транзакция A использует старое значение X для своих операций.

        Результат: Транзакция A использует устаревшие данные.


    Коллизия фантомных записей (Phantom Read):
        Происходит, когда одна транзакция читает набор строк, соответствующих некоторому критерию,
        а другая транзакция добавляет или удаляет строки, удовлетворяющие тому же критерию.

        Пример:

            Транзакция A выбирает все строки, где возраст > 30.
            Транзакция B добавляет новую строку с возрастом 35.
            Транзакция A повторяет запрос и видит больше строк, чем в первый раз.



Механизмы разрешения коллизий

    Блокировки (Locks):

        Эксклюзивная блокировка (Exclusive Lock): Запрещает другим транзакциям читать или записывать данные, 
                                                  пока блокировка не будет снята.

        Разделяемая блокировка (Shared Lock): Разрешает другим транзакциям только читать данные, но запрещает записывать.

        Пример использования блокировок:

            BEGIN TRANSACTION;
    
            -- Транзакция A
            SELECT * FROM accounts WHERE id = 1 FOR UPDATE;
    
            -- Транзакция B
            -- Это будет заблокировано, пока Транзакция A не завершится
            SELECT * FROM accounts WHERE id = 1 FOR UPDATE;
    
            COMMIT;


    Управление конкурентностью с помощью версионности (MVCC):
        В MVCC каждая транзакция видит консистентное состояние базы данных на момент её начала. 
        Это достигается хранением нескольких версий данных.

        Пример MVCC:

            В PostgreSQL используется MVCC, что позволяет транзакциям работать с "снимками" базы данных, избегая блокировок:
    
                BEGIN TRANSACTION;
                -- Транзакция A
                SELECT * FROM accounts WHERE id = 1;
        
                -- Транзакция B
                UPDATE accounts SET balance = balance + 100 WHERE id = 1;
                COMMIT;
        
                -- Транзакция A продолжает видеть старые данные
                -- до завершения своей транзакции
                COMMIT;


    Уровни изоляции транзакций:

        Read Uncommitted: Транзакция может читать данные, изменённые другими транзакциями, 
                          даже если эти изменения ещё не зафиксированы.

        Read Committed: Транзакция может читать только зафиксированные изменения.

        Repeatable Read: Транзакция видит данные такими, какими они были на момент её начала, 
                         даже если другие транзакции изменяют эти данные.

        Serializable: Самый строгий уровень изоляции, предотвращающий все виды коллизий, 
                      но может существенно снизить производительность.

        Пример установки уровня изоляции:
         
            SET TRANSACTION ISOLATION LEVEL SERIALIZABLE;
            
            BEGIN TRANSACTION;
            -- Транзакция выполняет свои операции здесь
            COMMIT;


    Оптимистические методы контроля конкурентности:
        Проверяют наличие конфликтов только в момент фиксации транзакции. 
        Если конфликты обнаружены, транзакция откатывается и может быть повторена.
        
        Пример оптимистического контроля:
         
            BEGIN TRANSACTION;
            
            -- Чтение данных
            SELECT * FROM accounts WHERE id = 1;
            
            -- Выполнение операций
            -- Предполагается, что данные не изменятся до фиксации
            
            -- Попытка фиксации транзакции
            -- Если обнаружены конфликты, транзакция откатывается
            COMMIT;



Заключение

    Коллизии в базах данных являются важным аспектом управления конкурентностью, особенно в многопользовательских системах. 
    Использование правильных механизмов разрешения коллизий, таких как блокировки, MVCC, 
    уровни изоляции транзакций и оптимистический контроль, 
    позволяет обеспечить целостность данных и высокую производительность баз данных.