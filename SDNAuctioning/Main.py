import itertools
import random

from Network.Edge import Edge
from Network.Graph import Graph
from Network.Node import Node
from SDNAuctioning import Auction
from SDNAuctioning.Operator import InfrastructureOperator
from statistics import mean
import Data.Operator
import SDNAuctioning.Operator
from Data.Client import Client
from Data.GenerateFile import GenerateFile
from Data.ReadFile import ReadFile


def create_network_topology(topology, num_vnf_services):

    node0 = Node(id="0", num_vnf_services=num_vnf_services)
    node1 = Node(id="1", num_vnf_services=num_vnf_services)
    node2 = Node(id="2", num_vnf_services=num_vnf_services)
    node3 = Node(id="3", num_vnf_services=num_vnf_services)
    node4 = Node(id="4", num_vnf_services=num_vnf_services)
    node5 = Node(id="5", num_vnf_services=num_vnf_services)
    node6 = Node(id="6", num_vnf_services=num_vnf_services)
    node7 = Node(id="7", num_vnf_services=num_vnf_services)
    node8 = Node(id="8", num_vnf_services=num_vnf_services)
    node9 = Node(id="9", num_vnf_services=num_vnf_services)
    node10 = Node(id="10", num_vnf_services=num_vnf_services)
    node11 = Node(id="11", num_vnf_services=num_vnf_services)
    node12 = Node(id="12", num_vnf_services=num_vnf_services)
    node13 = Node(id="13", num_vnf_services=num_vnf_services)
    node14 = Node(id="14", num_vnf_services=num_vnf_services)
    node15 = Node(id="15", num_vnf_services=num_vnf_services)
    node16 = Node(id="16", num_vnf_services=num_vnf_services)
    node17 = Node(id="17", num_vnf_services=num_vnf_services)
    node18 = Node(id="18", num_vnf_services=num_vnf_services)
    node19 = Node(id="19", num_vnf_services=num_vnf_services)
    node20 = Node(id="20", num_vnf_services=num_vnf_services)
    node21 = Node(id="21", num_vnf_services=num_vnf_services)
    node22 = Node(id="22", num_vnf_services=num_vnf_services)
    node23 = Node(id="23", num_vnf_services=num_vnf_services)
    node24 = Node(id="24", num_vnf_services=num_vnf_services)
    node25 = Node(id="25", num_vnf_services=num_vnf_services)
    node26 = Node(id="26", num_vnf_services=num_vnf_services)

    topology.add_node(node0)
    topology.add_node(node1)
    topology.add_node(node2)
    topology.add_node(node3)
    topology.add_node(node4)
    topology.add_node(node5)
    topology.add_node(node6)
    topology.add_node(node7)
    topology.add_node(node8)
    topology.add_node(node9)
    topology.add_node(node10)
    topology.add_node(node11)
    topology.add_node(node12)
    topology.add_node(node13)
    topology.add_node(node14)
    topology.add_node(node15)
    topology.add_node(node16)
    topology.add_node(node17)
    topology.add_node(node18)
    topology.add_node(node19)
    topology.add_node(node20)
    topology.add_node(node21)
    topology.add_node(node22)
    topology.add_node(node23)
    topology.add_node(node24)
    topology.add_node(node25)
    topology.add_node(node26)

    edge0_25 = Edge(from_node=node0, to_node=node25, distance=313)
    edge25_0 = Edge(from_node=node25, to_node=node0, distance=313)

    edge0_3 = Edge(from_node=node0, to_node=node3, distance=280)
    edge3_0 = Edge(from_node=node3, to_node=node0, distance=280)

    edge0_5 = Edge(from_node=node0, to_node=node5, distance=291)
    edge5_0 = Edge(from_node=node5, to_node=node0, distance=291)

    edge1_9 = Edge(from_node=node1, to_node=node9, distance=534)
    edge9_1 = Edge(from_node=node9, to_node=node1, distance=534)

    edge1_2 = Edge(from_node=node1, to_node=node2, distance=435)
    edge2_1 = Edge(from_node=node2, to_node=node1, distance=435)

    edge1_6 =  Edge(from_node=node1, to_node=node6, distance=689)
    edge6_1 = Edge(from_node=node6, to_node=node1, distance=689)

    edge2_3 = Edge(from_node=node2, to_node=node3, distance=878)
    edge3_2 = Edge(from_node=node3, to_node=node2, distance=878)

    edge2_7 = Edge(from_node=node2, to_node=node7, distance=1422)
    edge7_2 = Edge(from_node=node7, to_node=node2, distance=1422)

    edge2_17 = Edge(from_node=node2, to_node=node17, distance=1170)
    edge17_2 = Edge(from_node=node17, to_node=node2, distance=1170)

    edge2_18 = Edge(from_node=node2, to_node=node18, distance=1064)
    edge18_2 = Edge(from_node=node18, to_node=node2, distance=1064)

    edge2_20 = Edge(from_node=node2, to_node=node20, distance=1247)
    edge20_2 = Edge(from_node=node20, to_node=node2, distance=1247)

    edge3_6 = Edge(from_node=node3, to_node=node6, distance=1183)
    edge6_3 = Edge(from_node=node6, to_node=node3, distance=1183)

    edge3_9 = Edge(from_node=node3, to_node=node9, distance=473)
    edge9_3 = Edge(from_node=node9, to_node=node3, distance=473)

    edge3_16 = Edge(from_node=node3, to_node=node16, distance=1712)
    edge16_3 = Edge(from_node=node16, to_node=node3, distance=1712)

    edge3_19 = Edge(from_node=node3, to_node=node19, distance=1317)
    edge19_3 = Edge(from_node=node19, to_node=node3, distance=1317)

    edge3_21 = Edge(from_node=node3, to_node=node21, distance=810)
    edge21_3 = Edge(from_node=node21, to_node=node3, distance=810)

    edge3_26 = Edge(from_node=node3, to_node=node26, distance=577)
    edge26_3 = Edge(from_node=node26, to_node=node3, distance=577)

    edge4_7 = Edge(from_node=node4, to_node=node7, distance=502)
    edge7_4 = Edge(from_node=node7, to_node=node4, distance=502)

    edge5_8 = Edge(from_node=node5, to_node=node8, distance=161)
    edge8_5 = Edge(from_node=node8, to_node=node5, distance=161)

    edge6_7 = Edge(from_node=node6, to_node=node7, distance=1362)
    edge7_6 = Edge(from_node=node7, to_node=node6, distance=1362)

    edge8_9 = Edge(from_node=node8, to_node=node9, distance=365)
    edge9_8 = Edge(from_node=node9, to_node=node8, distance=365)

    edge8_10 = Edge(from_node=node8, to_node=node10, distance=643)
    edge10_8 = Edge(from_node=node10, to_node=node8, distance=643)

    edge8_13 = Edge(from_node=node8, to_node=node13, distance=381)
    edge13_8 = Edge(from_node=node13, to_node=node8, distance=381)

    edge9_12 = Edge(from_node=node9, to_node=node12, distance=382)
    edge12_9 = Edge(from_node=node12, to_node=node9, distance=382)

    edge9_13 = Edge(from_node=node9, to_node=node13, distance=251)
    edge13_9 = Edge(from_node=node13, to_node=node9, distance=251)

    edge11_16 = Edge(from_node=node11, to_node=node16, distance=513)
    edge16_11 = Edge(from_node=node16, to_node=node11, distance=513)

    edge14_20 = Edge(from_node=node14, to_node=node20, distance=3600)
    edge20_14 = Edge(from_node=node20, to_node=node14, distance=3600)

    edge15_16 = Edge(from_node=node15, to_node=node16, distance=1090)
    edge16_15 = Edge(from_node=node16, to_node=node15, distance=1090)

    edge16_20 = Edge(from_node=node16, to_node=node20, distance=2250)
    edge20_16 = Edge(from_node=node20, to_node=node16, distance=2250)

    edge17_26 = Edge(from_node=node17, to_node=node26, distance=173)
    edge26_17 = Edge(from_node=node26, to_node=node17, distance=173)

    edge17_18 = Edge(from_node=node17, to_node=node18, distance=187)
    edge18_17 = Edge(from_node=node18, to_node=node17, distance=187)

    edge19_20 = Edge(from_node=node19, to_node=node20, distance=463)
    edge20_19 = Edge(from_node=node20, to_node=node19, distance=463)

    edge20_21 = Edge(from_node=node20, to_node=node21, distance=1432)
    edge21_20 = Edge(from_node=node21, to_node=node20, distance=1432)

    edge20_26 = Edge(from_node=node20, to_node=node26, distance=357)
    edge26_20 = Edge(from_node=node26, to_node=node20, distance=357)

    edge21_22 = Edge(from_node=node21, to_node=node22, distance=379)
    edge22_21 = Edge(from_node=node22, to_node=node21, distance=379)

    edge21_23 = Edge(from_node=node21, to_node=node23, distance=442)
    edge23_21 = Edge(from_node=node23, to_node=node21, distance=442)

    edge21_24 = Edge(from_node=node21, to_node=node24, distance=816)
    edge24_21 = Edge(from_node=node24, to_node=node21, distance=816)

    edge21_25 = Edge(from_node=node21, to_node=node25, distance=772)
    edge25_21 = Edge(from_node=node25, to_node=node21, distance=772)

    topology.add_edge(edge0_25)
    topology.add_edge(edge25_0)

    topology.add_edge(edge0_3)
    topology.add_edge(edge3_0)

    topology.add_edge(edge0_5)
    topology.add_edge(edge5_0)

    topology.add_edge(edge1_9)
    topology.add_edge(edge9_1)

    topology.add_edge(edge1_2)
    topology.add_edge(edge2_1)

    topology.add_edge(edge1_6)
    topology.add_edge(edge6_1)

    topology.add_edge(edge2_3)
    topology.add_edge(edge3_2)

    topology.add_edge(edge2_7)
    topology.add_edge(edge7_2)

    topology.add_edge(edge2_17)
    topology.add_edge(edge17_2)

    topology.add_edge(edge2_18)
    topology.add_edge(edge18_2)

    topology.add_edge(edge2_20)
    topology.add_edge(edge20_2)

    topology.add_edge(edge3_6)
    topology.add_edge(edge6_3)

    topology.add_edge(edge3_9)
    topology.add_edge(edge9_3)

    topology.add_edge(edge3_16)
    topology.add_edge(edge16_3)

    topology.add_edge(edge3_19)
    topology.add_edge(edge19_3)

    topology.add_edge(edge3_21)
    topology.add_edge(edge21_3)

    topology.add_edge(edge3_26)
    topology.add_edge(edge26_3)

    topology.add_edge(edge4_7)
    topology.add_edge(edge7_4)

    topology.add_edge(edge5_8)
    topology.add_edge(edge8_5)

    topology.add_edge(edge6_7)
    topology.add_edge(edge7_6)

    topology.add_edge(edge8_9)
    topology.add_edge(edge9_8)

    topology.add_edge(edge8_10)
    topology.add_edge(edge10_8)

    topology.add_edge(edge8_13)
    topology.add_edge(edge13_8)

    topology.add_edge(edge9_12)
    topology.add_edge(edge12_9)

    topology.add_edge(edge9_13)
    topology.add_edge(edge13_9)

    topology.add_edge(edge11_16)
    topology.add_edge(edge16_11)

    topology.add_edge(edge14_20)
    topology.add_edge(edge20_14)

    topology.add_edge(edge15_16)
    topology.add_edge(edge16_15)

    topology.add_edge(edge16_20)
    topology.add_edge(edge20_16)

    topology.add_edge(edge17_26)
    topology.add_edge(edge26_17)

    topology.add_edge(edge17_18)
    topology.add_edge(edge18_17)

    topology.add_edge(edge19_20)
    topology.add_edge(edge20_19)

    topology.add_edge(edge20_21)
    topology.add_edge(edge21_20)

    topology.add_edge(edge20_26)
    topology.add_edge(edge26_20)

    topology.add_edge(edge21_22)
    topology.add_edge(edge22_21)

    topology.add_edge(edge21_23)
    topology.add_edge(edge23_21)

    topology.add_edge(edge21_24)
    topology.add_edge(edge24_21)

    topology.add_edge(edge21_25)
    topology.add_edge(edge25_21)


def auctioning(bids, operator):
    auction = Auction.SDNAuction(bids, operator)
    # bids.clear()
    return auction


def bids_creation(bids_created, infra_operator, operators_created):
    optimal_file = open("gerador_" + str(len(bids_created)) + ".dat", "w+")
    greedy_file = open("greedy_gerador_" + str(len(bids_created)) + ".dat", "w+")
    print("Loading files...\n")

    num_bids = len(bids_created)

    GenerateFile(bids=bids_created, operators=operators_created, infra_operator=infra_operator,
                 file_optimal=optimal_file, file_greedy=greedy_file, num_bids=num_bids)


def main():
    num_clients = 2240
    num_operators = 5
    operators = []
    operators_created = []
    bids_created = []
    topology = Graph()

    # Create network topology
    create_network_topology(topology, num_vnf_services=5)

    # Resource advertisement phase
    infra_operator = InfrastructureOperator(num_nodes=27, num_links=36, num_vnf_services=5,
                                            service_capacity=100, topology=topology)

    flag = 1

    ## CREATING FILES ##

    if flag == 1:
        # Operators creation + clients creation + operator's update demands phases
        # 1400. 2800. 5600. 11200. 28000. Divided by num_operators

        for i in range(num_operators):
            operators_created.append(Data.Operator.NetworkOperator(id="operator" + str(i), topology=topology,
                                                                   infra_operator=infra_operator, num_clients=num_clients))
            for j in range(num_clients):
                bids_created.append(operators_created[i].clients[j].bid)

        bids_creation(bids_created, infra_operator, operators_created)

    ## READING FILE ##

    elif flag == 2:

        greedy_file = open("greedy_gerador_" + str(num_clients * num_operators) + ".dat", "r")

        ReadFile(file_greedy=greedy_file, num_bids= num_clients * num_operators, infra_operator=infra_operator)

        for i in range(num_operators):
            if i == 0:
                clients_id = ReadFile.clients_operator0
            elif i == 1:
                clients_id = ReadFile.clients_operator1
            elif i == 2:
                clients_id = ReadFile.clients_operator2
            elif i == 3:
                clients_id = ReadFile.clients_operator3
            elif i == 4:
                clients_id = ReadFile.clients_operator4

            operators.append(SDNAuctioning.Operator.NetworkOperator(id="operator" + str(i) + "\n", topology=topology,
                                                                    infra_operator=infra_operator, clients_id=clients_id,
                                                                    bids=ReadFile.bids))

        # FIRST AUCTION #
        results = open("results_greedy_" + str(num_clients * num_operators) + ".dat", "a+")

        accepted_bids = []
        market_valuation = []
        operator_revenue = []
        accepted_bids_percentage = []
        mean_bid_price = []
        op0 = []
        op1 = []
        op2 = []
        op3 = []
        op4 = []

        for i in range(10):
            auction = auctioning(bids=ReadFile.bids, operator=infra_operator)

            accepted_bids.append(auction.accepted_bids)
            market_valuation.append(auction.market_valuation)
            operator_revenue.append(auction.operator_revenue)
            accepted_bids_percentage.append(auction.accepted_bids_percentage)
            mean_bid_price.append(auction.mean_bid_price)
            op0.append(auction.counter_operator0)
            op1.append(auction.counter_operator1)
            op2.append(auction.counter_operator2)
            op3.append(auction.counter_operator3)
            op4.append(auction.counter_operator4)

            results.write("Results #" + str(i) + "\r\n")
            results.write("accepted bids: " + str(auction.accepted_bids) + "\r\n")
            results.write("market valuation: " + str(auction.market_valuation) + "\r\n")
            results.write("infrastructure revenue: " + str(auction.operator_revenue) + "\r\n")
            results.write("percentage of accepted bids: " + str(auction.accepted_bids_percentage) + "\r\n")
            results.write("mean bid price: " + str(auction.mean_bid_price) + "\r\n")
            results.write("op0: " + str(auction.counter_operator0) + "\r\n")
            results.write("op1: " + str(auction.counter_operator1) + "\r\n")
            results.write("op2: " + str(auction.counter_operator2) + "\r\n")
            results.write("op3: " + str(auction.counter_operator3) + "\r\n")
            results.write("op4: " + str(auction.counter_operator4) + "\r\n\r\n")

        results.write("Log \r\n")
        results.write("accepted_bids_" + str(num_clients * num_operators) + " =" + str(accepted_bids) + "\r\n")
        results.write("market_valuation_" + str(num_clients * num_operators) + " =" + str(market_valuation) + "\r\n")
        results.write("infrastructure_revenue_" + str(num_clients * num_operators) + " =" + str(operator_revenue) + "\r\n")
        results.write("percentage_accepted_bids_" + str(num_clients * num_operators) + " =" + str(accepted_bids_percentage) + "\r\n")
        results.write("mean_bid_price_" + str(num_clients * num_operators) + " =" + str(mean_bid_price) + "\r\n")
        results.write("op0_" + str(num_clients * num_operators) + " =" + str(op0) + "\r\n")
        results.write("op1_" + str(num_clients * num_operators) + " =" + str(op1) + "\r\n")
        results.write("op2_" + str(num_clients * num_operators) + " =" + str(op2) + "\r\n")
        results.write("op3_" + str(num_clients * num_operators) + " =" + str(op3) + "\r\n")
        results.write("op4_" + str(num_clients * num_operators) + " =" + str(op4) + "\r\n\r\n")

        results.close()

        # for i in range(len(operators)):
        #     for j in range(len(operators[i].clients)):
        #         operators[i].clients[j].update_client()

        # # SECOND AUCTION #

        # random_operator = random.choice(operators)

        # Auction.HubAuction(operator=random_operator, clients=random_operator.clients)


if __name__ == "__main__":
    main()
