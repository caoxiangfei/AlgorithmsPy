# python3
import sys

def BWT(text):
    n = len(text)
    mat = [None for _ in range(n)]
    text1 = [_ for _ in text]
    #print(text1)

    for i in range(n):
        s = text1.pop(0)

        text1.append(s)
        #print(text1)
        e = tuple(text1)
        mat[i] = e
    mat.sort()
    bwt = ''
    for m in mat:
        bwt += m[-1]
    return bwt

if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(BWT(text))