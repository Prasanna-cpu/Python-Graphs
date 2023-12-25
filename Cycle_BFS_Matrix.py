from collections import deque


def BFSCycleMatrix(graph,start):
    num_vertices=len(graph)
    visited=[False]*num_vertices
    parent=[-1]*num_vertices
    queue=deque()
      
    visited[start]=True
    queue.append(start)
    
    while queue:
        v=queue.popleft()
        
        
        for neighbour in range(num_vertices):
            if graph[v][neighbour] == 1:  # Assuming 1 represents an edge
                if not visited[neighbour]:  #if neighbor is not visited then
                    visited[neighbour]=True
                    queue.append(neighbour)
                    parent[neighbour]=v
                    
            elif parent[v]!=neighbour:
                print(f"Cycle detected at {v} -> {neighbour}")
                
                
                
adjacency_matrix = [
    [0, 1, 1, 0],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [0, 0, 1, 0]
]

BFSCycleMatrix(adjacency_matrix, 0)