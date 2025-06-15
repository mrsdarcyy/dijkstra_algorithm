import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent))  # Добавляем корень проекта в путь

import unittest
from dijkstra.graph import Graph

class TestGraph(unittest.TestCase):
    def setUp(self):
        """Создаём тестовый граф перед каждым тестом."""
        self.graph = Graph()
    
    def test_add_vertex(self):
        """Тестируем добавление вершин."""
        self.graph.add_vertex('A')
        self.graph.add_vertex('B')
        
        self.assertIn('A', self.graph.get_vertices())
        self.assertIn('B', self.graph.get_vertices())
        self.assertEqual(len(self.graph.get_vertices()), 2)
    
    def test_add_edge(self):
        """Тестируем добавление рёбер."""
        self.graph.add_edge('A', 'B', 1)
        self.graph.add_edge('A', 'C', 2)
        
        # Проверяем, что вершины добавлены
        self.assertIn('A', self.graph.get_vertices())
        self.assertIn('B', self.graph.get_vertices())
        self.assertIn('C', self.graph.get_vertices())
        
        # Проверяем, что рёбра добавлены
        self.assertEqual(self.graph.get_neighbors('A')['B'], 1)
        self.assertEqual(self.graph.get_neighbors('A')['C'], 2)
    
    def test_get_neighbors(self):
        """Тестируем получение соседей вершины."""
        self.graph.add_edge('A', 'B', 1)
        self.graph.add_edge('A', 'C', 2)
        self.graph.add_edge('B', 'D', 3)
        
        neighbors_a = self.graph.get_neighbors('A')
        neighbors_b = self.graph.get_neighbors('B')
        
        self.assertEqual(neighbors_a, {'B': 1, 'C': 2})
        self.assertEqual(neighbors_b, {'D': 3})
        self.assertEqual(self.graph.get_neighbors('D'), {})

if __name__ == "__main__":
    unittest.main()