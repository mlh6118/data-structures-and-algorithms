# Forward declaration to allow usage type in line 12.
class Vertex: ...


class Graph:

    def __init__(self):
        self.vertices = []
        self.edges = []

    # add_node takes in a value of type string and returns a type Vertex.
    def add_node(self, value: str) -> Vertex:
        vertex = Vertex(value)
        self.vertices.append(vertex)
        return vertex

    def add_edge(self):
        pass

    def get_node(self):
        pass

    def get_neighbor(self):
        pass

    def size(self) -> int:
        return len(self.vertices)


class Vertex:
    def __init__(self, value):
        self.value = value


class Edge:
    def __init__(self, vertex1, vertex2, weight=1):
        self.vertex1 = vertex1
        self.vertex2 = vertex2
        self.weight = weight


