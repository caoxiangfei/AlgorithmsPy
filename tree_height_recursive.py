# python3

import sys
import threading

def get_depth(index, parents):
    parent = parents[index]
    if parent == -1:
        return 1
    else:
        return get_depth(parent, parents) + 1

def compute_height(n, parents):
    # Replace this code with a faster implementation
    max_height = float('-inf')
    leaf = []
    for j in range(n):
        if ((j in parents) == False) and parents[j] != -1:
            leaf.append(j)


    for i in leaf:
        depth = get_depth(i, parents)
        if depth > max_height:
            max_height = depth


    return max_height



def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()

#index = 9
#parents = [9, 7, 5, 5, 2, 9, 9, 9, 2, -1]
#print(compute_height(10, parents) )