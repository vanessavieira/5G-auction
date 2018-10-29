from Network.Service import Service


class Edge:
    bandwidth_service = []

    def __init__(self, from_node, to_node, distance):
        self.from_node = from_node
        self.to_node = to_node
        self.distance = distance
        self.compute_offered_services()

    def compute_offered_services(self):
        self.bandwidth_service = []
        service = Service(id=str(self.from_node) + str(self.to_node), node="no node", type="bandwidth")
        self.bandwidth_service.append(service)
