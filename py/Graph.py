# Graph class
class Graph:
    # Graph constructor
    def __init__(self, V):
        # Number of vertices and the adjacency lists are set
        self.V = V
        self.adj = [[] for i in range(V)]
    # Function to add an edge to the graph
    def addEdge(self, v, w):
        # Adds a Node to the Adjacency List specified
        self.adj[v].append(w)
    # Function that does the Depth First Search Algorithm on the Graph
    def DFS(self, i):
        # A VHS-Visited Hash Set, Stack, and a DFS list are created
        VHS = set()
        Stack = []
        DFS = []
        # The starting element is added to the stack and the VHS
        Stack.append(i)
        VHS.add(i)
        # Loop that iterates while the Stack isn't empty
        while Stack:
            # Var is the element popped out from the stack and it's added to the DFS list
            Var = Stack.pop()
            DFS.append(Var)
            # Loop that goes through each Node in an adjacency list
            for j in range(len(self.adj[Var])):
                # Checks if the Node in the adjacency list is in the VHS
                if self.adj[Var][j] in VHS:
                    continue
                # Adds the Node to the Stack and VHS if the Node isn't in the VHS
                else:
                    Stack.append(self.adj[Var][j])
                    VHS.add(self.adj[Var][j])
        # Returns the DFS list
        return DFS
# Create a Graph
g = Graph(6)
# Add edges and vertices to the graph
g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(2, 3)
g.addEdge(2, 4)
g.addEdge(4, 5)
g.addEdge(1, 3)
g.addEdge(3, 5)
# Calling the DFS function with the existing graph
print(g.DFS(0))