class Graph:
    def __init__(self):
        self.graph = {}
    
    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

def dfs(graph, start, visited=None):
    """
    Depth-First Search Algorithm
    Time Complexity: O(V + E) where V is the number of vertices and E is the number of edges
    Space Complexity: O(V)
    
    This algorithm explores as far as possible along each branch before backtracking.
    It's used for traversing or searching tree or graph data structures.
    """
    if visited is None:
        visited = set()
    
    visited.add(start)
    print(start, end=' ')  # Process the current node
    
    for neighbor in graph.graph.get(start, []):
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# Example usage
if __name__ == "__main__":
    g = Graph()
    g.add_edge(0, 1)
    g.add_edge(0, 2)
    g.add_edge(1, 2)
    g.add_edge(2, 0)
    g.add_edge(2, 3)
    g.add_edge(3, 3)
    
    print("Depth-First Search (starting from vertex 2):")
    dfs(g, 2)
