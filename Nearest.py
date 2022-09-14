import networkx as nx

def nearest_neighbors(g):
    current_node = 0
    path = [current_node]
    n = g.number_of_nodes()

    # We'll repeat the same routine (n-1) times
    for _ in range(n - 1):
        next_node = None
        # The distance to the closest vertex. Initialized with infinity.
        min_edge = float("inf")
        for v in g.nodes():
          if min_edge >= g[current_node][v]['weight']:
             min_edge = g[current_node][v]['weight']
             next_node = v
            # Write your code here: decide if v is a better candidate than next_node.
            # If it is, then update the values of next_node and min_edge

        assert next_node is not None
        path.append(next_node)
        current_node = next_node

    weight = sum(g[path[i]][path[i + 1]]['weight'] for i in range(g.number_of_nodes() - 1))
    weight += g[path[-1]][path[0]]['weight']
    return weight
