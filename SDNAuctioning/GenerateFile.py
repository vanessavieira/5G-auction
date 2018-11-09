class GenerateFile:

    def __init__(self, bids, infra_operator, file):
        self.bids = bids
        self.infra_operator = infra_operator
        self.file = file
        self.create_instances()

    def create_instances(self):
        optimal_value = 0
        self.file = open("gerador_28000.dat", "a+")

        self.file.write(str(len(self.bids)) + " " + str(len(self.infra_operator.services)) + " " + str(optimal_value)
                        + "\r\n")

        for i in range(len(self.bids)):
            self.file.write(str(self.bids[i].valuation) + "\r\n")
        print("teste!!: " + str(len(self.infra_operator.services)))

        for j in range(len(self.infra_operator.services)):

            for k in range(len(self.bids)):
                flag = False
                count = 0

                for v in self.bids[k].required_services:
                    if v == self.infra_operator.services[j]:
                        self.file.write(str(self.bids[k].required_service_quantity[count]) + "\r\n")
                        flag = True
                    count += 1

                if not flag:
                    self.file.write("0\r\n")

        for t in range(len(self.infra_operator.services)):
            self.file.write("100\r\n")

        self.file.close()
