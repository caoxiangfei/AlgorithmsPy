# python3

import sys


def build_trie(patterns):
    tree = dict()
    tree[0] = {}
    root = 0
    count = 0
    #lastnode = 0
    for pattern in patterns:
        pattern = pattern + '$'
        currentnode = root
        for i in range(len(pattern)):
            currentsymbol = pattern[i]
            # print(currentsymbol)
            # print(currentnode, '*')
            # print(tree)
            if (currentnode in tree.keys()) and (currentsymbol in tree[currentnode]):
                currentnode = tree[currentnode][currentsymbol]
            else:
                count = count + 1
                newnode = count
                # print(lastnode)
                if currentnode not in tree.keys():
                    tree[currentnode] = {}
                # print(tree[lastnode])
                tree[currentnode][currentsymbol] = newnode
                currentnode = newnode
        # lastnode = newnode

    # write your code here
    return tree


def solve(text, n, patterns):
    result = [None]
    trie = build_trie(patterns)
    #i = 0
    #v = 0
    #print(trie)
    for i in range(len(text)):
        v = 0
        w = i
        count = 0
        while count < len(trie):
            if '$' in trie[v].keys() and (i != result[-1]):
                result.append(i)
                #print(result)
            elif w < len(text) and (text[w] in trie[v].keys()):
                v = trie[v][text[w]]
                w += 1
            else:
                count = len(trie)

    result.pop(0)

    return result



text = sys.stdin.readline().strip()
n = int(sys.stdin.readline().strip())
patterns = []
for i in range(n):
    patterns += [sys.stdin.readline().strip()]

ans = solve(text, n, patterns)

sys.stdout.write(' '.join(map(str, ans)) + '\n')

#text = 'ACATA'
#text1 = 'AATCGGGTTCAATCGGGGT'
#n = 2
#patterns = ['AT', 'A', 'AG']
#patterns1 = ['ATCG', 'GGGT']
#print(solve(text1, n, patterns1))
