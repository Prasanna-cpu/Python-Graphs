def DirectedCycles(graph):
    num_vertices=len(graph)
    visited=[0]*num_vertices
    
    def dfs(vertex):
        visited[vertex]=1
        for neighbor in graph[vertex]:
            if visited[neighbor]==1:
                return True
            elif visited[neighbor]==0 and dfs(neighbor):
                return True
            
        visited[vertex]=2
        return False
    
    
    for vertex in range(num_vertices):
        if visited[vertex]==0 and dfs(vertex):
            return True
        return False
    
    
directed_graph = {
    0: [1],
    1: [2],
    2: [0, 3],
    3: [3]
}

print(DirectedCycles(directed_graph)) 