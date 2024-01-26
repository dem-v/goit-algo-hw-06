from goit_algo_hw6_task1 import RealLifeGraph


def dijkstra(graph, start):
    # Ініціалізація відстаней та множини невідвіданих вершин
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.keys())

    while unvisited:
        # Знаходження вершини з найменшою відстанню серед невідвіданих
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        # Якщо поточна відстань є нескінченністю, то ми завершили роботу
        if distances[current_vertex] == float('infinity'):
            break

        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight

            # Якщо нова відстань коротша, то оновлюємо найкоротший шлях
            if distance < distances[neighbor]:
                distances[neighbor] = distance

        # Видаляємо поточну вершину з множини невідвіданих
        unvisited.remove(current_vertex)

    return distances


if __name__ == "__main__":
    graph = RealLifeGraph()
    d_w = graph.get_neighbors_dict_with_weights()
    a = dijkstra(graph.get_neighbors_dict_with_weights(), 0)
    print(f"Відстані до всіх вершин: {a}")
    z = {k for k, v in d_w.items() if len(v.items()) == 0}
    print(f"Найдовший маршрут - до кінцевих вузлів {[(z, v) for k, v in a.items() if k in z]}")
