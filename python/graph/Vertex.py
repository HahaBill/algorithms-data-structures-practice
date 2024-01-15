from typing import Optional, List

class Vertex(object):

    def __init__(self, vertex_id: int, value: int, neighbours: "Optional[List[Vertex]]" = None) -> None:
        self._vertex_id = vertex_id
        self.value = value 
        self.neighbours = neighbours

    @property
    def vertex_id(self) -> int:
        return self._vertex_id
    
    def __hash__(self) -> int:
        return hash(self._vertex_id)
    
    def __eq__(self, other) -> int:
        if not isinstance(other, Vertex):
            raise Exception("An object is not a type of Vertex!")
        return self._vertex_id == other.vertex_id
