from typing import Optional, List, Dict, Tuple, Set
from .Vertex import Vertex

class Graph(object):

    def __init__(self, graph_dict: Optional[Dict[Vertex, List[Vertex]]] = None) -> None:
        self.num_vertices = 0
        self.num_edges = 0

        if graph_dict == None:
            graph_dict = {}
        self.graph_dict = graph_dict

    def getNumEdges(self) -> int:
        return self.num_edges
    
    def getNumVertices(self) -> int:
        return self.num_vertices
    
    def getAllVertices(self) -> List[Vertex]:
        return self.graph_dict.keys()
    
    def getAllEdges(self) -> List[List[Vertex]]:
        return self.generateAllEdges()
    
    def getEdges(self, vertex) -> List[Vertex]:
        return self.graph_dict[vertex]

    def addEdge(self, source: Vertex, destination: Vertex) -> None:
        if source not in self.graph_dict:
            self.addVertex(source)
        if destination not in self.graph_dict:
            self.addVertex(destination)

        self.graph_dict[source].append(destination)
        self.graph_dict[destination].append(source)
        self.num_edges += 1

    def addVertex(self, vertex: Vertex) -> None:
        if not isinstance(vertex, Vertex):
            raise Exception("An object is not a type of Vertex!")
        if vertex not in self.graph_dict:
            self.graph_dict[vertex] = []
            self.num_vertices += 1
        else:
            raise Exception(f"Vertex {vertex.vertex_id} is already in the graph!")
        return self
        
    def generateAllEdges(self) -> List[Set[Vertex]]:
        edges = []
        for currVertex in self.graph_dict:
            for neighbour in self.graph_dict[currVertex]:
                if {neighbour, currVertex} not in edges:
                    edges.append({currVertex, neighbour})
        return edges

    def generateAllDirectedEdges(self) -> List[Tuple[Vertex, Vertex]]:
        pass

        

