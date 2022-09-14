
import networkx as nx


def dp(G) :
    n = G.number_of_nodes()
    T = [[float( 'inf'  )]*(1 << n) for _ in range(n)]

    T[0][1] = 0
    for s in range(1 << n):
        b=bin(s)[2:]
        if sum(int(b[k]) for k in range(len(b))) <= 1 or not (s & 1):
            continue

        for i in range(1, n):
            if not ((s >> i) & 1):
                continue
            for j in range(n):
                if j == i or not ((s >> j) & 1):
                    continue

                T[i][s] = min(T[i][s],
                              T[j][s ^ (1 << i)] + G[i][j][ 'weight' ])
                print(s ^ (1 << i), i, s, j, T[i][s])

    return min(T[i][(1 << n) - 1] + G[0][i][ 'weight' ]
            for i in range(1, n))

def get_graph(coordinates):
    g = nx.Graph()
    n = len(coordinates)
    for i in range(n):
        for j in range(i + 1):
            g.add_edge(i, j, weight = ((coordinates[i][0] - coordinates[j][0])**2 + (coordinates[j][1] - coordinates[i][1])**2)**0.5)
    return g

coordinates = [(166, 282), (43, 79), (285, 44), (0, 0)]
g = get_graph(coordinates)
dp(g)

# print((3>>j)&1)
#for s in range(1<<n):
    #b = bin(s)[2:]
    #if sum(int(b[k]) for k in range(len(b))) <= 1 or not (s & 1):
        #continue









