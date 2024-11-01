import networkx as nx # type: ignore
import matplotlib.pyplot as plt

G = nx.Graph()
for i in range(1, 6):
    G.add_node(i)

for i in range(1, 11):
    for j in range(i+1, 11):
        G.add_edge(i, j)

# G = nx.complete_graph(10)

nx.draw(G)
plt.show()