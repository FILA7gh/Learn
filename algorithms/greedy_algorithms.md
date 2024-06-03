Жадные алгоритмы — это класс алгоритмов, которые принимают локально оптимальные решения на каждом шаге
с целью найти глобально оптимальное решение. Эти алгоритмы делают выбор, который кажется наилучшим в данный момент,
без учета будущих последствий. Жадные алгоритмы часто просты в реализации и работают достаточно быстро,
однако не всегда гарантируют нахождение оптимального решения.


Основные принципы жадных алгоритмов:

    Выбор жадного критерия: На каждом шаге алгоритм выбирает наиболее оптимальный вариант по какому-то критерию.

    Неизменяемость выбора: Выбранные шаги не изменяются в будущем, даже если это приведет к не оптимальному решению.

    Оптимальное подрешение: Алгоритм опирается на предположение, что оптимальное решение для задачи можно составить
                            из локально оптимальных подрешений.


Примеры жадных алгоритмов:

    1. Задача о сдаче сдачи

        Для заданной суммы и набора номиналов монет, найти минимальное количество монет, необходимое для этой суммы.

        def coin_change(coins, amount):
            coins.sort(reverse=True)
            count = 0
            for coin in coins:
                if amount == 0:
                    break
                count += amount // coin
                amount %= coin
            return count if amount == 0 else -1

        # Пример использования
        coins = [1, 5, 10, 25]
        amount = 63
        print(coin_change(coins, amount))  # Output: 6 (25+25+10+1+1+1)


    2. Алгоритм Дейкстры

        Алгоритм для нахождения кратчайших путей от одной вершины графа до всех остальных.

        import heapq

        def dijkstra(graph, start):
            heap = [(0, start)]
            distances = {vertex: float('infinity') for vertex in graph}
            distances[start] = 0

            while heap:
                current_distance, current_vertex = heapq.heappop(heap)

                if current_distance > distances[current_vertex]:
                    continue

                for neighbor, weight in graph[current_vertex].items():
                    distance = current_distance + weight

                    if distance < distances[neighbor]:
                        distances[neighbor] = distance
                        heapq.heappush(heap, (distance, neighbor))

            return distances

        # Пример использования
        graph = {
            'A': {'B': 1, 'C': 4},
            'B': {'A': 1, 'C': 2, 'D': 5},
            'C': {'A': 4, 'B': 2, 'D': 1},
            'D': {'B': 5, 'C': 1}
        }
        start = 'A'
        print(dijkstra(graph, start))  # Output: {'A': 0, 'B': 1, 'C': 3, 'D': 4}


    3. Задача о рюкзаке (непрерывная версия)

        Для заданного веса рюкзака и набора предметов с определенными весами и ценностями, найти набор предметов,
        который максимизирует общую ценность, не превышая вес рюкзака.

        def fractional_knapsack(items, capacity):
            items.sort(key=lambda x: x[1] / x[0], reverse=True)
            total_value = 0
            for weight, value in items:
                if capacity == 0:
                    break
                if weight <= capacity:
                    capacity -= weight
                    total_value += value
                else:
                    total_value += value * (capacity / weight)
                    capacity = 0
            return total_value

        # Пример использования
        items = [(10, 60), (20, 100), (30, 120)]  # (weight, value)
        capacity = 50
        print(fractional_knapsack(items, capacity))  # Output: 240.0



Преимущества и недостатки жадных алгоритмов:

    Преимущества:

        Простота реализации.
        Быстрая работа (часто линейная или логарифмическая сложность).
        Подходят для задач, где локально оптимальные решения ведут к глобально оптимальному решению.


    Недостатки:

        Не всегда находят оптимальное решение.
        Могут не подходить для всех задач.
        Часто требуют дополнительных доказательств правильности.


Жадные алгоритмы полезны для решения широкого спектра задач, особенно когда они могут гарантировать
нахождение оптимального решения или когда приближенное решение приемлемо.
