import networkx as nx
import math
import matplotlib.pyplot as plt

# Choose a directional graph
G = nx.DiGraph()

# https://networkx.org/documentation/stable/reference/classes/generated/networkx.Graph.add_weighted_edges_from.html
G.add_weighted_edges_from([
    (1,2,-math.log10(0.2)),
    (1,3,-math.log10(0.9)),
    (2,3,-math.log10(0.6)),
    (2,4,-math.log10(0.8)),
    (3,4,-math.log10(0.1)),
    (3,5,-math.log10(0.3)),
    (4,5,-math.log10(0.4)),
    (4,6,-math.log10(0.35)),
    (5,7,-math.log10(0.25)),
    (6,7,-math.log10(0.5))

])

# https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.shortest_paths.generic.shortest_path.html
path = nx.shortest_path(G, 1, 7, weight="weight")

# https://networkx.org/documentation/stable/reference/algorithms/generated/networkx.algorithms.shortest_paths.generic.shortest_path_length.html 
length = nx.shortest_path_length(G, 1, 7, weight="weight")

probability = math.pow(10,-length)

print(f"{path=}")
print(f"{length=:.4f}")
print(f"{probability=:.4f}")

# Shouldn't we draw the result?

# 1. Compute a layout to lock down node positions
# https://networkx.org/documentation/stable/reference/generated/networkx.drawing.layout.spring_layout.html
pos = nx.spring_layout(G,seed=6) # Seed chosen by trying some graphs
# Alternatives here can be found at https://networkx.org/documentation/stable/reference/drawing.html#module-networkx.drawing.layout

# 2. Draw the base graph (nodes and edges)
# https://networkx.org/documentation/stable/reference/generated/networkx.drawing.nx_pylab.draw.html
nx.draw(G, pos, with_labels=True, node_color="thistle", edge_color="red", node_size=700, font_weight="bold")

# 3. Extract the 'weight' attribute into a dictionary and round each value to 5 decimal places
# https://docs.python.org/3/builtins/functions.html#round
edge_labels = {k: round(v, 5) for k, v in nx.get_edge_attributes(G, "weight").items()}

# 4. Draw the weight labels onto the edges
# https://networkx.org/documentation/stable/reference/generated/networkx.drawing.nx_pylab.draw_networkx_edge_labels.html 
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# 5. Display the plot
plt.show()
