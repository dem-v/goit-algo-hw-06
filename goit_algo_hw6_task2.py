from goit_algo_hw6_task1 import RealLifeGraph
from collections import deque
from timeit import timeit


# з матеріалу уроку
def dfs_iterative(graph, start_vertex):
    visited = set()
    # Використовуємо стек для зберігання вершин
    stack = [start_vertex]
    while stack:
        # Вилучаємо вершину зі стеку
        vertex = stack.pop()
        if vertex not in visited:
            print(vertex, end=' ')
            # Відвідуємо вершину
            visited.add(vertex)
            # Додаємо сусідні вершини до стеку
            stack.extend(reversed(graph[vertex]))


# з матеріалу уроку
def bfs_iterative(graph, start):
    # Ініціалізація порожньої множини для зберігання відвіданих вершин
    visited = set()
    # Ініціалізація черги з початковою вершиною
    queue = deque([start])

    while queue:  # Поки черга не порожня, продовжуємо обхід
        # Вилучаємо першу вершину з черги
        vertex = queue.popleft()
        # Перевіряємо, чи була вершина відвідана раніше
        if vertex not in visited:
            # Якщо не була відвідана, друкуємо її
            print(vertex, end=" ")
            # Додаємо вершину до множини відвіданих вершин
            visited.add(vertex)
            # Додаємо всіх невідвіданих сусідів вершини до кінця черги
            # Операція різниці множин вилучає вже відвідані вершини зі списку сусідів
            queue.extend(set(graph[vertex]) - visited)
    # Повертаємо множину відвіданих вершин після завершення обходу
    return visited


if __name__ == "__main__":
    graph = RealLifeGraph()
    #dfs_iterative(graph.get_neighbors_dict(), 0)
    print(f"\nЧас виконання DFS: {timeit(lambda: dfs_iterative(graph.get_neighbors_dict(), 0), number=1)} секунд")
    print()
    #bfs_iterative(graph.get_neighbors_dict(), 0)
    print(f"\nЧас виконання BFS: {timeit(lambda: bfs_iterative(graph.get_neighbors_dict(), 0), number=1)} секунд")