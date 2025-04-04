
import gradio as gr
from app import demo as app
import os

_docs = {'NetworkGraph': {'description': 'A base class for defining methods that all input/output components should have.', 'members': {'__init__': {'value': {'type': 'Any', 'default': 'None', 'description': None}, 'label': {'type': 'str | None', 'default': 'None', 'description': None}, 'info': {'type': 'str | None', 'default': 'None', 'description': None}, 'show_label': {'type': 'bool | None', 'default': 'None', 'description': None}, 'container': {'type': 'bool', 'default': 'True', 'description': None}, 'scale': {'type': 'int | None', 'default': 'None', 'description': None}, 'min_width': {'type': 'int | None', 'default': 'None', 'description': None}, 'interactive': {'type': 'bool | None', 'default': 'None', 'description': None}, 'visible': {'type': 'bool', 'default': 'True', 'description': None}, 'elem_id': {'type': 'str | None', 'default': 'None', 'description': None}, 'elem_classes': {'type': 'list[str] | str | None', 'default': 'None', 'description': None}, 'render': {'type': 'bool', 'default': 'True', 'description': None}, 'key': {'type': 'int | str | None', 'default': 'None', 'description': None}, 'load_fn': {'type': 'Callable | None', 'default': 'None', 'description': None}, 'every': {'type': 'Timer | float | None', 'default': 'None', 'description': None}, 'inputs': {'type': 'Component | Sequence[Component] | set[Component] | None', 'default': 'None', 'description': None}}, 'postprocess': {}, 'preprocess': {}}, 'events': {'selectNode': {'type': None, 'default': None, 'description': ''}, 'deselectNode': {'type': None, 'default': None, 'description': ''}, 'selectEdge': {'type': None, 'default': None, 'description': ''}, 'deselectEdge': {'type': None, 'default': None, 'description': ''}, 'stabilizationIterationsDone': {'type': None, 'default': None, 'description': ''}, 'stabilized': {'type': None, 'default': None, 'description': ''}}}, '__meta__': {'additional_interfaces': {}}}

abs_path = os.path.join(os.path.dirname(__file__), "css.css")

with gr.Blocks(
    css=abs_path,
    theme=gr.themes.Default(
        font_mono=[
            gr.themes.GoogleFont("Inconsolata"),
            "monospace",
        ],
    ),
) as demo:
    gr.Markdown(
"""
# `gradio_networkgraph`

<div style="display: flex; gap: 7px;">
<a href="https://pypi.org/project/gradio_networkgraph/" target="_blank"><img alt="PyPI - Version" src="https://img.shields.io/pypi/v/gradio_networkgraph"></a>  
</div>

Gradio component for displaying vis.js network visualizations.
""", elem_classes=["md-custom"], header_links=True)
    app.render()
    gr.Markdown(
"""
## Installation

```bash
pip install gradio_networkgraph
```

## Usage

```python

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

```
""", elem_classes=["md-custom"], header_links=True)


    gr.Markdown("""
## `NetworkGraph`

### Initialization
""", elem_classes=["md-custom"], header_links=True)

    gr.ParamViewer(value=_docs["NetworkGraph"]["members"]["__init__"], linkify=[])


    gr.Markdown("### Events")
    gr.ParamViewer(value=_docs["NetworkGraph"]["events"], linkify=['Event'])







    demo.load(None, js=r"""function() {
    const refs = {};
    const user_fn_refs = {};
    requestAnimationFrame(() => {

        Object.entries(user_fn_refs).forEach(([key, refs]) => {
            if (refs.length > 0) {
                const el = document.querySelector(`.${key}-user-fn`);
                if (!el) return;
                refs.forEach(ref => {
                    el.innerHTML = el.innerHTML.replace(
                        new RegExp("\\b"+ref+"\\b", "g"),
                        `<a href="#h-${ref.toLowerCase()}">${ref}</a>`
                    );
                })
            }
        })

        Object.entries(refs).forEach(([key, refs]) => {
            if (refs.length > 0) {
                const el = document.querySelector(`.${key}`);
                if (!el) return;
                refs.forEach(ref => {
                    el.innerHTML = el.innerHTML.replace(
                        new RegExp("\\b"+ref+"\\b", "g"),
                        `<a href="#h-${ref.toLowerCase()}">${ref}</a>`
                    );
                })
            }
        })
    })
}

""")

demo.launch()
