
from collections import deque

def isBipartite(graph):
    
    if not graph:
        return
    
    
    num_vertices=len(graph)
    color=[0]*num_vertices
    queue =deque()
    
    for start in range(num_vertices):
        if color[start]==0:
            queue.append(start)
            color[start]=1
            
            
            while queue:
                current=queue.popleft()
                
                for neighbor in graph[current]:
                    if color[neighbor] == 0:
                        color[neighbor]=-color[current]
                        queue.append(neighbor)
                    elif color[neighbor]==color[current]:
                        return False
            return True


graph = {
    0: [1, 3],
    1: [0, 2],
    2: [1, 3],
    3: [0, 2]
}

print(isBipartite(graph)) 
    
    