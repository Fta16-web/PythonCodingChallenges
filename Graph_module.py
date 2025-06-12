'''

'''
class Graph:
    def __init__(self, directed=False):
        """Initialize the graph."""
        self.graph = {}  # Dictionary to store the adjacency list
        self.directed = directed  # True for directed graph, False for undirected

    def add_vertex(self, vertex):
        """Add a vertex to the graph."""
        if vertex not in self.graph:
            self.graph[vertex] = []

    def add_edge(self, vertex1, vertex2):
        """Add an edge between two vertices."""
        if vertex1 not in self.graph:
            self.add_vertex(vertex1)
        if vertex2 not in self.graph:
            self.add_vertex(vertex2)

        self.graph[vertex1].append(vertex2)
        if not self.directed:
            self.graph[vertex2].append(vertex1)

    def remove_edge(self, vertex1, vertex2):
        """Remove an edge between two vertices."""
        if vertex1 in self.graph and vertex2 in self.graph[vertex1]:
            self.graph[vertex1].remove(vertex2)
        if not self.directed and vertex2 in self.graph and vertex1 in self.graph[vertex2]:
            self.graph[vertex2].remove(vertex1)

    def remove_vertex(self, vertex):
        """Remove a vertex and all connected edges."""
        if vertex in self.graph:
            # Remove edges in all connected vertices
            for connected_vertex in self.graph[vertex]:
                self.graph[connected_vertex].remove(vertex)
            # Remove the vertex
            del self.graph[vertex]

    def get_vertices(self):
        """Return a list of all vertices in the graph."""
        return list(self.graph.keys())

    def get_edges(self):
        """Return a list of all edges in the graph."""
        edges = []
        for vertex in self.graph:
            for neighbor in self.graph[vertex]:
                if self.directed or (neighbor, vertex) not in edges:
                    edges.append((vertex, neighbor))
        return edges

    def display(self):
        """Display the graph."""
        for vertex, neighbors in self.graph.items():
            print(f"{vertex} -> {', '.join(map(str, neighbors))}")
    
    def get_neighbors(self, vertex):
        """Return the list of neighbors for a given vertex."""
        return self.graph.get(vertex, [])

