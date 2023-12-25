from collections import defaultdict,deque


def TopologicalSort(graph):
    indegree=defaultdict(int)
    queue=deque()
    result=[]
    
    for vertex in graph:
        for neighbor in graph[vertex]:
            indegree[neighbor] += 1
    
    
    for vertex in graph:
        if indegree[vertex]==0:
            queue.append(vertex)
            
    
    while queue:
        current_vertex=queue.popleft()
        result.append(current_vertex)
        
        for neighbor in graph[current_vertex]:
            indegree[neighbor]-=1
            if indegree[neighbor]==0:
                queue.append(neighbor)
                
    if len(result)<len(graph):
        return None #Graph has a cycle
    
    return result
    
    
graph = {
    0: [1, 2],
    1: [3],
    2: [3],
    3: []
}

result = TopologicalSort(graph)
if result:
    print("Topological Sort:", result)
else:
    print("Graph has a cycle, cannot perform topological sort.")
    
    
    