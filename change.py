# Uses python3
import sys

def get_change(m):
    coins = [10, 5, 1]
    back = 0
    i = 0
    while m > 0:
        while m  >= coins[i]:
            back += 1
            m = m - coins[i]
        i = i + 1
    return back






    #write your code here

if __name__ == '__main__':
        m = int(sys.stdin.read())
        print(get_change(m))
