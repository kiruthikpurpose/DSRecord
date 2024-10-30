class Graph:
    def __init__(self):
        self.graph = {}

    def add_node(self, node):
        if node not in self.graph:
            self.graph[node] = []

    def add_edge(self, node1, node2):
        if node1 in self.graph and node2 in self.graph:
            self.graph[node1].append(node2)
            self.graph[node2].append(node1)

    def __repr__(self):
        return str(self.graph)


n = int(input())
g = Graph()

for _ in range(n):
    operation = input().split()
    command = operation[0]

    if command == "AddNode":
        g.add_node(int(operation[1]))
    elif command == "AddEdge":
        g.add_edge(int(operation[1]), int(operation[2]))

print(g)
