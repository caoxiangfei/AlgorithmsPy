# Uses python3
import sys

def optimal_weight(W, w):
    # write your code here
    n = len(w)
    value = []
    v = [0] + w
    w = v
    for i in range(n+1):
        value.append([])
        for j in range(W+1):
            value[i].append(0)
    for i in range(1, n+1):
        for we in range(1, W+1):
            value[i][we] = value[i-1][we]
            if w[i] <= we:
                val = value[i-1][we-w[i]] + v[i]
                if value[i][we] < val:
                    value[i][we] = val
    return value[n][W]









if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w))
