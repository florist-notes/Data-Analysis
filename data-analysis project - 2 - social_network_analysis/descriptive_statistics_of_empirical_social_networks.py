import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

A1 = np.loadtxt("adj_allVillageRelationships_vilno_1.csv", delimiter=",")  #np.loadtxt is used to read in the CSV files, the adjacency matrices.
A2 = np.loadtxt("adj_allVillageRelationships_vilno_2.csv", delimiter=",")
# now convert the adjacency matrices to graph objects.
G1 = nx.to_networkx_graph(A1)
G2 = nx.to_networkx_graph(A2)

'''
    let's count the number of nodes and the number of edges in the networks.In addition, each node has a total number of edges,
    its degree.Let's also calculate the mean degree for all nodes in the network.
'''
def basic_net_stats(G):
    print("Number of nodes : %d" %G.number_of_nodes())
    print("Number of edges : %d" %G.number_of_edges())
    print("Average degree : %.2f" % np.mean(list(G.degree().values())))

basic_net_stats(G1)
basic_net_stats(G2)

plot_degree_distribution(G1)
plot_degree_distribution(G2)
plt.show()
