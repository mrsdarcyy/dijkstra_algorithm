from typing import Dict, List, Optional, Tuple
import math

class Graph:
    """Класс для представления взвешенного графа с использованием adjacency list."""
    
    def __init__(self):
        self.vertices: Dict[str, Dict[str, float]] = {}
    
    def add_vertex(self, name: str) -> None:
        """Добавляет вершину в граф, если её ещё нет."""
        if name not in self.vertices:
            self.vertices[name] = {}
    
    def add_edge(self, from_vertex: str, to_vertex: str, weight: float) -> None:
        """
        Добавляет направленное ребро между вершинами с заданным весом.
        
        Args:
            from_vertex: Начальная вершина ребра
            to_vertex: Конечная вершина ребра
            weight: Вес ребра (расстояние между вершинами)
        """
        self.add_vertex(from_vertex)
        self.add_vertex(to_vertex)
        self.vertices[from_vertex][to_vertex] = weight
    
    def get_neighbors(self, vertex: str) -> Dict[str, float]:
        """Возвращает соседей вершины и веса рёбер."""
        return self.vertices.get(vertex, {})
    
    def get_vertices(self) -> List[str]:
        """Возвращает список всех вершин графа."""
        return list(self.vertices.keys())
    
    def __repr__(self) -> str:
        return f"Graph({self.vertices})"