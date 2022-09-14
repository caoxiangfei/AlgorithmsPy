#Uses python3
import sys


# Return the trie built from patterns
# in the form of a dictionary of dictionaries,
# e.g. {0:{'A':1,'T':2},1:{'C':3}}
# where the key of the external dictionary is
# the node ID (integer), and the internal dictionary
# contains all the trie edges outgoing from the corresponding
# node, and the keys are the letters on those edges, and the
# values are the node IDs to which these edges lead.
def build_trie(patterns):
    tree = dict()
    tree[0] = {}
    root = 0
    count = 0
    lastnode = 0
    for pattern in patterns:
        currentnode = root
        for i in range(len(pattern)):
            currentsymbol = pattern[i]
            #print(currentsymbol)
            #print(currentnode, '*')
            #print(tree)
            if (currentnode in tree.keys()) and (currentsymbol in tree[currentnode]):
                currentnode = tree[currentnode][currentsymbol]
            else:
                count = count + 1
                newnode = count
                #print(lastnode)
                if currentnode not in tree.keys():
                    tree[currentnode] = {}
                    #print(tree[lastnode])
                tree[currentnode][currentsymbol] = newnode
                currentnode = newnode
                #lastnode = newnode

    # write your code here
    return tree



if __name__ == '__main__':
    patterns = sys.stdin.read().split()[1:]
    tree = build_trie(patterns)
    for node in tree:
        for c in tree[node]:
            print("{}->{}:{}".format(node, tree[node][c], c))

#patterns = ['AT$', 'AG$', 'AC$']
#print(build_trie(patterns))
