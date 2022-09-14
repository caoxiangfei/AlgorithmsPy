# Uses python3
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def get_maximum_value(dataset):
    digits = []
    op = []
    for i in range(len(dataset)):
        if i % 2 == 0:
            digits.append(dataset[i])
        else:
            op.append(dataset[i])
    op = [0] + op
    m = []
    M = []
    n = len(digits)
    for i in range(n+1):
        m.append([])
        M.append([])
        for k in range(n+1):
            m[i].append(0)
            M[i].append(0)

    for i in range(1,n+1):
        m[i][i] = int(digits[i-1])
        M[i][i] = int(digits[i-1])
    for s in range(1, n):
        for i in range(1, n-s+1):
            j = i + s
            min0 = float('inf')
            max0 = float('-inf')
            for k in range(i, j):
                a = evalt(M[i][k], M[k+1][j], op[k])
                b = evalt(M[i][k], m[k+1][j], op[k])
                c = evalt(m[i][k], M[k+1][j], op[k])
                d = evalt(m[i][k], m[k+1][j], op[k])
                min0 = min(min0, a, b, c, d)
                max0 = max(max0, a, b, c, d)
            m[i][j], M[i][j] = min0, max0



    #write your code here
    return M[1][n]


if __name__ == "__main__":
    print(get_maximum_value(input()))

