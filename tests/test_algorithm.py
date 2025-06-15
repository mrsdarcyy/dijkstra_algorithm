import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))  # Добавляем корень проекта в путь

import unittest
from dijkstra.graph import Graph
from dijkstra.algorithm import dijkstra, shortest_path

class TestDijkstraAlgorithm(unittest.TestCase):
    def setUp(self):
        """Создаём тестовый граф перед каждым тестом."""
        self.graph = Graph()
        edges = [
            ('A', 'B', 1),
            ('A', 'C', 4),
            ('B', 'C', 2),
            ('B', 'D', 5),
            ('C', 'D', 1)
        ]
        for from_vertex, to_vertex, weight in edges:
            self.graph.add_edge(from_vertex, to_vertex, weight)
    
    def test_dijkstra(self):
        """Тестируем корректность работы алгоритма Дейкстры."""
        distances, previous = dijkstra(self.graph, 'A', 'D')
        
        expected_distances = {
            'A': 0,
            'B': 1,
            'C': 3,
            'D': 4
        }
        
        self.assertEqual(distances, expected_distances)
    
    def test_shortest_path(self):
        """Тестируем восстановление пути."""
        _, previous = dijkstra(self.graph, 'A', 'D')
        path = shortest_path(previous, 'A', 'D')
        
        self.assertEqual(path, ['A', 'B', 'C', 'D'])
    
    def test_no_path(self):
        """Тестируем случай, когда путь не существует."""
        graph = Graph()
        graph.add_edge('A', 'B', 1)
        graph.add_vertex('C')  # Изолированная вершина
        
        distances, previous = dijkstra(graph, 'A', 'C')
        path = shortest_path(previous, 'A', 'C')
        
        self.assertEqual(distances['C'], float('infinity'))
        self.assertEqual(path, [])

if __name__ == "__main__":
    unittest.main()