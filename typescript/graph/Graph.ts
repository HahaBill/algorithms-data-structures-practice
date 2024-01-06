import { Vertex } from "./Vertex";

export class Graph<T> {
    num_edges: number;
    num_vertices: number;
    graph_dict: Map<number, Vertex<T>[]>;
    vertices: Vertex<T>[];

    constructor() {
        this.num_edges = 0;
        this.num_vertices = 0;
        this.graph_dict = new Map<number, Vertex<T>[]>;
        this.vertices = [];
    }

    getNumEdges(): number {
        return this.num_edges;
    }

    getNumVertices(): number {
        return this.num_vertices;
    }

    getAllVertices(): Array<Vertex<T>> {
        return this.vertices;
    }

    // getAllEdges(): Array<Set<Vertex>> {
        
    // }

    addEdge(source: Vertex<T>, destination: Vertex<T>): void {
        if(!this.graph_dict.has(source.vertex_id)) {
            this.addVertex(source);
        }
        if(!this.graph_dict.has(destination.vertex_id)) {
            this.addVertex(destination);
        }
        this.graph_dict.get(source.vertex_id)?.push(destination);
        this.graph_dict.get(destination.vertex_id)?.push(source);
        this.num_edges += 1;
    }

    addVertex(vertex: Vertex<T>): void {
        this.graph_dict.set(vertex.vertex_id, []);
        this.num_vertices += 1;
    }

    // generateEdges(): Array<Set<Vertex>> {
    //     for(var currVertex of this.vertices) {

    //     }
    // }
}