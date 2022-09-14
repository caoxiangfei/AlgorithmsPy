#Uses python3
import sys
import math


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
    if p[1] < oldp[1]:
        shiftup1(H, i)
    else:
        shiftdown1(H, i)


def weight(a, b, c, d):
    return ((a-b)**2 + (c-d)**2)**0.5

def minimum_distance(x, y):
    result = 0.
    cost = []
    parent = []
    for i in range(len(x)):
        cost.append(float('inf'))
        parent.append(None)
    cost[0] = 0.
    q = [[0, 0.]]
    for s in range(1, len(x)):
        q.append([s, float('inf')])
    while len(q) > 0:
        v = extractmin1(q)
        for j in range(len(x)):
            for p in range(len(q)):
                if q[p][0] == j and q[p][1] > weight(x[v], x[j], y[v], y[j]):
                    cost[j] = weight(x[v], x[j], y[v], y[j])
                    parent[j] = v
                    changepriority(q, p, [j, cost[j]])
    for c in cost:
        result = result + c


    #write your code here
    return result


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    print("{0:.9f}".format(minimum_distance(x, y)))

#x = [0, 0, 1, 3, 3]
#y = [0, 2, 1, 0, 2]
#print(minimum_distance(x, y))
