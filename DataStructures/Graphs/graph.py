class Graph():
    def __init__(self) -> None:
        self.adjacency = {}

    def add_vertex(self, *nodes):
        for node in nodes:
            if node in self.adjacency:
                return
            else:
                self.adjacency[node] = []

    def add_edge(self, *nodes):
        for node1, node2 in nodes:
            if node1 not in self.adjacency:
                print(f"Node {node1} does not exist")
            elif node2 not in self.adjacency:
                print(f"Node {node2} does not exist")
            else:
                if node1 not in self.adjacency[node1]:
                    self.adjacency[node1].append(node2)
                if node2 not in self.adjacency[node1]:
                    self.adjacency[node2].append(node1)

    def __repr__(self) -> str:
        s = ""
        for node in self.adjacency:
            s += f"{node} -> {self.adjacency[node]}\n"
        return s


g = Graph()
g.add_vertex(1, 2, 3, 4, 5)
g.add_edge((1, 2), (3, 4), (1, 5))
print(g)
