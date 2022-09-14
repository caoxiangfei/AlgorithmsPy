
def FastModularExponentiation1(b, k, m):

    b = b % m
    for i in range(1, k+1):
       b = b**2 % m
    return b

def FastModularExponentiation(b, e, m):
    a = bin(e)[2:]
    mod = 1
    for bi in range(len(a)):
        if int(a[bi]) != 0:
            k = len(a) - 1 - bi
            mod = mod * FastModularExponentiation1(b, k, m)
            #print(k)
            #print(a[bi])
            #print(FastModularExponentiation1(b, k, m))
    b = mod % m
    return b

print(FastModularExponentiation())