import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

gen = nx.connected_component_subgraphs(G1)
g = gen.__next__()
# >>>type(g)
# >>>g.number_of_nodes()
# >>>len(gen.__next__())  #returns number of nodes in that subcomponent
# >>>len(G1)  #returns the total number of nodes in the graph

G1_LCC = max(nx.connected_component_subgraphs(G1), key=len)
G2_LCC = max(nx.connected_component_subgraphs(G2), key=len)
# >>>len(G1_LCC)
# >>>G1_LCC.number_of_nodes()
( G1_LCC.number_of_nodes() / G1.number_of_nodes() )*100
# we see that 97.9% of all of the nodes of graph G1 are contained in the largest connected component.
( G2_LCC.number_of_nodes() / G2.number_of_nodes() )*100
# we see that 92.4% of all of the nodes of graph G1 are contained in the largest connected component.

plt.figure()
nx.draw(G1_LCC, node_color = "red", edge_color = "gray", node_size = 20)
# >>>plt.savefig("component.pdf")
plt.figure()
nx.draw(G2_LCC, node_color = "red", edge_color = "gray", node_size = 20)
plt.show()
