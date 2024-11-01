import networkx as nx # type: ignore
import numpy

G = nx.read_edgelist('edgeFile.txt')
N = list(G.nodes())

spll = []
for u in N:
    for v in N:
        l = nx.shortest_path(G, u, v)
        print(f'shortest path between {u} and {v} is {l}')
        spll.append(l)

min_spll = min(spll)
max_spll = max(spll)
avg = numpy.average(spll)

print(f'min shortest path len is {min_spll}')
print(f'max shortest path len is {max_spll}')
print(f'avg shortest path len is {avg}')