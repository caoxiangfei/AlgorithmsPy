#Uses python3

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


def distance(adj, s, t):
    dist = bfs(adj, s)
    if dist[t] != float('inf'):
        return dist[t]
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    s, t = data[2 * m] - 1, data[2 * m + 1] - 1
    print(distance(adj, s, t))
