def floyd_warshall(graph):
    """
    Floyd-Warshall Algorithm
    Time Complexity: O(V^3) where V is the number of vertices
    Space Complexity: O(V^2)
    
    This algorithm finds shortest paths in a weighted graph with positive or negative 
    edge weights (but with no negative cycles).
    """
    V = len(graph)
    dist = [row[:] for row in graph]  # Create a copy of the graph

    # Initialize the solution matrix same as input graph matrix
    # If there is no edge between i and j, set dist[i][j] = float('inf')
    for i in range(V):
        for j in range(V):
            if i != j and dist[i][j] == 0:
                dist[i][j] = float('inf')

    # Consider each vertex as an intermediate vertex
    for k in range(V):
        # Pick all vertices as source one by one
        for i in range(V):
            # Pick all vertices as destination for the above source
            for j in range(V):
                # If vertex k is on the shortest path from i to j,
                # then update the value of dist[i][j]
                dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    return dist

# Example usage
if __name__ == "__main__":
    graph = [
        [0, 5, float('inf'), 10],
        [float('inf'), 0, 3, float('inf')],
        [float('inf'), float('inf'), 0, 1],
        [float('inf'), float('inf'), float('inf'), 0]
    ]

    result = floyd_warshall(graph)
    print("Shortest distances between every pair of vertices:")
    for row in result:
        print([int(x) if x != float('inf') else 'INF' for x in row])
