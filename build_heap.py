# python3

def shiftdown(H, j, swap):
    minindex = j
    size = len(H)
    l = 2*j + 1
    r = 2*j + 2



    if l<size and H[l] < H[minindex]:
        minindex = l
    if r<size and H[r] < H[minindex]:
        minindex = r
    if j != minindex:
        swap.append([j, minindex])

        H[j], H[minindex] = H[minindex], H[j]
        return shiftdown(H, minindex, swap)
    else:
        return swap




def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    n = len(data)
    swap = []
    a = list(range(0, n // 2))
    a.reverse()
    for i in a:
        shiftdown(data, i, swap)

    return swap


def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n

    swaps = build_heap(data)

    print(len(swaps))
    #print(swaps)
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
