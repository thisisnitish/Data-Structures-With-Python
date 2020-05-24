#Python code for Graph representation in adjacency matrix for undirected graph

class Graph:
    #Initialize the matrix
    def __init__(self, size):
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])  #initializing the matrix with 0 by default
        self.size = size
    
    #Add edges
    def add_edge(self, vertex1, vertex2):
        if vertex1 == vertex2:
            print("Same vertex %d and %d" %(vertex1, vertex2))
        self.adjMatrix[vertex1][vertex2] = 1
        self.adjMatrix[vertex2][vertex1] = 1

    #Remove edges
    def remove_edge(self, vertex1, vertex2):
        if self.adjMatrix[vertex1][vertex2] == 0:
            print("No edge is between %d and %d" %(vertex1, vertex2))
            return
        self.adjMatrix[vertex1][vertex2] = 0
        self.adjMatrix[vertex2][vertex1] = 0

    def __len__(self):
        return self.size

    #display the matrix
    def displayMatrix(self):
        print('Adjacency Matrix is: ')
        print()
        for row in self.adjMatrix:
            for val in row:
                print(val, end=' ')
            print()

#main function
if __name__ == "__main__":

    vertex = int(input('Enter the number of vertices: '))
    graph = Graph(vertex)
    
    for i in range(vertex):
        u, v = [int(x) for x in input("Enter the pairs of vertices inorder to create the edge between them: ").split()]
        graph.add_edge(u, v)
    
    graph.displayMatrix()