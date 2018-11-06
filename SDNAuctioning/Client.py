from random import uniform
from random import randint


class Client:
    distance_to_antenna = 0
    process_power = 0
    battery = 0
    num_neighbours = 0
    storage = 0
    value = 0
    sort_metric = 0

    def __init__(self, operator_id, topology, num_clients):
        self.operator_id = operator_id
        self.topology = topology
        self.num_clients = num_clients
        self.compute_properties()

    def compute_properties(self):
        self.distance_to_antenna = uniform(0.1, 3.0)
        self.process_power = randint(10, 100)
        self.battery = randint(10, 100)
        self.num_neighbours = randint(1, self.num_clients)
        self.storage = randint(10, 100)
        self.value = randint(1, 100)

        self.sort_metric = (self.process_power + self.battery + self.num_neighbours + self.storage) / (self.value + self.distance_to_antenna)

        # print("Sort metric:" + str(self.sort_metric))
