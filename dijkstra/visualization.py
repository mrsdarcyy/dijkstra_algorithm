import networkx as nx
import matplotlib.pyplot as plt
from typing import List, Dict, Optional
from .graph import Graph

def visualize_graph(graph: Graph, path: Optional[List[str]] = None) -> None:
    """
    Визуализирует граф с помощью networkx и matplotlib.
    
    Args:
        graph: Граф для визуализации
        path: Опциональный список вершин, представляющий путь для выделения
    """
    # Создаём directed graph в networkx
    nx_graph = nx.DiGraph()
    
    # Добавляем вершины и рёбра
    for vertex in graph.get_vertices():
        nx_graph.add_node(vertex)
    
    for from_vertex in graph.get_vertices():
        for to_vertex, weight in graph.get_neighbors(from_vertex).items():
            nx_graph.add_edge(from_vertex, to_vertex, weight=weight)
    
    # Позиционирование вершин
    pos = nx.spring_layout(nx_graph)
    
    # Рисуем граф
    plt.figure(figsize=(10, 8))
    
    # Устанавливаем цвета по умолчанию
    node_colors = ['skyblue' for _ in nx_graph.nodes()]
    edge_colors = ['black' for _ in nx_graph.edges()]
    
    # Если задан путь, меняем цвета соответствующих вершин и рёбер
    if path:
        node_colors = ['red' if node in path else 'skyblue' for node in nx_graph.nodes()]
        path_edges = list(zip(path, path[1:]))
        edge_colors = ['red' if (u, v) in path_edges else 'black' for u, v in nx_graph.edges()]
    
    # Рисуем вершины
    nx.draw_networkx_nodes(nx_graph, pos, node_size=700, node_color=node_colors)
    
    # Рисуем рёбра
    nx.draw_networkx_edges(nx_graph, pos, width=2, edge_color=edge_colors, arrows=True)
    
    # Рисуем метки вершин
    nx.draw_networkx_labels(nx_graph, pos, font_size=12, font_family='sans-serif')
    
    # Рисуем веса рёбер
    edge_labels = nx.get_edge_attributes(nx_graph, 'weight')
    nx.draw_networkx_edge_labels(nx_graph, pos, edge_labels=edge_labels)
    
    title = "Граф с кратчайшим путём (алгоритм Дейкстры)" if path else "Граф (алгоритм Дейкстры)"
    plt.title(title)
    plt.axis('off')
    plt.tight_layout()
    plt.show()