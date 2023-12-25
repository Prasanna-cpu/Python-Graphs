def DFSCycleMatrix(adj_matrix, start, visited, parent):
    visited[start] = True

    for neighbor in range(len(adj_matrix)):
        if adj_matrix[start][neighbor] == 1:  # Assuming 1 represents an edge
            if not visited[neighbor]:
                parent[neighbor] = start
                DFSCycleMatrix(adj_matrix, neighbor, visited, parent)
            elif parent[start] != neighbor:
                # If the neighbor is already visited and not the parent, then it's a cycle
                print(f"Cycle detected: {start} -> {neighbor}")

# Example usage
adjacency_matrix = [
    [0, 1, 1, 0],
    [1, 0, 1, 0],
    [1, 1, 0, 1],
    [0, 0, 1, 0]
]

num_vertices = len(adjacency_matrix)
visited = [False] * num_vertices
parent = [-1] * num_vertices

for vertex in range(num_vertices):
    if not visited[vertex]:
        DFSCycleMatrix(adjacency_matrix, vertex, visited, parent)
