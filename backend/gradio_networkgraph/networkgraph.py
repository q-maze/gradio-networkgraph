import json

from gradio.components.base import Component


class NetworkGraph(Component):
    EVENTS = [
        "selectNode",
        "deselectNode",
        "selectEdge",
        "deselectEdge",
        "stabilizationIterationsDone",
        'stabilized'
    ]
    def preprocess(self, payload):
        """
        This docstring is used to generate the docs for this custom component.
        Parameters:
            payload: the data to be preprocessed, sent from the frontend
        Returns:
            the data after preprocessing, sent to the user's function in the backend
        """
        return payload

    def postprocess(self, value):
        """
        This docstring is used to generate the docs for this custom component.
        Parameters:
            payload: the data to be postprocessed, sent from the user's function in the backend
        Returns:
            the data after postprocessing, sent to the frontend
        """
        return value

    def example_payload(self):
        return {
            'nodes': [1],
            'edges': [[1, 2]],
        }

    def example_value(self):
        return {
            "nodes": [{'id': 1, "label": "node 1"}, {'id': 2, "label": "node 2"}],
            "edges": [{"from": 1, "to": 2, "label": "edge", "id": "edge1"}],
            "options": {}
        }

    def api_info(self):
        return {"type": {}, "description": "any valid json"}
