# Uses python3
import sys

def optimal_sequence(n):

    num = list(range(1, n+1))
    op = list(range(n+1))
    op[1] = 0
    for i in range(1, n):
        if num[i] % 2 != 0 and num[i] % 3 != 0:
            op[num[i]] = op[num[i]-1] + 1
        elif num[i] % 2 != 0 and num[i] % 3 == 0:
            op[num[i]] = min(op[num[i]-1] + 1, op[num[i]//3] + 1)
        elif num[i] % 3 != 0 and num[i] % 2 == 0:
            op[num[i]] = min(op[num[i]-1] + 1, op[num[i]//2] + 1)
        elif num[i] % 3 ==0 and num[i] % 2 ==0:
            op[num[i]] = min(op[num[i]//2] + 1, op[num[i]//3] + 1)
    sequence = [n]
    opf = op[n] - 1
    k = n - 1
    h = 0
    while k >= 0:

        if op[num[k]] ==  opf:
            if num[k] + 1 == sequence[h] or num[k] * 2 == sequence[h] or num[k] * 3 == sequence[h]:
                sequence.append(num[k])
                opf = opf - 1
                h = h + 1
        k = k - 1

    sequence.reverse()






    return sequence

input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')



