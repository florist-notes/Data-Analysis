import matplotlib.pyplot as plt

def plot_degree_distribution(G):
    plt.hist(list(G.degree().values()), histtype="step")
    plt.xlabel(" Degree $k$ ")
    plt.ylabel(" $P(k)$ ")
    plt.title(" Degree distribution ")

G1 = er_graph(500,0.08)
plot_degree_distribution(G1)
G2 = er_graph(500,0.08)
plot_degree_distribution(G2)
G3 = er_graph(500,0.08)
plot_degree_distribution(G3)
plt.show()

    #1.2_extra graph
    #>>>G1 = er_graph(100, 0.03)
    #>>>plot_degree_distribution(G1)
    #>>>G2 = er_graph(100, 0.30)
    #>>>plot_degree_distribution(G2)
    #>>>plt.show()
