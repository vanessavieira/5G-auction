import itertools
from SDNAuctioning.Client import Client
from SDNAuctioning.BidGenerator import Bid
from random import randint


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
        self.update_used_units()

    def calculate_num_services(self):
        self.num_services = self.num_links + self.num_vnf_services * self.num_nodes

    def calculate_services(self):

        for i in range(len(self.topology.nodes)):
            self.services.append(self.topology.nodes[i].vnf_services)

        for i in range(len(self.topology.edges)):
            self.services.append(self.topology.edges[i].bandwidth_service)

        self.services = list(itertools.chain(*self.services))

    def update_used_units(self):
        for i in range(len(self.topology.nodes)):
            if i != 0:
                self.services[i].used_units = randint(100, 300)


class NetworkOperator:
    bids = []
    clients = []

    clients_demands_services = []
    clients_demands_quantities = []

    def __init__(self, id, topology, infra_operator, num_clients):
        self.id = id
        self.topology = topology
        self.infra_operator = infra_operator
        self.num_clients = num_clients
        self.create_clients()

    def create_clients(self):
        self.clients = []
        self.bids = []
        for i in range(self.num_clients):
            self.clients.append(Client("Client" + str(i) + "_" + str(self.id),
                                       self.id, self.topology, self.num_clients, self.infra_operator))
            self.bids.append(self.clients[i].bid)
        # print(self.clients)

