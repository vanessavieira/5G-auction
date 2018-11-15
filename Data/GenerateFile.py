class GenerateFile:

    def __init__(self, bids, operators, infra_operator, file_optimal, file_greedy, num_bids, seed):
        self.bids = bids
        self.operators = operators
        self.infra_operator = infra_operator
        self.file_optimal = file_optimal
        self.file_greedy = file_greedy
        self.num_bids = num_bids
        self.seed = seed
        # self.create_instances_optimal()
        self.create_instances_greedy()

    def create_instances_optimal(self):
        print("Generating optimal instances file...\n")
        optimal_value = 0
        self.file_optimal = open("gerador_" + str(self.num_bids) + ".dat", "a+")

        self.file_optimal.write(str(len(self.bids)) + " " + str(len(self.infra_operator.services))
                                + " " + str(optimal_value) + "\r\n")

        for i in range(len(self.bids)):
            self.file_optimal.write(str(self.bids[i].valuation) + "\r\n")

        for j in range(len(self.infra_operator.services)):

            for k in range(len(self.bids)):
                flag = False

                for v in range(len(self.bids[k].required_services)):
                   # print(self.bids[k].required_services[v])

                    if self.bids[k].required_services[v] == self.infra_operator.services_id[j]:
                        # print(self.bids[k].required_services[v])
                        self.file_optimal.write(str(self.bids[k].required_service_quantity[v]) + "\r\n")
                        flag = True

                if not flag:
                    self.file_optimal.write("0\r\n")

        for t in range(len(self.infra_operator.services)):
            self.file_optimal.write(str(self.infra_operator.service_capacity) + "\r\n")

        self.file_optimal.close()
        print("Done...\n")

    def create_instances_greedy(self):
        print("Generating greedy instances file...\n")
        self.file_greedy = open("greedy_gerador_" + str(self.num_bids) + "_" + str(self.seed) + ".dat", "a+")

        self.file_greedy.write(str(len(self.bids)) + "\r\n")

        self.file_greedy.write(str(len(self.operators)) + "\r\n")

        for i in range(len(self.bids)):
            self.file_greedy.write(str(self.bids[i].valuation) + "\r\n")
            self.file_greedy.write(str(self.bids[i].network_operator) + "\r\n")
            self.file_greedy.write(str(self.bids[i].client) + "\r\n")
            self.file_greedy.write(str(len(self.bids[i].required_services)) + "\r\n")

            for j in range(len(self.bids[i].required_services)):
                self.file_greedy.write(str(self.bids[i].required_services[j]) + "\r\n")

            for k in range(len(self.bids[i].required_service_quantity)):
                self.file_greedy.write(str(self.bids[i].required_service_quantity[k]) + "\r\n")

        self.file_greedy.close()
        print("Done...\n")
