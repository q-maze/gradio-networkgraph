
import gradio as gr
from gradio_networkgraph import NetworkGraph


def on_graph_interaction(graph, event_data: gr.EventData):
    return event_data._data


with gr.Blocks() as demo:
    graph = NetworkGraph(
        value={
            "nodes": [{'id': 1, "label": "node 1"}, {'id': 2, "label": "node 2"}],
            "edges": [{"from": 1, "to": 2, "label": "edge", "id": "edge1"}],
            "options": {}
        },
        label="Static"
    )
    output = gr.Textbox()
    graph.selectNode(on_graph_interaction, inputs=[graph], outputs=[output])
    graph.deselectNode(on_graph_interaction, inputs=[graph], outputs=[output])
    graph.selectEdge(on_graph_interaction, inputs=[graph], outputs=[output])
    graph.deselectEdge(on_graph_interaction, inputs=[graph], outputs=[output])


if __name__ == "__main__":
    demo.launch()
