import heapq

def dijkstra(graph, start):
    """
    Dijkstra's Algorithm
    Time Complexity: O((V + E) log V) where V is the number of vertices and E is the number of edges
    Space Complexity: O(V)
    
    This algorithm finds the shortest paths between nodes in a graph, which may represent, 
    for example, road networks.
    """
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    pq = [(0, start)]
    
    while pq:
        current_distance, current_vertex = heapq.heappop(pq)
        
        # If we've found a longer path, ignore it
        if current_distance > distances[current_vertex]:
            continue
        
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight
            
            # If we've found a shorter path, update it
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))
    
    return distances

# Example usage
if __name__ == "__main__":
    graph = {
        'A': {'B': 4, 'C': 2},
        'B': {'D': 3, 'E': 1},
        'C': {'B': 1, 'D': 5},
        'D': {'E': 2},
        'E': {}
    }
    start_vertex = 'A'
    shortest_distances = dijkstra(graph, start_vertex)
    print(f"Shortest distances from vertex {start_vertex}:")
    for vertex, distance in shortest_distances.items():
        print(f"To {vertex}: {distance}")
