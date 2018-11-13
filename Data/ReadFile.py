from SDNAuctioning.Bid import Bid


class ReadFile:
    num_operators = []
    bids = []

    def __init__(self, file_greedy, num_bids, infra_operator):
        self.file_greedy = file_greedy
        self.num_bids = num_bids
        self.infra_operator = infra_operator
        self.read_greedy_file()

    def read_greedy_file(self):

        print("Reading file...")
        self.file_greedy = open("greedy_gerador_" + str(self.num_bids) + ".dat", "r")

        self.num_bids = int(self.file_greedy.readline())
        self.num_operators = int(self.file_greedy.readline())

        for i in range(self.num_bids):

            services_requested = []
            requested_services_quantity = []
            valuation = int(self.file_greedy.readline())
            operator_id = self.file_greedy.readline()
            client_id = self.file_greedy.readline()
            num_services = int(self.file_greedy.readline())

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



