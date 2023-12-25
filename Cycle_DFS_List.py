from collections import deque

from annotated_types import Len


def DFSCycleList(graph,start,visited,parent):
    
    visited[start]=True
    for neighbor in graph[start]:
        if not visited[neighbor]:
            parent[neighbor]=start
            DFSCycleList(graph,neighbor,visited,parent)
        elif parent[start]!=neighbor:
            print(f"Cycle detected:{start}=>{neighbor}")
            
            


graph = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1, 3],
    3: [2]
}

num_vertices=len(graph)
visited=[False]*num_vertices
parent=[-1]*num_vertices

for vertex in range(num_vertices):
    if not visited[vertex]:
        DFSCycleList(graph,vertex,visited,parent)
        
