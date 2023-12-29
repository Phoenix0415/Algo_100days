import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from modules import Vertex, vals_to_vets, vets_to_vals
from collections import deque
from graph_adjacency_list import GraphAdjList


def graph_bfs(graph: GraphAdjList, start_vet: Vertex) -> list[Vertex]:
    """breadth first search - BFS"""
    # using adjacency list to represent graph, which is easy to get all adjacent vertexes of a vertex
    # traversal sequence of vertexes
    res = []
    # hashmap to record visited vertexes. using set to avoid duplicate vertexes
    # # Initialize a haspmap using set to keep track of visited vertexes, starting with the initial vertex.
    # python使用set()创建集合时需要将元素放在一个可迭代的对象中，比如列表，如果不加[]会报错，因为start_vet不是一个可迭代的对象。
    visited = set[Vertex]([start_vet])
    # # Initialize a queue with the initial vertex to record vertexes to be visited.
    que = deque[Vertex]([start_vet])
    # # Continue the traversal as long as there are vertexes in the queue.
    while len(que) > 0:
        vet = que.popleft()  # dequeue a vertex from the front of the queue
        res.append(vet)  # Record the visited vertex.
        
        # Iterate through all adjacent vertices of the current vertex (vet)
        for adj_vet in graph.adj_list[vet]:
            if adj_vet in visited:
                continue  # Skip vertices that have already been visited
            que.append(adj_vet)  # Enqueue unvisited adjacent vertices
            visited.add(adj_vet)  # Mark the adjacent vertex as visited
    # Return the traversal sequence of vertexes
    return res


"""Driver Code"""
if __name__ == "__main__":
    # initialize a undirected graph
    v = vals_to_vets([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
    edges = [
        [v[0], v[1]],
        [v[0], v[3]],
        [v[1], v[2]],
        [v[1], v[4]],
        [v[2], v[5]],
        [v[3], v[4]],
        [v[3], v[6]],
        [v[4], v[5]],
        [v[4], v[7]],
        [v[5], v[8]],
        [v[6], v[7]],
        [v[7], v[8]],
    ]
    graph = GraphAdjList(edges)
    print("\nafter initialization, the graph is")
    graph.print()

    # breadth first search - BFS
    res = graph_bfs(graph, v[0])
    print("\nthe breadth first search - BFS result is")
    print(vets_to_vals(res))