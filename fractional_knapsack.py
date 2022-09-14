# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.0
    i = len(weights) - 1
    vw = []
    for w in range(len(weights)):
        vw.append([weights[w], values[w]/weights[w]])

    def sortSecond(val):
        return val[1]
    vw.sort(key = sortSecond)



            #print(vw)

    while capacity > 0 and i >= 0:
        a = min(vw[i][0], capacity)
        value = value + a * vw[i][1]
        capacity = capacity - a
        #weights[i] = weights[i] - a
        i = i - 1


    # write your code here

    return value



if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.4f}".format(opt_value))

