'''
    Erdos-Renyi (E.R) random graph distribution model.It has 2(N,p) parameters.N is the number of nodes in
    the graph,and p is the probability for any pair of nodes to be connected by an edge.
'''
from scipy.stats import bernoulli
import networkx as nx
# >>>bernoulli.rvs(p=0.2)    #the rvs method to generate one single realization of a Bernoulli random variable.
N = 20      #sample case
p = 0.2     #sample case

def er_graph(N, p):
    G = nx.Graph()
    G.add_nodes_from(range(N))
    for node1 in G.nodes():
        for node2 in G.nodes():
            if node1 < node2 and bernoulli.rvs(p=p) == True: #>>>if bernoulli.rvs(p=p): is equally true since only if b.rvs==1 it will enter the loop
                G.add_edge(node1,node2)
    return G

nx.draw(er_graph(50,0.08), node_size=40, node_color="gray")
plt.show()
