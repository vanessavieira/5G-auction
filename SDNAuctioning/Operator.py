import itertools


class InfrastructureOperator:
    num_services = 0
    services = []

    def __init__(self, num_nodes, num_links, num_vnf_services, service_capacity, topology):
        self.num_nodes = num_nodes
        self.num_links = num_links
        self.topology = topology
        self.num_vnf_services = num_vnf_services
        self.service_capacity = service_capacity
        self.calculate_num_services()
        self.calculate_services()

    def calculate_num_services(self):
        self.num_services = self.num_links + self.num_vnf_services * self.num_nodes

    def calculate_services(self):

        for i in range(len(self.topology.nodes)):
            self.services.append(self.topology.nodes[i].vnf_services)

        for i in range(len(self.topology.edges)):
            self.services.append(self.topology.edges[i].bandwidth_service)

        self.services = list(itertools.chain(*self.services))


class NetworkOperator:
    clients_demands = []
    bids = []

    def __init__(self, id, topology):
        self.id = id
        self.topology = topology

    # def add_clients_demands(self):
    #     # TODO um for criando clientes dessa operadora
    #     self.clients_demands.append(#TODO)
    #
    # def create_bids(self):
    #     self.bids.append(#TODO)
