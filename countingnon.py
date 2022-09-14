import itertools as it
count = 0
for d in it.product(range(10), repeat=4):
    if d[0] <= d[1] and d[1] <= d[2] and d[2] < d[3]:
        count += 1
        print(d)
print(count)