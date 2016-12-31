import matplotlib.pyplot as plt
import networkx as nx

G = nx.karate_club_graph()
nx.draw(G, with_labels=True, node_color="lightblue", edge_color="gray")
plt.show()

# >>>G.degree()          #get access to node degree's(no of links) stores as a dict in networkx
# >>>G.degree()[33]      #gives the value(degree) for id 33
# >>>G.degree(33)        #gives the value(degree) for id 33        #same
# >>>G.degree(0) is G.degree()[0]     #True
