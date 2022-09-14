# Uses python3
import sys

def get_change(m):
    #write your code here
    coins = [1, 3, 4]
    if m == 0:
        return 0


    change = list(range(m+1))
    for w in change:
        w = float('inf')
    change[0] = 0

    for c in range(1, m+1):

        for  i in range(3):
            if c >= coins[i]:
                minnumcoins = (change[c - coins[i]] + 1)
                if minnumcoins < change[c]:
                    change[c] = minnumcoins




    return change[m]

if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))

