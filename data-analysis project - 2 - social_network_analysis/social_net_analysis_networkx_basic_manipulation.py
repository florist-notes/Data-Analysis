import networkx as nx

G = nx.Graph()  #we have an empty graph called G.
G.add_node(1) # node no 1 has been added to our graph.
G.add_nodes_from([2,3]) # add multiple nodes to graph,input is a list
G.add_nodes_from(["u","v"]) #node labels can be strings as well
# >>>G.nodes() # to check the nodes in graph
G.add_edge(1,2)
G.add_edge("u","v")
G.add_edges_from([(1,3),(1,4),(1,5),(1,6)]) #python will add these non-existant nodes automatically
G.add_edge("u","w")
# >>>G.edges() # to check the edges in graph
G.remove_node(2) #remove node no 2 from graph
G.remove_nodes_from([4,5]) # removes multiple nodes from graph,input is a list
G.remove_edge(1,3)
G.remove_edges_from([(1,2),("u","v")])

G.number_of_nodes() #total no of nodes in graph
G.number_of_edges() #total no of edges in graph
