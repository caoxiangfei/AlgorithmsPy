#Uses python3

import sys
import random

clock = 1
def partition2(a, l, r):
    x = a[l][1]
    j = l
    for i in range(l + 1, r + 1):
        if a[i][1] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    m = partition2(a, l, r)
    randomized_quick_sort(a, l, m - 1);
    randomized_quick_sort(a, m + 1, r);


def previsit(v, pre):
    global clock
    pre[v] = clock
    clock = clock + 1


def postvisit(v, post):
    global clock
    post.append([v, clock])
    clock = clock + 1



def reverseg(adj):
    edges = []
    for i in range(len(adj)):
        if adj[i] != []:
            for vertex in adj[i]:
                edges.append([i, vertex])
    edgesr = [[j, i] for i, j in edges]
    adjr = [[] for _ in range(len(adj))]
    for a, b in edgesr:
        adjr[a].append(b)
    return adjr

def deleteg(adj, v):
    adj[v] = [None]
    for edg in adj:
        if v in edg:
            edg.remove(v)

def explore(adj, v, visited, path):
    if adj[v] != [None]:
        visited[v] = True
        path.append(v)
        previsit(v, pre)

        if adj[v] != []:
            for w in adj[v]:
                if (visited[w] is None):
                    explore(adj, w, visited, path)

        postvisit(v, post)




def dfs(adj, visited):
    n = len(adj)

    for v in range(n):
        if visited[v] is None:
            explore(adj, v, visited, path)


def acyclic(adj):
    #order = []
    n = len(adj)
    visited = [None for _ in range(n)]
    #adjr = reverseg(adj)
    #print(adjr)
    dfs(adj, visited)
    randomized_quick_sort(post, 0, n-1)
    #print(post)
    vertices = [post[_][0] for _ in range(n)]
    vertices.reverse()
    #print(vertices)
    #while len(vertices) > 0:
        #v = vertices[-1]
        #path1 = []
        #visited1 = [None for _ in range(n)]
        #print(v)
        #print(adj)
        #print(visited)
        #explore(adj, v, visited1, path1)
        #for p in path1:
            # print(adj, p)
            #order.insert(0, p)
            #vertices.remove(p)
            #deleteg(adj, p)


    return vertices

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    pre = [None for _ in range(len(adj))]
    post = []
    visited = [None for _ in range(len(adj))]
    path = []
    order = acyclic(adj)
    for x in order:
        print(x + 1, end=' ')

