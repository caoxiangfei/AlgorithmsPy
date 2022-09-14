# python3
import sys

def compute_min_refills(distance, m, stops):
    numrefills = 0
    currentrefill = 0
    stop = list(stops)
    n = len(stop)
    stop = [0] + stop + [distance]
    while currentrefill <= n:
        lastrefill = currentrefill
        while currentrefill <= n and (stop[currentrefill + 1] - stop[lastrefill] <= m):
            currentrefill += 1
        if currentrefill == lastrefill:
            return -1
        if currentrefill <= n:
            numrefills += 1
    return numrefills





    # write your code here


if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    print(compute_min_refills(d, m, stops))
