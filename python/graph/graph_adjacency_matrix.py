import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))
from modules import Vertex, print_matrix


class GraphAdjMat:
    """undirected graph implemented by adjacency matrix"""

    def __init__(self, vertices: list[int], edges: list[list[int]]):
        """constructor"""
        # list of vertices. its elements are vertex values, the index of each element is the vertex index
        self.vertices: list[int] = []
        # adjacency matrix, its index is the vertex index
        self.adj_mat: list[list[int]] = []
        # add vertices
        for val in vertices:
            self.add_vertex(val)
        # add edges
        # note: the edges elements represent vertex indices, that is, the index of each element in vertices
        for e in edges:
            self.add_edge(e[0], e[1])

    def size(self) -> int:
        """get the number of vertices"""
        return len(self.vertices)

    def add_vertex(self, val: int):
        """add vertex"""
        n = self.size()
        # add vertex to vertices list
        self.vertices.append(val)
        # add a row to adjacency matrix
        new_row = [0] * n
        self.adj_mat.append(new_row)
        # add a column to adjacency matrix
        for row in self.adj_mat:
            row.append(0)

    def remove_vertex(self, index: int):
        """delete vertex"""
        # if index is out of range, raise IndexError
        if index >= self.size():
            raise IndexError()
        # remove vertex from vertices list
        self.vertices.pop(index)
        # delete row of index from adjacency matrix
        self.adj_mat.pop(index)
        # delete column of index from adjacency matrix
        for row in self.adj_mat:
            row.pop(index)

    def add_edge(self, i: int, j: int):
        """add edge"""
        # parameters i, j are vertex indexes
        # if index is out of range or i == j, raise IndexError. if i == j, it means the edge is a loop
        if i < 0 or j < 0 or i >= self.size() or j >= self.size() or i == j:
            raise IndexError()
        # in undirected graph, the adjacency matrix is symmetric about the main diagonal
        self.adj_mat[i][j] = 1
        self.adj_mat[j][i] = 1

    def remove_edge(self, i: int, j: int):
        """delete edge"""
        # parameters i, j are vertex indexes
        # if index is out of range or i == j, raise IndexError. if i == j, it means the edge is a loop
        if i < 0 or j < 0 or i >= self.size() or j >= self.size() or i == j:
            raise IndexError()
        self.adj_mat[i][j] = 0
        self.adj_mat[j][i] = 0

    def print(self):
        """print adjacency matrix"""
        print("vertices =", self.vertices)
        print("adjacency matrix =")
        print_matrix(self.adj_mat)


"""Driver Code"""
if __name__ == "__main__":
    # initialize undirected graph
    # note: the edges elements represent vertex indices, that is, the index of each element in vertices
    vertices = [1, 3, 2, 5, 4]
    edges = [[0, 1], [0, 3], [1, 2], [2, 3], [2, 4], [3, 4]]
    graph = GraphAdjMat(vertices, edges)
    print("\nafter initialization, graph is")
    graph.print()

    # add edge
    # the indices of vertices 1, 2 are 0, 2 respectively
    graph.add_edge(0, 2)
    print("\nadd edge 1-2, graph is")
    graph.print()

    # delete edge
    # the indices of vertices 1, 3 are 0, 1 respectively
    graph.remove_edge(0, 1)
    print("\nafter deleting edge 1-3, graph is")
    graph.print()

    # add vertex
    graph.add_vertex(6)
    print("\nafter adding vertex 6, graph is")
    graph.print()

    # delete vertex
    # the index of vertex 3 is 1
    graph.remove_vertex(1)
    print("\nafter deleting vertex 3, graph is")
    graph.print()