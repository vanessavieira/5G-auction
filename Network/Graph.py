from collections import defaultdict


class Graph(object):

    def __init__(self):
        self.edge_list = defaultdict(list)
        self.edges = []
        self.distances = {}
        self.nodes = []
        self.bandwidth_service = []

    def add_node(self, node):
        self.nodes.append(node)

    def add_edge(self, edge):
        self.edge_list[edge.from_node.id].append(edge.to_node.id)
        self.distances[(edge.from_node.id, edge.to_node.id)] = edge.distance
        self.edges.append(edge)

