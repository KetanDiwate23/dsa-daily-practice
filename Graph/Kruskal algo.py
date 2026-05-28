class Graph:

    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    # Add edge
    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    # Find set of an element
    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    # Union of two sets
    def union(self, parent, rank, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)

        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y

        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x

        else:
            parent[root_y] = root_x
            rank[root_x] += 1

    # Kruskal Algorithm
    def kruskal_mst(self):

        result = []

        i = 0  # index for sorted edges
        e = 0  # number of edges in MST

        # Sort edges according to weight
        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = []
        rank = []

        # Create disjoint sets
        for node in range(self.V+1):
            parent.append(node)
            rank.append(0)

        # Process edges
        while e < self.V - 1:

            u, v, w = self.graph[i]
            i += 1

            x = self.find(parent, u)
            y = self.find(parent, v)

            # Add edge if no cycle formed
            if x != y:
                e += 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        # Print MST
        total_cost = 0

        print("\nEdges in Minimum Spanning Tree:")
        print("Edge \tWeight")

        for u, v, weight in result:
            total_cost += weight
            print(f"{u} - {v}\t{weight}")

        print("\nMinimum Spanning Tree Cost =", total_cost)


# User Input
vertices = int(input("Enter number of vertices: "))
edges = int(input("Enter number of edges: "))

g = Graph(vertices)

print("Enter edges in format: source destination weight")

for _ in range(edges):
    u, v, w = map(int, input().split())
    g.add_edge(u, v, w)

# Run Kruskal Algorithm
g.kruskal_mst()