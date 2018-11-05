from random import uniform

class Client:
    distance_to_antenna = 0

    def __init__(self, operator_id):
        self.operator_id = operator_id
        self.calculate_demand()
        self.calculate_distance_to_antenna()

    def calculate_demand(self):
        

    def calculate_distance_to_antenna(self):
        self.distance_to_antenna = uniform(0.1, 3.0)