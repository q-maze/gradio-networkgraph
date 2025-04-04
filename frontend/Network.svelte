<script lang="ts">
    import type { Gradio } from "@gradio/utils";
    import { onMount } from "svelte";
    import { Network } from "vis-network";

    export let gradio: Gradio;
    export let value;
    export let selectedNodes = []
    export let selectedEdges = []

    let container;
    let network;

    function renderNetwork() {
      if (!container) return;
  
      // Set up the network
      var nodes = value.nodes
      var edges = value.edges
      var options = value.options
      var data = { nodes, edges, options };
      network = new Network(container, data);

      function sendData(params) {
        selectedNodes = params.nodes;
        selectedEdges = params.edges.map(
          (edgeId) => network.getConnectedNodes(edgeId)
        );
        return {
          "nodes": selectedNodes,
          "edges": selectedEdges,
        }
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

      function getPositions() {
        return network.getPositions();
      }

      function stabilizationIterationsDone() {
        gradio.dispatch("stabilizationIterationsDone", getPositions())
      }

      function stabilized() {
        gradio.dispatch("stabilized", getPositions())
      }

      // Event Listeners
      network.on("selectNode", selectNode);
      network.on("deselectNode", deselectNode);
      network.on("selectEdge", selectEdge);
      network.on("deselectEdge", deselectEdge);
      network.on("stabilizationIterationsDone", stabilizationIterationsDone)
      network.on("stabilized", stabilized)
  
      // Adjust canvas size
      container.style.width = options.width || "100%";
      container.style.height = options.height || "500px";
      network.redraw();
    };
  
    onMount(() => {
      renderNetwork();
    });

    $: if (value) {
      renderNetwork()
    }

  </script>
  
  <style>
    #vis-network-container {
      width: 100%;
      height: 100%;
      /* border: 1px solid lightgray; */
    }
  </style>
  
  <div id="vis-network-container" bind:this={container}></div>
  