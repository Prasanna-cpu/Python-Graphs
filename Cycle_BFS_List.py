from collections import deque


def BFSCycleList(graph, start):
    visited = [False] * len(graph)
    parent = [-1] * len(graph)
    queue = deque()

    visited[start] = [True]
    queue.append(start)

    while queue:
        current_vertex = queue.popleft()

        for neighbour in graph[current_vertex]:
            if not visited[neighbour]:
                visited[neighbour] = True
                queue.append(neighbour)
                parent[neighbour]=current_vertex
            elif parent[current_vertex]!=neighbour:
                print(f"Cycle detected at {current_vertex} -> {neighbour}")

    
graph = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1, 3],
    3: [2]
}

BFSCycleList(graph, 0)