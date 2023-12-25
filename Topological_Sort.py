from collections import deque


def TopologicalSort(graph):
    
    
    def TopoUtil(v,visited,stack):
        visited[v] = True
        
        for neighbor in graph[v]:
            if not visited[neighbor]:
                TopoUtil(neighbor,visited,stack)
        stack.append(v)
            
    num_vertices=len(graph)
    visited=[False]*num_vertices
    stack=[]
    
    for num in range(num_vertices):
        if not visited[num]:
            TopoUtil(num,visited,stack)
    return stack[::-1]
    
    
graph = {
    0: [1, 2],
    1: [3],
    2: [3],
    3: []
}

result = TopologicalSort(graph)
print("Topological Sort:", result)