# python3

import sys
import threading



def compute_height(n, parents):
    # Replace this code with a faster implementation
    max_height = float('-inf')
    depths = [None]*n
    leaf = []
    for j in range(n):
        if ((j in parents) == False) and parents[j] != -1:
            leaf.append(j)

    for idx in leaf:
        parent_stack = []
        id = idx
        parent = parents[id]
        while parent != -1:
            parent_stack.append(id)
            id, parent = parent, parents[parent]
        #print(parent_stack, id, parent )
        if parent == -1:
            depth = 1
        else:
            depth = depths[id]
        while parent_stack:
            depths[parent_stack.pop()] = depth
            depth += 1
        #print(depths, depth)
        if max_height < depth:
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

