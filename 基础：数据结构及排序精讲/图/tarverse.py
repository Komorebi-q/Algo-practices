class Vertex:
    def __init__(self, id = 0, neighbors=None):
        self.id = id
        self.neighbors = neighbors if neighbors is not None else []

def traverse_graph(s: Vertex, visited: List[Bool]):
    if s is None:
        return 
    if visited[s.id]:
        return
    
    visited[s.id] = True
    print('visited vertex: ', s.id)
    # pre order
    for neighbor in s.neighbors:
        traverse_graph(neighbor, visited)
    # post order
    
class Node:
    def __init__(self, val=0, children=None):
        self.val = val
        self.children = children if children is not None else []
    
def traverse_edge(s, visited):
    if s is None:
        return
    
    for neighbor in s.neighbors:
        if visited[s.id][neighbor.id]:
            continue
        print(f"visited edge: {s.id} -> {neighbor.id}")
        visited[s.id][neighbor.id] = True
        traverse_edge(neighbor, visited)
    
graph = []
on_path = [False] * len(graph)
path = []

# 遍历 src -> dest 的所有路径
def traverse_path(graph, src, dest):
    if src.id < 0 or src.id >= len(graph):
        return 
    if on_path[src.id]: 
        return
    if src.id == dest.id:
        print(f'find path: {'->'.join(map(str, path))} -> {dest}' )
        return
    
    on_path[src.id] = True
    path.append(src)
    for neighbor in graph[src.id]:
        traverse_path(graph, neighbor, dest)
    # 回溯 
    path.pop()
    on_path[src.id] = False