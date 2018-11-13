from random import uniform
from random import randint
from SDNAuctioning import BidGenerator


class Client:
    distance_to_antenna = 0
    process_power = 0
    battery = 0
    num_neighbours = 0
    storage = 0
    value = 0
    sort_metric = 0
    bid = 0
    winning_client = 0

    def __init__(self, client_id, operator_id, topology, num_clients, infra_operator):
        self.client_id = client_id
        self.operator_id = operator_id
        self.topology = topology
        self.num_clients = num_clients
        self.infra_operator = infra_operator
        self.compute_properties()
        # self.compute_bid()

    def compute_properties(self):
        self.distance_to_antenna = uniform(0.1, 3.0)
        self.process_power = randint(10, 100)
        self.battery = randint(10, 100)
        self.num_neighbours = randint(1, self.num_clients)
        self.storage = randint(10, 100)
        self.value = randint(1, 50)

        # print("Sort metric:" + str(self.sort_metric))

    def compute_bid(self):
        self.bid = BidGenerator.BidGenerator(self.client_id, self.operator_id, self.infra_operator,
                                             self.topology, self.num_clients)
        # print(vars(self.bid))

    def update_client(self):
        if self.bid.winning_bid == 1:
            self.winning_client = 1

    def compute_sort_metric(self):
        self.sort_metric = self.winning_client * ((self.process_power + self.battery +
                                                   self.num_neighbours + self.storage +
                                                   self.bid.total_required_service_quantity) /
                                                  (self.value * self.distance_to_antenna))
