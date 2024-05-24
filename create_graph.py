# Adjusting the layout to make the graph more spread out
import matplotlib.pyplot as plt
import networkx as nx

# Labels for each node
labels = {
    1: "Taylor Swift",
    2: "Ed Sheeran",
    3: "Selena Gomez",
    4: "Ariana Grande",
    5: "Justin Bieber",
    6: "Beyoncé",
    7: "Jay-Z",
    8: "Kim Kardashian",
    9: "Dwayne Johnson",
    10: "Kevin Hart",
    11: "Ellen DeGeneres",
    12: "Oprah Winfrey",
    13: "Michelle Obama",
    14: "Kylie Jenner",
    15: "Kendall Jenner",
    16: "LeBron James",
}

# Connections between nodes
connections = {
    1: [2, 3, 4, 5],
    2: [1, 5, 6, 3],
    3: [1, 4, 8, 14],
    4: [3, 6, 5, 9, 8],
    5: [2, 4, 8, 1],
    6: [8, 7],
    7: [6],
    8: [6, 1, 5, 14],
    9: [6, 4, 10],
    10: [9, 11],
    11: [10, 12],
    12: [11, 7, 13],
    13: [12, 6],
    14: [8, 15, 3],
    15: [14, 16],
    16: [15, 1, 6],
}

# Create a directed graph
G = nx.DiGraph()

# Add nodes to the graph
for node in labels:
    G.add_node(node, label=labels[node])

# Add edges to the graph
for source, targets in connections.items():
    for target in targets:
        G.add_edge(source, target)

plt.figure(figsize=(14, 10))
pos = nx.spring_layout(G, k=4)  # Increase the spacing between nodes
nx.draw(G, pos, with_labels=True, labels=labels, node_size=4000, node_color="lightblue", font_size=8, arrows=True)

plt.title("Directed Graph of Celebrity Connections")

plt.show()