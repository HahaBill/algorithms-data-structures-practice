export class Vertex<T> {
    readonly vertex_id: number;
    value: number;
    neighbours: Vertex<T>[];

    constructor(vertex_id: number, value: number) {
        this.vertex_id = vertex_id;
        this.value = value;
        this.neighbours = []
    }
}