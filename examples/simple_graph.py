import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))  # Добавляем корень проекта в путь

from dijkstra import Graph, dijkstra, shortest_path, visualize_graph

def main():
    # Создаём граф
    graph = Graph()
    
    # Добавляем вершины и рёбра (пример из википедии)
    edges = [
        ('A', 'B', 7),
        ('A', 'C', 9),
        ('A', 'F', 14),
        ('B', 'C', 10),
        ('B', 'D', 15),
        ('C', 'D', 11),
        ('C', 'F', 2),
        ('D', 'E', 6),
        ('E', 'F', 9)
    ]
    
    for from_vertex, to_vertex, weight in edges:
        graph.add_edge(from_vertex, to_vertex, weight)
    
    # Вычисляем кратчайший путь от A до E
    start, end = 'A', 'E'
    distances, previous = dijkstra(graph, start, end)
    path = shortest_path(previous, start, end)
    
    # Выводим результаты
    print(f"Кратчайшее расстояние от {start} до {end}: {distances[end]}")
    print(f"Кратчайший путь: {' -> '.join(path)}")
    
    # Визуализируем граф с путём
    visualize_graph(graph, path)

if __name__ == "__main__":
    main()