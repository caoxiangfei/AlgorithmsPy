#Uses python3

import sys

def explore(adj, v, visited):
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











    #return visited

def reach(adj, x, y):
    if x == y:
        return 1
    visited = []
    explore(adj, x, visited)
    for end in visited:
        if end == y:
            return 1
    return 0

    #write your code here
    #return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]

    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(reach(edges, x, y))

#visited = []
#adj = [[1, 2], [3, 2], [4, 3], [1, 4]]
#a = 1
#explore(adj, a, visited)
#print(visited)
