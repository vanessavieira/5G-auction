import statistics


class ManageResults:
    # 1400, 2800, 4200, 5600, 7000, 8400, 9800, 11200

    accepted_bids = []
    market_valuation = []
    operator_revenue = []
    percentage_accepted_bids = []
    mean_bid_price = []
    op0 = []
    op1 = []
    op2 = []
    op3 = []
    op4 = []
    num_hubs = []
    operator_costs_hubs = []
    operator_costs_auction = []

    def __init__(self, num_bids, num_operators, file):
        self.num_bids = num_bids
        self.num_operators = num_operators
        self.file = file
        self.read_files()

    def read_files(self):
        print("Reading file...")

        for i in range(10):
            self.file = open("SDNAuctioning/results_greedy_" + str(self.num_bids * self.num_operators) + "_"
                             + str(i+1) + ".dat","r")
            self.accepted_bids.append(int(self.file.readline()))
            print(self.accepted_bids)
            self.market_valuation.append(int(self.file.readline()))
            print(self.market_valuation)
            self.operator_revenue.append(float((self.file.readline()).strip("\r\n")))
            print(self.operator_revenue)
            self.percentage_accepted_bids.append(float((self.file.readline()).strip("\r\n")))
            print(self.percentage_accepted_bids)
            self.mean_bid_price.append(float((self.file.readline()).strip("\r\n")))
            print(self.mean_bid_price)
            self.op0.append(int(self.file.readline()))
            print(self.op0)
            self.op1.append(int(self.file.readline()))
            print(self.op1)
            self.op2.append(int(self.file.readline()))
            print(self.op2)
            self.op3.append(int(self.file.readline()))
            print(self.op3)
            self.op4.append(int(self.file.readline()))
            print(self.op4)
            self.num_hubs.append(int(self.file.readline()))
            self.operator_costs_hubs.append(float((self.file.readline()).strip("\r\n")))
            self.operator_costs_auction.append(float((self.file.readline()).strip("\r\n")))

            self.file.close()

        mean_accepted_bids = statistics.mean(self.accepted_bids)
        std_accepted_bids = statistics.stdev(self.accepted_bids)

        mean_market_valuation = statistics.mean(self.market_valuation)
        std_market_valuation = statistics.stdev(self.market_valuation)

        mean_operator_revenue = statistics.mean(self.operator_revenue)
        std_operator_revenue = statistics.stdev(self.operator_revenue)

        mean_percentage_accepted_bids = statistics.mean(self.percentage_accepted_bids)
        std_percentage_accepted_bids = statistics.stdev(self.percentage_accepted_bids)

        mean_mean_bid_price = statistics.mean(self.mean_bid_price)
        std_mean_bid_price = statistics.stdev(self.mean_bid_price)

        mean_op0 = statistics.mean(self.op0)
        std_op0 = statistics.stdev(self.op0)

        mean_op1 = statistics.mean(self.op1)
        std_op1 = statistics.stdev(self.op1)

        mean_op2 = statistics.mean(self.op2)
        std_op2 = statistics.stdev(self.op2)

        mean_op3 = statistics.mean(self.op3)
        std_op3 = statistics.stdev(self.op3)

        mean_op4 = statistics.mean(self.op4)
        std_op4 = statistics.stdev(self.op4)

        mean_num_hubs = statistics.mean(self.num_hubs)
        std_num_hubs = statistics.stdev(self.num_hubs)

        mean_operator_costs_hubs = statistics.mean(self.operator_costs_hubs)
        std_operator_costs_hubs = statistics.stdev(self.operator_costs_hubs)

        mean_operator_costs_auction = statistics.mean(self.operator_costs_auction)
        std_operator_costs_auction = statistics.stdev(self.operator_costs_auction)

        f = open("Results/2nd_Test/final_results_greedy_" + str(self.num_bids * self.num_operators) + ".dat", "w+")

        f.write(str(mean_accepted_bids) + "\r\n")
        f.write(str(std_accepted_bids) + "\r\n")

        f.write(str(mean_market_valuation) + "\r\n")
        f.write(str(std_market_valuation) + "\r\n")

        f.write(str(mean_operator_revenue) + "\r\n")
        f.write(str(std_operator_revenue) + "\r\n")

        f.write(str(mean_percentage_accepted_bids) + "\r\n")
        f.write(str(std_percentage_accepted_bids) + "\r\n")

        f.write(str(mean_mean_bid_price) + "\r\n")
        f.write(str(std_mean_bid_price) + "\r\n")

        f.write(str(mean_op0) + "\r\n")
        f.write(str(std_op0) + "\r\n")

        f.write(str(mean_op1) + "\r\n")
        f.write(str(std_op1) + "\r\n")

        f.write(str(mean_op2) + "\r\n")
        f.write(str(std_op2) + "\r\n")

        f.write(str(mean_op3) + "\r\n")
        f.write(str(std_op3) + "\r\n")

        f.write(str(mean_op4) + "\r\n")
        f.write(str(std_op4) + "\r\n")

        f.write(str(mean_num_hubs) + "\r\n")
        f.write(str(std_num_hubs) + "\r\n")

        f.write(str(mean_operator_costs_hubs) + "\r\n")
        f.write(str(std_operator_costs_hubs) + "\r\n")

        f.write(str(mean_operator_costs_auction) + "\r\n")
        f.write(str(std_operator_costs_auction) + "\r\n")




