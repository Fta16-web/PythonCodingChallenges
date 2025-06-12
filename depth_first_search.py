'''


'''
from Graph_module import Graph
def depth_first_search(graph: Graph, start_vertex, visited=None, result=None):
    """
    Perform a depth-first search (DFS) on the graph starting from the start_vertex.
    
    Parameters:
    - graph: Graph object
    - start_vertex: The starting vertex for DFS
    - visited: A set to keep track of visited vertices (default is None)
    - result: A list to store the order of visited vertices (default is None)
    """
    if visited is None:
        visited = set()  # Initialize visited set if not provided
    if result is None:
        result = []  # Initialize result list if not provided

    visited.add(start_vertex)
    result.append(start_vertex)

    # Recursively visit each neighbor that hasn't been visited
    for neighbor in graph.get_neighbors(start_vertex):
        if neighbor not in visited:
            depth_first_search(graph, neighbor, visited, result)

    return result  # Return the order of visited vertices




import unittest

class TestDepthFirstSearch(unittest.TestCase):

    def setUp(self):
        """Set up the graph for testing."""
        self.graph = Graph(directed=False)  # Create an undirected graph
        # Add edges
        self.graph.add_edge(1, 2)
        self.graph.add_edge(1, 3)
        self.graph.add_edge(2, 4)
        self.graph.add_edge(3, 4)
        self.graph.add_edge(4, 5)

    def test_dfs_traversal(self):
        """Test DFS traversal for a connected graph."""
        expected_result = [1, 2, 4, 3, 5]  # Expected DFS order- note: The issue here is that DFS can produce different valid traversal orders depending on how the graph's 
                                            # adjacency list is stored (since sets and dictionaries don't guarantee order).
        dfs_result = depth_first_search(self.graph, start_vertex=1)
        self.assertEqual(dfs_result, expected_result)

    def test_dfs_single_vertex(self):
        """Test DFS for a graph with a single vertex."""
        single_vertex_graph = Graph()
        single_vertex_graph.add_vertex(1)
        expected_result = [1]
        dfs_result = depth_first_search(single_vertex_graph, start_vertex=1)
        self.assertEqual(dfs_result, expected_result)

    def test_dfs_disconnected_graph(self):
        """Test DFS for a disconnected graph."""
        disconnected_graph = Graph()
        disconnected_graph.add_edge(1, 2)
        disconnected_graph.add_edge(3, 4)

        # Starting DFS from vertex 1 should only visit 1 and 2
        expected_result_1 = [1, 2]
        dfs_result_1 = depth_first_search(disconnected_graph, start_vertex=1)
        self.assertEqual(dfs_result_1, expected_result_1)

        # Starting DFS from vertex 3 should only visit 3 and 4
        expected_result_2 = [3, 4]
        dfs_result_2 = depth_first_search(disconnected_graph, start_vertex=3)
        self.assertEqual(dfs_result_2, expected_result_2)

    def test_dfs_empty_graph(self):
        """Test DFS on an empty graph."""
        empty_graph = Graph()
        dfs_result = depth_first_search(empty_graph, start_vertex=1)
        self.assertEqual(dfs_result, [1])  # Should just return the starting vertex if nothing else is there

    def test_dfs_non_existent_vertex(self):
        """Test DFS starting from a vertex that doesn't exist."""
        dfs_result = depth_first_search(self.graph, start_vertex=99)
        self.assertEqual(dfs_result, [99])  # Non-existent vertex should just return itself

if __name__ == '__main__':
    unittest.main()
