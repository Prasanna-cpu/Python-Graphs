from collections import deque


def isBipartite(graph):
    if not graph:
        return True

    V = len(graph)
    color = [0] * V
    queue = deque()

    for start in range(V):
        if color[start] == 0:
            color[start] = 1
            queue.append(start)
            while queue:
                current = queue.popleft()

                for neighbor in graph[current]:
                    if graph[current][neighbor] == 1 :
                        if color[neighbor] == 0:
                           color[neighbor] = -color[current]
                           queue.append(neighbor)
                        elif color[neighbor]==color[current]:
                            return False
    return True


adjacency_matrix = [
    [0, 1, 0, 1],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 0, 1, 0]
]

print(isBipartite(adjacency_matrix))
                        

            
        