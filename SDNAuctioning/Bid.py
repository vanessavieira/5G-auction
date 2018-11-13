import math


class Bid:
    total_required_service_quantity = 0

    winning_bid = 0

    price_to_pay = []

    sort_metric = 0

    def __init__(self, client, network_operator, operator, valuation, required_services, required_service_quantity):
        self.client = client
        self.network_operator = network_operator
        self.operator = operator
        self.valuation = valuation
        self.required_services = required_services
        self.required_service_quantity = required_service_quantity
        self.compute_total_required_service_quantity()
        self.update_required_services()
        self.compute_sort_metric()

    def compute_total_required_service_quantity(self):
        for i in range(len(self.required_service_quantity)):
            self.total_required_service_quantity += self.required_service_quantity[i]

    def update_required_services(self):
        required_services_temp = []
        for i in range(len(self.required_services)):
            required_services_temp.append(self.operator.services[self.required_services[i]])

        self.required_services = required_services_temp

    def compute_sort_metric(self):
        self.sort_metric = self.valuation/(math.sqrt(self.total_required_service_quantity))
