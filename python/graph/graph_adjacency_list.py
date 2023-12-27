import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from modules import Vertex, vals_to_vets


class GraphAdjList:
    """undirected graph represented by adjacency list"""

    def __init__(self, edges: list[list[Vertex]]):
        """constructor"""
        # adjacency list: key is vertex, value is list of adjacent vertices
        self.adj_list = dict[Vertex, list[Vertex]]()
        # add edges and vertices
        for edge in edges:
            self.add_vertex(edge[0])
            self.add_vertex(edge[1])
            self.add_edge(edge[0], edge[1])

    def size(self) -> int:
        """get the number of vertices"""
        return len(self.adj_list)

    def add_edge(self, vet1: Vertex, vet2: Vertex):
        """add edge"""
        # check if vet1 and vet2 are in the adjacency list and vet1 != vet2
        if vet1 not in self.adj_list or vet2 not in self.adj_list or vet1 == vet2:
            raise ValueError()
        # add edge vet1 - vet2
        self.adj_list[vet1].append(vet2)
        self.adj_list[vet2].append(vet1)

    def remove_edge(self, vet1: Vertex, vet2: Vertex):
        """remove edge"""
        if vet1 not in self.adj_list or vet2 not in self.adj_list or vet1 == vet2:
            raise ValueError()
        # remove edge vet1 - vet2
        self.adj_list[vet1].remove(vet2)
        self.adj_list[vet2].remove(vet1)

    def add_vertex(self, vet: Vertex):
        """add vertex"""
        if vet in self.adj_list:
            return
        # add a new vertex vet to the adjacency list
        self.adj_list[vet] = []

    def remove_vertex(self, vet: Vertex):
        """remove vertex"""
        if vet not in self.adj_list:
            raise ValueError()
        # delete the vertex vet from the adjacency list
        self.adj_list.pop(vet)
        # traverse the adjacency list and delete all edges containing vet
        for vertex in self.adj_list:
            if vet in self.adj_list[vertex]:
                self.adj_list[vertex].remove(vet)

    def print(self):
        """print the adjacency list"""
        print("adjacency list:")
        for vertex in self.adj_list:
            tmp = [v.val for v in self.adj_list[vertex]]
            print(f"{vertex.val}: {tmp},")


"""Driver Code"""
if __name__ == "__main__":
    # initialize an undirected graph
    v = vals_to_vets([1, 3, 2, 5, 4])
    edges = [
        [v[0], v[1]],
        [v[0], v[3]],
        [v[1], v[2]],
        [v[2], v[3]],
        [v[2], v[4]],
        [v[3], v[4]],
    ]
    graph = GraphAdjList(edges)
    print("\nafter initialization, the graph is")
    graph.print()

    # add edge
    # vertices 1, 2 are v[0], v[2]
    graph.add_edge(v[0], v[2])
    print("\nafter adding edge 1-2, the graph is")
    graph.print()

    # delete edge
    # vertices 1, 3 are v[0], v[1]
    graph.remove_edge(v[0], v[1])
    print("\nafter deleting edge 1-3, the graph is")
    graph.print()

    # add vertex
    v5 = Vertex(6)
    graph.add_vertex(v5)
    print("\nafter adding vertex 6, the graph is")
    graph.print()

    # delete vertex
    # vertex 3 is v[1]
    graph.remove_vertex(v[1])
    print("\nafter deleting vertex 3, the graph is")
    graph.print()