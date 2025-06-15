from typing import Dict, List, Tuple, Optional
import heapq
from .graph import Graph

def dijkstra(graph: Graph, start: str, end: str) -> Tuple[Dict[str, float], Dict[str, Optional[str]]]:
    """
    Реализация алгоритма Дейкстры для поиска кратчайшего пути.
    
    Args:
        graph: Граф для поиска
        start: Начальная вершина
        end: Конечная вершина
    
    Returns:
        Кортеж из:
        - distances: словарь с кратчайшими расстояниями до всех вершин
        - previous: словарь с предыдущими вершинами для восстановления пути
    """
    # Инициализация
    distances = {vertex: float('infinity') for vertex in graph.get_vertices()}
    distances[start] = 0
    previous = {vertex: None for vertex in graph.get_vertices()}
    
    # Приоритетная очередь (min-heap)
    priority_queue = [(0, start)]
    
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        
        # Если достигли конечной вершины, можно остановиться
        if current_vertex == end:
            break
        
        # Пропускаем если нашли более короткий путь до этой вершины
        if current_distance > distances[current_vertex]:
            continue
        
        # Обход всех соседей текущей вершины
        for neighbor, weight in graph.get_neighbors(current_vertex).items():
            distance = current_distance + weight
            
            # Если найден более короткий путь до соседа
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous[neighbor] = current_vertex
                heapq.heappush(priority_queue, (distance, neighbor))
    
    return distances, previous

def shortest_path(previous: Dict[str, Optional[str]], start: str, end: str) -> List[str]:
    """
    Восстанавливает кратчайший путь из словаря previous.
    
    Args:
        previous: Словарь предыдущих вершин (из dijkstra)
        start: Начальная вершина
        end: Конечная вершина
    
    Returns:
        Список вершин, представляющий кратчайший путь
    """
    path = []
    current = end
    
    # Восстанавливаем путь от конца к началу
    while current is not None:
        path.append(current)
        current = previous.get(current, None)
    
    # Разворачиваем путь, чтобы он шёл от начала к концу
    path.reverse()
    
    # Проверяем, что путь существует
    if path[0] != start:
        return []
    
    return path