# Uses python3
import sys


def computeprefix(text):
    n = len(text)
    s = [None for _ in range(n)]
    s[0] = 0
    border = 0
    for i in range(1, n):
        while border > 0 and (text[i] != text[border]):
            border = s[border - 1]
        if text[i] == text[border]:
            border = border + 1
        else:
            border = 0
        s[i] = border
    return s


def kmp(pattern, text):
    string = pattern + '$' + text
    s = computeprefix(string)
    result = []
    n = len(pattern)
    for i in range(n, len(string)):
        if s[i] == n:
            result.append(i - 2*n)

    return result




if __name__ == '__main__':
    input = sys.stdin.read()
    m, n = map(int, input.split())
    for r  in kmp(m, n):
        print(r)

#pattern = 'ATA'
#text = 'ATATA'
#print(kmp(pattern, text))