from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self):
        v = (input("enter vertex"))
        if v not in self.graph:
            self.graph[v] = []
            print("vertex added")
        else:
            print("vertex already exists")

    def add_edge(self):
        u = (input("enter starting vertex"))
        v = (input("enter ending vertex"))

        if u in self.graph and v in self.graph:
            self.graph[u].append(v)
            self.graph[v].append(u)
            print("edge added")
        else:
            print("vertex does not exist")

    def display(self):
        print('\n Graph Adjacency List')
        for vertex in self.graph:
            print(vertex,'->',self.graph[vertex])

    def bfs_traversal(self):
        start = (input("enter starting vertex"))
        if start not in self.graph:
            print("vertex does not exist")
            return

        visited = set()
        queue = deque([start])

        while queue:
            node = queue.popleft()
            if node not in visited:
                print(node,end ='->')
                visited.add(node)
                for neighbor in self.graph[node]:
                    queue.append(neighbor)
        print()

    # DFS traversal
    def dfs_traversal(self):
        start = input("Enter starting vertex for DFS: ")
        if start not in self.graph:
            print("Invalid start vertex")
            return

        visited = set()
        print("DFS Traversal:")
        self.dfs_util(start, visited)
        print()

    def dfs_util(self, v, visited):
        visited.add(v)
        print(v, end=" ")
        for neighbor in self.graph[v]:
            if neighbor not in visited:
                self.dfs_util(neighbor, visited)

# -------- Menu Driven Program --------
g = Graph()

while True:
    print("\n--- Graph Menu ---")
    print("1. Add Vertex")
    print("2. Add Edge")
    print("3. Display Graph")
    print("4. BFS Traversal")
    print("5. DFS Traversal")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
         g.add_vertex()
    elif choice == 2:
        g.add_edge()
    elif choice == 3:
        g.display()
    elif choice == 4:
        g.bfs_traversal()
    elif choice == 5:
        g.dfs_traversal()
    elif choice == 6:
        print("Exiting program...")
        break
    else:
        print("Invalid choice")



