---
tags: [gradio-custom-component, ]
title: gradio_networkgraph
short_description: Gradio component for displaying vis.js network visualizations.
colorFrom: blue
colorTo: yellow
sdk: gradio
pinned: false
app_file: space.py
---

# `gradio_networkgraph`
<a href="https://pypi.org/project/gradio_networkgraph/" target="_blank"><img alt="PyPI - Version" src="https://img.shields.io/pypi/v/gradio_networkgraph"></a>  

Gradio component for displaying vis.js network visualizations.

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

## `NetworkGraph`

### Initialization

<table>
<thead>
<tr>
<th align="left">name</th>
<th align="left" style="width: 25%;">type</th>
<th align="left">default</th>
<th align="left">description</th>
</tr>
</thead>
<tbody>
<tr>
<td align="left"><code>value</code></td>
<td align="left" style="width: 25%;">

```python
Any
```

</td>
<td align="left"><code>None</code></td>
<td align="left">None</td>
</tr>

<tr>
<td align="left"><code>label</code></td>
<td align="left" style="width: 25%;">

```python
str | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">None</td>
</tr>

<tr>
<td align="left"><code>info</code></td>
<td align="left" style="width: 25%;">

```python
str | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">None</td>
</tr>

<tr>
<td align="left"><code>show_label</code></td>
<td align="left" style="width: 25%;">

```python
bool | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">None</td>
</tr>

<tr>
<td align="left"><code>container</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>True</code></td>
<td align="left">None</td>
</tr>

<tr>
<td align="left"><code>scale</code></td>
<td align="left" style="width: 25%;">

```python
int | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">None</td>
</tr>

<tr>
<td align="left"><code>min_width</code></td>
<td align="left" style="width: 25%;">

```python
int | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">None</td>
</tr>

<tr>
<td align="left"><code>interactive</code></td>
<td align="left" style="width: 25%;">

```python
bool | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">None</td>
</tr>

<tr>
<td align="left"><code>visible</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>True</code></td>
<td align="left">None</td>
</tr>

<tr>
<td align="left"><code>elem_id</code></td>
<td align="left" style="width: 25%;">

```python
str | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">None</td>
</tr>

<tr>
<td align="left"><code>elem_classes</code></td>
<td align="left" style="width: 25%;">

```python
list[str] | str | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">None</td>
</tr>

<tr>
<td align="left"><code>render</code></td>
<td align="left" style="width: 25%;">

```python
bool
```

</td>
<td align="left"><code>True</code></td>
<td align="left">None</td>
</tr>

<tr>
<td align="left"><code>key</code></td>
<td align="left" style="width: 25%;">

```python
int | str | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">None</td>
</tr>

<tr>
<td align="left"><code>load_fn</code></td>
<td align="left" style="width: 25%;">

```python
Callable | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">None</td>
</tr>

<tr>
<td align="left"><code>every</code></td>
<td align="left" style="width: 25%;">

```python
Timer | float | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">None</td>
</tr>

<tr>
<td align="left"><code>inputs</code></td>
<td align="left" style="width: 25%;">

```python
Component | Sequence[Component] | set[Component] | None
```

</td>
<td align="left"><code>None</code></td>
<td align="left">None</td>
</tr>
</tbody></table>


### Events

| name | description |
|:-----|:------------|
| `selectNode` |  |
| `deselectNode` |  |
| `selectEdge` |  |
| `deselectEdge` |  |
| `stabilizationIterationsDone` |  |
| `stabilized` |  |



