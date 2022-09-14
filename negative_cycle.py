#Uses python3

import sys


def bellmanford(adj, cost, s):
    dist = []
    prev = []
    for i in range(len(adj)):
        dist.append(float('inf'))
        prev.append(None)

    dist[s] = 0
    for u in range(len(adj)):
        for j in range(len(adj[u])):
            if dist[adj[u][j]] > dist[u] + cost[u][j]:
                #print(dist[adj[u][j]] , dist[u] + cost[u][j])
                dist[adj[u][j]] = dist[u] + cost[u][j]
                prev[adj[u][j]] = u

    return dist


def negative_cycle(adj, cost):
    for s in range(len(adj)):
        dist1 = bellmanford(adj, cost, s)
        if dist1[s] < 0:
            return 1

    #write your code here
    return 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    adj = [[] for _ in range(n)]
    cost = [[] for _ in range(n)]
    for ((a, b), w) in edges:
        adj[a - 1].append(b - 1)
        cost[a - 1].append(w)
    print(negative_cycle(adj, cost))








