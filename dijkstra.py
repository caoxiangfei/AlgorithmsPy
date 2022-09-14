#Uses python3

import sys
import queue




def shiftdown1(H, j):
    minindex = j
    size = len(H)
    l = 2*j + 1
    r = 2*j + 2

    if l<size and H[l][1] < H[minindex][1]:
        minindex = l
    if r<size and H[r][1] < H[minindex][1]:
        minindex = r
    if j != minindex:
        H[j], H[minindex] = H[minindex], H[j]
        return shiftdown1(H, minindex)
    else:
        return H



def shiftup1(H, i):
    parent = (i-1) // 2

    while i > 0 and H[parent][1] > H[i][1]:
        H[i], H[parent] = H[parent], H[i]
        i = parent
        return shiftup1(H, i)
    return H



def insert1(H, p):
    H.append(p)
    i = len(H)-1
    shiftup1(H, i)
    return H



def extractmin1(H):

    result = H[0]

    H[0] = H[-1]
    #print(result)
    H.pop()
    #print(H)
    shiftdown1(H, 0)

    return result[0]

def build_heap1(data):
    n = len(data)
    a = list(range(0, n // 2))
    a.reverse()
    for i in a:
        shiftdown1(data, i)
    return data

def changepriority(H, i, p):
    oldp = H[i]
    H[i] = p
    if p < oldp:
        shiftup1(H, i)
    else:
        shiftdown1(H, i)





def distance(adj, cost, s, t):
    dist = []
    prev = []
    for i in range(len(adj)):
        dist.append(float('inf'))
        prev.append(None)

    dist[s] = 0
    h = [[s, dist[s]]]
    while len(h) > 0:
        u = extractmin1(h)
        #print(adj[u])
        for j in range(len(adj[u])):
            if dist[adj[u][j]] > dist[u] + cost[u][j]:
                dist[adj[u][j]] = dist[u] + cost[u][j]
                prev[adj[u][j]] = u
                insert1(h, [adj[u][j], dist[adj[u][j]]])


    #write your code here
    if dist[t] == float('inf'):
        return -1

    return dist[t]


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
    s, t = data[0] - 1, data[1] - 1
    print(distance(adj, cost, s, t))


#edges = [[[1, 2], 1], [[4, 1], 2], [[2, 3], 2], [[1, 3], 5]]
#edges1 = [[5, 2], [1, 3], [3, 4], [1, 4]]
#edges1 = [[[1, 2], 4], [[1, 3], 2], [[2, 3], 2], [[3, 2], 1], [[2, 4], 2], [[3, 5], 4], [[5, 4], 1], [[2, 5], 3], [[3, 4], 4]]
#edges2 = [[[1, 2], 7], [[1, 3], 5], [[2, 3], 2]]
#s = 2
#t = 1

#adj = [[] for _ in range(3)]
#cost = [[] for _ in range(3)]
#for ((a, b), w) in edges2:
    #adj[a - 1].append(b - 1)
    #cost[a - 1].append(w)

#print(adj)
#print(distance(adj, cost, s, t))