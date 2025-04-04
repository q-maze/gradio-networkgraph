
import gradio as gr
from gradio_networkgraph import NetworkGraph

OPTIONS = {
    "physics": {
        "stabilization": {
            "enabled": True,
            "fit": True,
            "iterations": 100,
            "onlyDynamicEdges": True,
            "updateInterval": 50,
        },
    }
}


with gr.Blocks() as demo:
    graph_data = gr.State({
        "nodes": [],
        "edges": [],
        "options": OPTIONS
    })
    nodes = gr.State([{'id': 1, "label": "node 1"}, {'id': 2, "label": "node 2"}])
    edges = gr.State([{"from": 1, "to": 2, "label": "edge", "id": "edge1"}])

    def add_node(nodes, edges):
        max_id = max(n["id"] for n in nodes)
        nodes += [{"id": max_id+1, "label": f"Node {max_id + 1}"}]
        edges += [{"from": max_id, "to": max_id + 1}]
        return nodes, edges

    def add_node_to_graph(nodes, edges):
        return {
            "nodes": nodes,
            "edges": edges,
            "options": OPTIONS
        }

    def on_graph_event(graph, event_data: gr.EventData):
        return event_data._data

    graph = NetworkGraph(
        value={
            "nodes": nodes.value,
            "edges": edges.value,
            "options": {}
        },
        label="Static"
    )
    position_output = gr.Textbox(label="Positions:")
    selection_output = gr.Textbox(label="Selection:")
    btn = gr.Button("Add node")
    node_edge_txt = gr.Textbox(
        value=f"Nodes:\n{nodes.value}\n\nEdges:\n{edges.value}",
    )
    graph.selectNode(on_graph_event, inputs=[graph], outputs=[selection_output])
    graph.deselectNode(on_graph_event, inputs=[graph], outputs=[selection_output])
    graph.selectEdge(on_graph_event, inputs=[graph], outputs=[selection_output])
    graph.deselectEdge(on_graph_event, inputs=[graph], outputs=[selection_output])
    graph.stabilizationIterationsDone(on_graph_event, inputs=[graph], outputs=[position_output])
    graph.stabilized(on_graph_event, inputs=[graph], outputs=[position_output])
    btn.click(add_node, inputs=[nodes, edges], outputs=[nodes, edges])
    nodes.change(lambda nodes, edges: f"Nodes:\n{nodes}\n\nEdges:\n{edges}", [nodes, edges], [node_edge_txt])
    nodes.change(add_node_to_graph, [nodes, edges], [graph])


if __name__ == "__main__":
    demo.launch()
