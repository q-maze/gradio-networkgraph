<script lang="ts">
    import type { Gradio } from "@gradio/utils";
    import { onMount, onDestroy } from "svelte";
    import { Network } from "vis-network";

    export let gradio: Gradio;
    export let nodes;
    export let edges;
    export let options;
    export let selectedNodes = []
    export let selectedEdges = []
    export let nodePositions = []

    let container;
    let network;
  
    onMount(() => {
      if (!container) return;
  
      // Set up the network
      const data = { nodes, edges, options };
      network = new Network(container, data);

      function sendData(params) {
        selectedNodes = params.nodes;
        selectedEdges = params.edges.map(
          (edgeId) => network.getConnectedNodes(edgeId)
        );
        nodePositions = network.getPositions();
        return {"nodes": selectedNodes, "edges": selectedEdges, "nodePositions": nodePositions}
      }

      function selectNode(params) {
        let selectedNodes = params.nodes;
        if (selectedNodes.length > 0) {
          const selectedNodeId = selectedNodes[0];
          network.focus(
            selectedNodeId,
            {
              scale: 1.5,
              animation: {
                duration: 500,
                easingFunction: "easeInOutQuad",
              }
            }
          )
          gradio.dispatch("selectNode", sendData(params))
        }
      }

      function deselectNode(params) {
        gradio.dispatch("deselectNode", sendData(params))
      }

      function selectEdge(params) {
        gradio.dispatch("selectEdge", sendData(params))
      }

      function deselectEdge(params) {
        gradio.dispatch("deselectEdge", sendData(params))
      }

      // Event Listeners
      network.on("selectNode", selectNode);
      network.on("deselectNode", deselectNode);
      network.on("selectEdge", selectEdge);
      network.on("deselectEdge", deselectEdge);
  
      // Adjust canvas size
      network.redraw();
    });

    onDestroy(() => {
      network.destroy()
    });
  </script>
  
  <style>
    #vis-network-container {
      width: 100%;
      height: 100%;
      /* border: 1px solid lightgray; */
    }
  </style>
  
  <div id="vis-network-container" bind:this={container}></div>
  