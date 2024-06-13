import math
import itertools
from heapq import heappop, heappush
from typing import Dict, List, Tuple

class Node:
    def __init__(self, label: str) -> None:
        self.label = label
        self.adjacentNodes = {}

    def add_connection(self, node: 'Node', weight: int) -> None:
        self.adjacentNodes[node] = weight

    def remove_connection(self, node: 'Node') -> None:
        if node in self.adjacentNodes:
            del self.adjacentNodes[node]

    def __lt__(self, other: 'Node') -> bool:
        #Compare nodes based on their labels
        return self.label < other.label
    
    def __repr__(self):
        return f"Node({self.label})"
    
        

class Graph:
    def __init__(self):
        self.nodes = []

    def add_node(self, node: Node) -> None:
        #Adding node to graph using the append method to the initialized node
        self.nodes.append(node)

    def remove_node(self, node: Node) -> None:
        #Removing the node from the list of nodes
        if node in self.nodes:
            self.nodes.remove(node)
        
        #Remove the connections to nodes in the list using the remove connections implemented in the node class
        for n in self.nodes:
            n.remove_connection(node)


    def add_edge(self, from_node: Node, to_node: Node, weight: int) -> None:
        #Adding edges using the add_connection implemented in the node class
        from_node.add_connection(to_node, weight)

    def dijkstra(self, source_node: Node) -> Dict[Node, int]:

        #Checking if the graph has no node to return an empty dictionary
        if not self.nodes:
            return {}
        
        
        #Initialize the distances of source node with "0" and all other nodes with infinity
        distances = {node: float('inf') for node in self.nodes}
        distances[source_node] = 0

        #Using priority queue to hold and evaluate the node with the shortest know distance
        priority_queue = [(0, source_node)]

        while priority_queue:
            current_distance, current_node = heappop(priority_queue)

            #skip the processing if the current distance is greated than the recorded distance
            if current_distance > distances[current_node]:
                continue

            #Processing each adjacent node
            for adjacent, weight in current_node.adjacentNodes.items():
                distance = current_distance + weight

                #if a shorter part to the adjacent node is found
                if distance < distances[adjacent]:
                    distances[adjacent] = distance
                    heappush(priority_queue, (distance, adjacent))

        return distances


    def kruskal(self) -> List[Tuple[int, Node, Node]]:
        #define a list to store all edges in form of (weight, node1, node2)
        edges = []

        #Ensuring that each edge is only added once in a undirecred graph
        for node in self.nodes:
            for adjacent, weight in node.adjacentNodes.items():

                if(weight, node, adjacent) not in edges and (weight, adjacent, node) not in edges:
                    edges.append((weight, node, adjacent))

        #Sorting the edges based on the weight
        edges.sort()

        #Initializing the Union-Find class to detect cycle
        uf = UnionFind(self.nodes)

        #Defining a list to store the resulting edges of the Minimum Spanning Tree
        mst = []

        #Performing iteration over sorted edges
        for weight, node1, node2, in edges:
            #Add edge to MST if it does not form a cycle
            if uf.union(node1, node2):
                mst.append((weight, node1, node2))

        #return the MST edges
        return mst
    


#Implementing a Union-Find Data Structure for the Kruskal Algorithm to detect cycle
class UnionFind:

    #Initializing the constructor of this class
    def __init__(self, nodes: List[Node]):
        self.parent = {node: node for node in nodes}
        self.rank = {node: 0 for node in nodes}
    
    #Implementing a method to find the representative root of the set containing the node
    def find(self, node: Node) -> Node:
        if self.parent[node] != node:
            self.parent[node] = self.find(self.parent[node])
        
        return self.parent[node]
    
    #Implementing a Union method to merge two sets and returns "True" if they were no cycle
    def union(self, firstNode: Node, secondNode: Node) -> bool:
        #Finding the roots of the sets for the first and second node
        root1 = self.find(firstNode)
        root2 = self.find(secondNode)

        #if they are in thesame set, a union would form a cycle, so return False
        if root1 == root2:
            return False
        
        #Union by rank: attach the smaller tree under the root to the larger tree
        if self.rank[root1] > self.rank[root2]:
            self.parent[root2] = root1
        elif self.rank[root1] < self.rank[root2]:
            self.parent[root1] = root2
        else:
            #if ranks are thesame, promote root1 and attach root2 under root1
            self.parent[root2] = root1
            self.rank[root1] += 1

        #return True as the union was successful and did not form a cycle
        return True