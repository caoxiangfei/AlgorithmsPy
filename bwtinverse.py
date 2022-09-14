# python3
import sys

def InverseBWT(bwt):
    # write your code here
    n = len(bwt)
    bwt1 = []
    for i in range(n):
        bwt1.append([bwt[i], i])

    bwt1end = tuple(bwt1)
    #print(bwt1end)
    bwt1.sort()
    for i in range(n):
        bwt1[i].append(i)
    bwt2 = [None for i in range(n)]
    for i in range(n):
        bwt2[bwt1[i][1]] = bwt1[bwt1[i][2]]
    #print(bwt1)
    #print(bwt2)
    result = []
    h = 0
    count = 0
    while count < n:
        temp = bwt2[h][0]
        result.append(temp)
        h =bwt2[h][-1]
        count += 1
    result.reverse()
    result.pop(0)
    result.append('$')

    c = ''.join(result)

    return c


if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    print(InverseBWT(bwt))