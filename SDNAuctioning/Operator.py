import itertools
from SDNAuctioning.Client import Client
from random import randint


class InfrastructureOperator:
    num_services = 0
    services = []
    services_id = []

    def __init__(self, num_nodes, num_links, num_vnf_services, service_capacity, topology):
        self.num_nodes = num_nodes
        self.num_links = num_links
        self.topology = topology
        self.num_vnf_services = num_vnf_services
        self.service_capacity = service_capacity
        self.calculate_services()
        self.calculate_num_services()
        # self.update_used_units()

    def calculate_num_services(self):
        self.num_services = len(self.services)

    def calculate_services(self):
        counter = 0
        for i in range(len(self.topology.nodes)):
            self.services.append(self.topology.nodes[i].vnf_services)

            for j in range(len(self.topology.nodes[i].vnf_services)):
                self.services_id.append(counter)
                counter += 1

        for i in range(len(self.topology.edges)):
            self.services.append(self.topology.edges[i].bandwidth_service)
            self.services_id.append(counter)
            counter += 1

        self.services = list(itertools.chain(*self.services))

    # def update_used_units(self):
    #     for i in range(len(self.services)):
    #         if i > 4:
    #             self.services[i].used_units = randint(100, 200)


class NetworkOperator:
    clients = []

    def __init__(self, id, topology, infra_operator, clients_id, bids):
        self.id = id
        self.topology = topology
        self.infra_operator = infra_operator
        self.clients_id = clients_id
        self.bids = bids
        self.create_clients()

    def create_clients(self):
        self.clients = []
        for i in range(len(self.clients_id)):
            for j in range(len(self.bids)):
                if self.clients_id[i] == self.bids[j].client:
                    self.clients.append(Client(self.clients_id[i],
                                               self.id, self.topology, len(self.clients_id), self.infra_operator,
                                               self.bids[j]))
        # print(self.clients)

