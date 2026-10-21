import networkx as nx

G = nx.Graph()

# https://networkx.org/documentation/stable/reference/classes/generated/networkx.Graph.add_weighted_edges_from.html
G.add_weighted_edges_from([
    (1,2,1),
    (1,3,5),
    (1,4,7),
    (1,5,9),
    (2,3,6),
    (2,4,4),
    (2,5,3),
    (3,4,5),
    (3,6,10),
    (4,6,3)
])

# https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.tree.mst.minimum_spanning_tree.html
T = nx.minimum_spanning_tree(G)

print(sorted(T.edges(data="weight")))
print("Total weight:", T.size(weight="weight"))