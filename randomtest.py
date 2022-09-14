
import sys

import queue

def bfs(g, s):
    dist = [float('inf') for _ in range(len(g))]
    dist[s] = 0
    q = queue.Queue(maxsize=len(g))
    q.put(s)
    while q.empty() is False:
        u = q.get()
        for v in g[u]:
            if dist[v] == float('inf'):
                q.put(v)
                dist[v] = dist[u] + 1
    return dist

"""def explore(adj, v, visited):
    visited.append(v)
    #print(visited)
    for ad in adj:
        #print(ad[0], ad[1], v)
        #print(a == ad[0])
        #print(ad[1] in visited)
        if v == ad[0] and (ad[1] not in visited):
            #print(v)
            w = ad[1]
            #print(w)
            explore(adj, w, visited)

        elif v == ad[1] and (ad[0] not in visited):
            w = ad[0]
            explore(adj, w, visited)





visited = []
adj = [[1, 2], [3, 2], [4, 3]]
a = 1
explore(adj, a, visited)
print(visited) """




edges = [[[1, 2], -5], [[4, 1], 2], [[2, 3], 2], [[3, 1], 1]]
#edges1 = [[5, 2], [1, 3], [3, 4], [1, 4]]


adj = [[] for _ in range(4)]
cost = [[] for _ in range(4)]
for ((a, b), w) in edges:
    adj[a - 1].append(b - 1)
    cost[a - 1].append(w)

print(adj)
print(cost)

#print(adj)
#print(edgesr)
    #print(reach(adj, x, y))




edges = [[[1, 2], -5], [[4, 1], 2], [[2, 3], 2], [[3, 1], 1]]
#edges = [[[1, 2], 1], [[4, 1], 2], [[2, 3], 2], [[1, 3], 5]]

edges1 = [[[1, 2], 4], [[1, 3], 2], [[2, 3], -3], [[3, 2], 1], [[2, 4], 2], [[3, 5], 4], [[5, 4], 1], [[2, 5], 3], [[3, 4], 4]]
edges2 = [[[1, 2], -7], [[1, 3], 5], [[2, 3], 2]]
edges3 = [[[2, 8], 12], [[4, 9], -1], [[4, 2], 19], [[4, 6], 5], [[4, 5], 10], [[4, 7], 17], [[4, 1], 4], [[6, 2], -17], [[7, 3], 16], [[8, 1], 2], [[8, 10], -16], [[9, 10], 13], [[10, 8], 7]]
n = 4
adj = [[] for _ in range(n)]
cbc = [[] for _ in range(n)]
cost = [[] for _ in range(n)]
for ((a, b), w) in edges:
    adj[a - 1].append(b - 1)
    cbc[a - 1].append(b - 1)
    cost[a - 1].append(w)


pre = [None for _ in range(len(adj))]
post = []
visited = [None for _ in range(len(adj))]
path = []


print(adj)
print(cost)
print(negative_cycle(adj, cost))

