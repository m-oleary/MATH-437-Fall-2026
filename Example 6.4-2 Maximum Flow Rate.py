import networkx as nx
import matplotlib.pyplot as plt

# Choose a directional graph
G = nx.DiGraph()

# Store the numbers as 'capacity' so the flow functions find them by default
G.add_weighted_edges_from([
    (1, 4, 10),
    (1, 3, 30),
    (1, 2, 20),
    (2, 5, 30),
    (2, 3, 40),
    (3, 4, 10),
    (3, 5, 20),
    (4, 3, 5),
    (4, 5, 20),
], weight="capacity")

flow_value, flow_dict = nx.maximum_flow(G, 1, 5)
print(f"{flow_value=}")
print(f"{flow_dict=}")

# 1. Compute a layout to lock down node positions
pos = nx.spring_layout(G, seed=22)  # Seed chosen by trying some graphs

# 2. Split edges into those with a reverse partner (e.g. 3->4 and 4->3) and the rest
bidirectional = [(u, v) for u, v in G.edges if G.has_edge(v, u)]
straight = [e for e in G.edges if e not in bidirectional]

capacities = nx.get_edge_attributes(G, "capacity")
straight_labels = {e: capacities[e] for e in straight}
curved_labels = {e: capacities[e] for e in bidirectional}

NODE_SIZE = 700
CURVE = "arc3,rad=0.08"

# 3. Nodes and node labels
nx.draw_networkx_nodes(G, pos, node_color="thistle", node_size=NODE_SIZE)
nx.draw_networkx_labels(G, pos, font_weight="bold")

# 4. Edges: straight for one-way pairs, curved for two-way pairs
nx.draw_networkx_edges(G, pos, edgelist=straight, edge_color="red", node_size=NODE_SIZE)
nx.draw_networkx_edges(G, pos, edgelist=bidirectional, edge_color="red",
                       node_size=NODE_SIZE, connectionstyle=CURVE)

# 5. Edge labels: the curved ones use the same connectionstyle so they follow the arcs
nx.draw_networkx_edge_labels(G, pos, edge_labels=straight_labels)
nx.draw_networkx_edge_labels(G, pos, edge_labels=curved_labels, connectionstyle=CURVE)

# 6. Display the plot
plt.axis("off")
plt.show()