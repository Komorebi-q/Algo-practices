# https://labuladong.online/zh/algo/data-structure-basic/graph-basic/

from abc import ABC, abstractmethod
from multiprocessing import set_forkserver_preload


class Vertex:
    def __init__(self, id: int):
        self.id = id
        self.neighbors = []


class TreeNode:
    def __init__(self, val: int, children=None):
        self.val = val
        self.children = children if children is not None else []


class Edge:
    def __init__(self, to: int, weight: int):
        self.to = to
        self.weight = weight


graph: list[list[Edge]] = []
matrix: list[list[int]] = []


class Graph(ABC):
    @abstractmethod
    def add_edge(self, from_vertex: int, to_vertex: int, weight: int):
        pass

    @abstractmethod
    def remove_edge(self, from_vertex: int, to_vertex: int):
        pass

    @abstractmethod
    def has_edge(self, from_vertex: int, to_vertex: int) -> bool:
        pass

    @abstractmethod
    def weight(self, from_vertex: int, to_vertex: int) -> int:
        pass

    @abstractmethod
    def neighbors(self, vertex: int) -> list[int]:
        pass

    @abstractmethod
    def size(self) -> int:
        pass


class WeightedGraph:
    class Edge:
        def __init__(self, to: int, weight: int):
            self.to = to
            self.weight = weight

    def __init__(self, n: int):
        self.graph = [[] for _ in range(n)]

    def add_edge(self, from_vertex: int, to_vertex: int, weight: int):
        self.graph[from_vertex].append(self.Edge(to_vertex, weight))

    def remove_edge(self, from_vertex: int, to_vertex: int):
        self.graph[from_vertex] = [
            edge for edge in self.graph[from_vertex] if edge.to != to_vertex
        ]

    def has_edge(self, from_vertex: int, to_vertex: int):
        for edge in self.graph[from_vertex]:
            if edge.to == to_vertex:
                return True

        return False

    def weight(self, from_vertex: int, to_vertex: int):
        for edge in self.graph[from_vertex]:
            if edge.to == to_vertex:
                return edge.weight

        return None

    def neighbors(self, vertex: int):
        return self.graph[vertex]

    def size(self):
        return len(self.graph)


class WeightedGraphMatrix:
    class Edge:
        def __init__(self, to: int, weight: int):
            self.to = to
            self.weight = weight

    def __init__(self, n: int):
        self.matrix = [[0] * n for _ in range(n)]

    def add_edge(self, from_vertex: int, to_vertex: int, weight: int):
        self.matrix[from_vertex][to_vertex] = weight

    def remove_edge(self, from_vertex: int, to_vertex: int):
        self.matrix[from_vertex][to_vertex] = 0

    def has_edge(self, from_vertex: int, to_vertex: int):
        return self.matrix[from_vertex][to_vertex] != 0

    def weight(self, from_vertex: int, to_vertex: int):
        return self.matrix[from_vertex][to_vertex]

    def neighbors(self, vertex: int):
        res = []

        for i in range(len(self.matrix[vertex])):
            weight = self.matrix[vertex][i]

            if weight != 0:
                res.append(self.Edge(i, weight))

        return res

    def size(self):
        return len(self.matrix)


class WeightedUndigraph:
    def __init__(self, n: int):
        self.graph = WeightedGraph(n)

    def add_edge(self, from_vertex: int, to_vertex: int, weight: int):
        self.graph.add_edge(from_vertex, to_vertex, weight)
        self.graph.add_edge(to_vertex, from_vertex, weight)

    def remove_edge(self, from_vertex: int, to_vertex: int):
        self.graph.remove_edge(from_vertex, to_vertex)
        self.graph.remove_edge(to_vertex, from_vertex)

    def has_edge(self, from_vertex: int, to_vertex: int) -> bool:
        return self.graph.has_edge(from_vertex, to_vertex)

    def weight(self, from_vertex: int, to_vertex: int) -> int:
        return self.graph.weight(from_vertex, to_vertex)

    def neighbors(self, vertex: int):
        return self.graph.neighbors(vertex)


if __name__ == "__main__":
    graph = WeightedGraphMatrix(3)
    graph.add_edge(0, 1, 1)
    graph.add_edge(1, 2, 2)
    graph.add_edge(2, 0, 3)
    graph.add_edge(2, 1, 4)

    print(graph.has_edge(0, 1))
    print(graph.has_edge(1, 0))

    for edge in graph.neighbors(2):
        print(f"{2} -> {edge.to} (weight: {edge.weight})")

    graph.remove_edge(0, 1)
    print(graph.has_edge(0, 1))
