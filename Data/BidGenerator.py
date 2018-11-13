from random import randint
import random
import math
from Network.Dijkstra import shortest_path


class BidGenerator:
    required_service_quantity = []
    total_required_service_quantity = 0

    winning_bid = 0
    input_node = 0
    output_node = 1
    shortest_node_path = []
    required_services = []
    services_to_choose = []
    price_to_pay = []

    valuation = 0
    sort_metric = 0

    def __init__(self, client, network_operator, operator, topology, num_clients):
        self.client = client
        self.network_operator = network_operator
        self.operator = operator
        self.topology = topology
        self.num_clients = num_clients
        self.compute_bid_topology()
        self.compute_vnf_service_request()
        self.compute_bandwidth_service_request()
        self.compute_all_services_request()
        self.compute_valuation()
        self.compute_sort_metric()

    def compute_bid_topology(self):
        self.input_node = 0
        self.output_node = randint(0, len(self.topology.nodes) - 1)

        while self.output_node == self.input_node:
            self.output_node = randint(1, len(self.topology.nodes) - 1)

        for i in range(len(self.topology.nodes)):
            if i == self.input_node:
                self.input_node = self.topology.nodes[i].id

            if i == self.output_node:
                self.output_node = self.topology.nodes[i].id

        self.shortest_node_path = shortest_path(self.topology, str(self.input_node),
                                                str(self.output_node))

    def compute_vnf_service_request(self):
        self.services_to_choose = []
        num_services_requested = randint(1, 7)

        for i in range(len(self.shortest_node_path)):
            for j in range(len(self.shortest_node_path[i].vnf_services)):
                for k in range(len(self.operator.services)):
                    if self.shortest_node_path[i].vnf_services[j] == self.operator.services[k]:
                        self.services_to_choose.append(self.operator.services_id[k])

        # self.services_to_choose = list(itertools.chain(*self.services_to_choose))
        # print("services_to_choose: " + str(self.services_to_choose))

        # vnf services
        self.required_services = random.sample(self.services_to_choose, num_services_requested)
        # print("chosen vnf services: " + str(self.required_services.__str__()))

    def compute_bandwidth_service_request(self):
        path_nodes = []
        required_services_edge = []
        for i in range(len(self.shortest_node_path)):
            if (i+1) != len(self.shortest_node_path):
                edge_tuple = (self.shortest_node_path[i], self.shortest_node_path[i+1])
                path_nodes.append(edge_tuple)

        for path in range(len(path_nodes)):
            for edge in range(len(self.topology.edges)):
                if (self.topology.edges[edge].from_node == path_nodes[path][0]) and \
                        (self.topology.edges[edge].to_node == path_nodes[path][1]):
                    required_services_edge = required_services_edge + self.topology.edges[edge].bandwidth_service

        for j in range(len(required_services_edge)):
            for k in range(len(self.operator.services)):
                if required_services_edge[j] == self.operator.services[k]:
                    self.required_services.append(self.operator.services_id[k])

        # print("chosen vnf services + bandwidth services: " + str(self.required_services))

    def compute_all_services_request(self):
        self.required_service_quantity = []
        for services in range(len(self.required_services)):
            rand_quantity = randint(1, 15)
            self.total_required_service_quantity += rand_quantity
            self.required_service_quantity.append(rand_quantity)

      #  print("Required service quantity: " + str(self.required_service_quantity))

    def compute_valuation(self):
        rand_valuation = randint(1, int(self.total_required_service_quantity))
        self.valuation = rand_valuation

      #  print("Valuation: " + str(self.valuation))
       # print("Total required service quantity: " + str(self.total_required_service_quantity) + "\n")

    def compute_sort_metric(self):
        self.sort_metric = self.valuation/(math.sqrt(self.total_required_service_quantity))
