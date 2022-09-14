def is_even(p):
    sign = 0  # sign = the number of transpositions mod 2
    s = 0  # first s elements are at the right places
    n = len(p)
    test = 0
    while s < n-1:
        u = s
        t = s
        #print(t)
        # a[t] is minimal among a[s+1]..a[u];
        while u < n-1:
            u = u + 1
            if p[u] < p[t]:
                t = u
                test += 1

            # a[t] is minimal among a[s+1]..a[n]
        tmp = p[s]
        p[s] = p[t]
        p[t] = tmp
        s= s+1
    return test

p=   [1, 2, 3, 5, 6]
print(is_even(p))

