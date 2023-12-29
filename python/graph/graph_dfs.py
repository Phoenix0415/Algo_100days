import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from modules import Vertex, vets_to_vals, vals_to_vets
from graph_adjacency_list import GraphAdjList


def dfs(graph: GraphAdjList, visited: set[Vertex], res: list[Vertex], vet: Vertex):
    """Depth-First Search (DFS) helper function"""
    res.append(vet)  # Record the visited vertex
    visited.add(vet)  # Mark the vertex as visited
    # Iterate through all adjacent vertices of the current vertex
    for adjVet in graph.adj_list[vet]:
        if adjVet in visited:
            continue  # Skip already visited vertices
        # Recursively visit adjacent vertices
        dfs(graph, visited, res, adjVet)


def graph_dfs(graph: GraphAdjList, start_vet: Vertex) -> list[Vertex]:
    """Depth-First Search (DFS) - recursive"""
    # Use an adjacency list to represent the graph, making it easy to get adjacent vertices of a vertex
    # Vertex traversal sequence
    res = []
    # Hash set to keep track of visited vertices
    visited = set[Vertex]()
    dfs(graph, visited, res, start_vet)
    return res


"""Driver Code"""
if __name__ == "__main__":
    # Initialize an undirected graph
    v = vals_to_vets([0, 1, 2, 3, 4, 5, 6])
    edges = [
        [v[0], v[1]],
        [v[0], v[3]],
        [v[1], v[2]],
        [v[2], v[5]],
        [v[4], v[5]],
        [v[5], v[6]],
    ]
    graph = GraphAdjList(edges)
    print("\nAfter initialization, the graph is")
    graph.print()

    # Depth-First Search (DFS)
    res = graph_dfs(graph, v[0])
    print("\nDepth-First Search (DFS) vertex sequence:")
    print(vets_to_vals(res))