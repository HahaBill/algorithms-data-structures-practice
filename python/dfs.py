from graph.Graph import Graph
from graph.Vertex import Vertex

def dfs():
    pass

if __name__ == "__main__":
    graph = Graph()
    (graph.addVertex(Vertex(0, 1))
        .addVertex(Vertex(1, 1))
        .addVertex(Vertex(2, 1))
        .addVertex(Vertex(3, 1))
        .addVertex(Vertex(4, 1))
        .addVertex(Vertex(5, 1)))
    
    print(graph.getAllVertices())
