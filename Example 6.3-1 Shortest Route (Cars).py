import networkx as nx

G = nx.Graph()

G.add_weighted_edges_from([
    (1,2,4000),
    (1,3,5400),
    (1,4,9800),
    (2,3,4300),
    (2,4,6200),
    (2,5,8700),
    (3,4,4800),
    (3,5,7100),
    (4,5,4900)
])

path = nx.shortest_path(G, 1, 5, weight="weight")

length = nx.shortest_path_length(G, 1, 5, weight="weight")

print(path, length)