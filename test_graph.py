import pytest
import math
from graph import Node, Graph

def test_add_remove_node():
    graph = Graph()
    nodeA = Node("A")
    nodeB = Node("B")
    nodeC = Node("C")
    
    graph.add_node(nodeA)
    graph.add_node(nodeB)
    graph.add_node(nodeC)
    
    assert nodeA in graph.nodes
    assert nodeB in graph.nodes
    assert nodeC in graph.nodes
    
    graph.remove_node(nodeA)
    assert nodeA not in graph.nodes
    assert nodeB in graph.nodes
    assert nodeC in graph.nodes

def test_dijkstra():
    nodeA = Node('A')
    nodeB = Node('B')
    nodeC = Node('C')
    nodeD = Node('D')
    nodeE = Node('E')

    graph = Graph()
    graph.add_node(nodeA)
    graph.add_node(nodeB)
    graph.add_node(nodeC)
    graph.add_node(nodeD)
    graph.add_node(nodeE)

    graph.add_edge(nodeA, nodeB, 1)
    graph.add_edge(nodeA, nodeC, 4)
    graph.add_edge(nodeB, nodeC, 2)
    graph.add_edge(nodeB, nodeD, 5)
    graph.add_edge(nodeC, nodeD, 1)
    graph.add_edge(nodeD, nodeE, 3)

    distances = graph.dijkstra(nodeA)

    assert distances[nodeA] == 0
    assert distances[nodeB] == 1
    assert distances[nodeC] == 3
    assert distances[nodeD] == 4
    assert distances[nodeE] == 7

def test_dijkstra_empty_graph():
    graph = Graph()
    distances = graph.dijkstra(Node('A'))
    assert distances == {}

def test_dijkstra_single_node():
    nodeA = Node('A')
    graph = Graph()
    graph.add_node(nodeA)
    distances = graph.dijkstra(nodeA)
    assert distances[nodeA] == 0

def test_dijkstra_no_edges():
    nodeA = Node('A')
    nodeB = Node('B')
    graph = Graph()
    graph.add_node(nodeA)
    graph.add_node(nodeB)
    distances = graph.dijkstra(nodeA)
    assert distances[nodeA] == 0
    assert distances[nodeB] == float('inf')

def test_dijkstra_multiple_edges():
    nodeA = Node('A')
    nodeB = Node('B')
    nodeC = Node('C')
    nodeD = Node('D')
    nodeE = Node('E')

    graph = Graph()
    graph.add_node(nodeA)
    graph.add_node(nodeB)
    graph.add_node(nodeC)
    graph.add_node(nodeD)
    graph.add_node(nodeE)

    graph.add_edge(nodeA, nodeB, 1)
    graph.add_edge(nodeA, nodeC, 4)
    graph.add_edge(nodeB, nodeC, 2)
    graph.add_edge(nodeB, nodeD, 5)
    graph.add_edge(nodeC, nodeD, 1)
    graph.add_edge(nodeD, nodeE, 3)

    distances = graph.dijkstra(nodeA)
    assert distances[nodeA] == 0
    assert distances[nodeB] == 1
    assert distances[nodeC] == 3
    assert distances[nodeD] == 4
    assert distances[nodeE] == 7

def test_kruskal():
    nodeA = Node('A')
    nodeB = Node('B')
    nodeC = Node('C')
    nodeD = Node('D')
    nodeE = Node('E')

    graph = Graph()
    graph.add_node(nodeA)
    graph.add_node(nodeB)
    graph.add_node(nodeC)
    graph.add_node(nodeD)
    graph.add_node(nodeE)

    graph.add_edge(nodeA, nodeB, 1)
    graph.add_edge(nodeA, nodeC, 4)
    graph.add_edge(nodeB, nodeC, 2)
    graph.add_edge(nodeB, nodeD, 5)
    graph.add_edge(nodeC, nodeD, 1)
    graph.add_edge(nodeD, nodeE, 3)

    mst = graph.kruskal()

    mst_edges = set((weight, u.label, v.label) for weight, u, v in mst)
    expected_edges = {(1, 'A', 'B'), (2, 'B', 'C'), (1, 'C', 'D'), (3, 'D', 'E')}

    assert mst_edges == expected_edges

def test_kruskal_empty_graph():
    graph = Graph()
    mst = graph.kruskal()
    assert mst == []

def test_kruskal_single_node():
    nodeA = Node('A')
    graph = Graph()
    graph.add_node(nodeA)
    mst = graph.kruskal()
    assert mst == []

def test_kruskal_no_edges():
    nodeA = Node('A')
    nodeB = Node('B')
    graph = Graph()
    graph.add_node(nodeA)
    graph.add_node(nodeB)
    mst = graph.kruskal()
    assert mst == []

def test_kruskal_multiple_edges():
    nodeA = Node('A')
    nodeB = Node('B')
    nodeC = Node('C')
    nodeD = Node('D')
    nodeE = Node('E')

    graph = Graph()
    graph.add_node(nodeA)
    graph.add_node(nodeB)
    graph.add_node(nodeC)
    graph.add_node(nodeD)
    graph.add_node(nodeE)

    graph.add_edge(nodeA, nodeB, 1)
    graph.add_edge(nodeA, nodeC, 4)
    graph.add_edge(nodeB, nodeC, 2)
    graph.add_edge(nodeB, nodeD, 5)
    graph.add_edge(nodeC, nodeD, 1)
    graph.add_edge(nodeD, nodeE, 3)

    mst = graph.kruskal()
    mst_edges = set((weight, u.label, v.label) for weight, u, v in mst)
    expected_edges = {(1, 'A', 'B'), (2, 'B', 'C'), (1, 'C', 'D'), (3, 'D', 'E')}
    assert mst_edges == expected_edges

def test_kruskal_negative_weights():
    nodeA = Node('A')
    nodeB = Node('B')
    nodeC = Node('C')
    nodeD = Node('D')
    nodeE = Node('E')

    graph = Graph()
    graph.add_node(nodeA)
    graph.add_node(nodeB)
    graph.add_node(nodeC)
    graph.add_node(nodeD)
    graph.add_node(nodeE)

    graph.add_edge(nodeA, nodeB, 1)
    graph.add_edge(nodeA, nodeC, -4)
    graph.add_edge(nodeB, nodeC, 2)
    graph.add_edge(nodeB, nodeD, 5)
    graph.add_edge(nodeC, nodeD, 1)
    graph.add_edge(nodeD, nodeE, 3)

    mst = graph.kruskal()
    mst_edges = set((weight, u.label, v.label) for weight, u, v in mst)
    expected_edges = {(-4, 'A', 'C'), (1, 'C', 'D'), (1, 'A', 'B'), (3, 'D', 'E')}
    assert mst_edges == expected_edges