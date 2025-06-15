import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))  # Добавляем корень проекта в путь

from dijkstra import Graph, dijkstra, shortest_path, visualize_graph

def main():
    # Создаём более сложный граф
    graph = Graph()
    
    # Добавляем вершины и рёбра
    edges = [
        ('A', 'B', 4),
        ('A', 'C', 2),
        ('B', 'C', 1),
        ('B', 'D', 5),
        ('C', 'D', 8),
        ('C', 'E', 10),
        ('D', 'E', 2),
        ('D', 'F', 6),
        ('E', 'F', 3),
        ('F', 'G', 5),
        ('G', 'H', 1),
        ('H', 'I', 4),
        ('I', 'J', 7),
        ('J', 'A', 3)
    ]
    
    for from_vertex, to_vertex, weight in edges:
        graph.add_edge(from_vertex, to_vertex, weight)
        # Добавляем обратные рёбра для неориентированного графа
        graph.add_edge(to_vertex, from_vertex, weight)
    
    # Вычисляем кратчайший путь от A до J
    start, end = 'A', 'J'
    distances, previous = dijkstra(graph, start, end)
    path = shortest_path(previous, start, end)
    
    # Выводим результаты
    print(f"Кратчайшее расстояние от {start} до {end}: {distances[end]}")
    print(f"Кратчайший путь: {' -> '.join(path)}")
    
    # Визуализируем граф с путём
    visualize_graph(graph, path)

if __name__ == "__main__":
    main()