from Network.Service import Service


class Node:
    vnf_services = []

    def __init__(self, id, num_vnf_services):
        self.id = id
        self.num_vnf_services = num_vnf_services
        self.compute_offered_services()

    def compute_offered_services(self):
        self.vnf_services = []
        for i in range(self.num_vnf_services):
            service = Service(i, self.id, type="vnf")
            self.vnf_services.append(service)
