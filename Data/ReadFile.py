from SDNAuctioning.Bid import Bid


class ReadFile:
    num_operators = []
    bids = []

    clients_operator0 = []
    clients_operator1 = []
    clients_operator2 = []
    clients_operator3 = []
    clients_operator4 = []

    def __init__(self, file_greedy, num_bids, infra_operator, seed):
        self.file_greedy = file_greedy
        self.num_bids = num_bids
        self.infra_operator = infra_operator
        self.seed = seed
        self.read_greedy_file()

    def read_greedy_file(self):

        print("Reading file...")
        self.file_greedy = open("SDNAuctioning/greedy_gerador_" + str(self.num_bids) + "_" + str(self.seed) + ".dat", "r")

        self.num_bids = int(self.file_greedy.readline())
        self.num_operators = int(self.file_greedy.readline())

        for i in range(self.num_bids):

            services_requested = []
            requested_services_quantity = []
            valuation = int(self.file_greedy.readline())
            operator_id = self.file_greedy.readline()
            client_id = self.file_greedy.readline()
            num_services = int(self.file_greedy.readline())

            if operator_id == "operator0\n":
                self.clients_operator0.append(client_id)
            elif operator_id == "operator1\n":
                self.clients_operator1.append(client_id)
            elif operator_id == "operator2\n":
                self.clients_operator2.append(client_id)
            elif operator_id == "operator3\n":
                self.clients_operator3.append(client_id)
            elif operator_id == "operator4\n":
                self.clients_operator4.append(client_id)

            for j in range(num_services):
                service_id = int(self.file_greedy.readline())
                services_requested.append(service_id)

            for k in range(num_services):
                service_quantity = int(self.file_greedy.readline())
                requested_services_quantity.append(service_quantity)

            bid = Bid(client=client_id, network_operator=operator_id, operator=self.infra_operator, valuation=valuation,
                      required_services=services_requested, required_service_quantity=requested_services_quantity)

            self.bids.append(bid)
            # print(bid)
            print(i)

        self.file_greedy.close()



