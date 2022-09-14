c = dict()

for n in range(8):
    c[n, 0] = 1
    c[n, n] = 1
    for k in range(1, n):
        c[n, k] = c[n-1, k-1] + c[n-1, k]
        print(c)

print(c[7, 4])