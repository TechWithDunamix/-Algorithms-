from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

def bfs(graph, start):
    """
    Breadth-First Search Algorithm
    Time Complexity: O(V + E) where V is the number of vertices and E is the number of edges
    Space Complexity: O(V)
    
    This algorithm explores all the vertices of a graph or all the nodes of a tree 
    at the present depth before moving to the vertices at the next depth level.
    """
    visited = set()
    queue = deque([start])
    visited.add(start)
    
    while queue:
        vertex = queue.popleft()
        print(vertex, end=' ')  # Process the current node
        
        for neighbor in graph.graph.get(vertex, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Example usage
if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)
    
    print("Breadth-First Search (starting from vertex 2):")
    bfs(g, 2)
