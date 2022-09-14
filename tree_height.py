# python3

import sys
import threading

def build_tree(root_node, nodes):
    children = [
        build_tree(child, nodes)
        for child, node in enumerate(nodes)
        if node == root_node
    ]
    return {'key': root_node, 'children': children}

def compute_height(tree):
    return 1 + max((compute_height(c) for c in tree['children']), default=-1)

def main():
    input()  # Throw away the number of nodes
    tree = build_tree(-1, list(map(int, input().split())))
    print(compute_height(tree))

if __name__ == '__main__':
    main()
