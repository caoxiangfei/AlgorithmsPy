# python3


def max_sliding_window_naive(Arr, w):
    n = len(Arr)
    k = n - w + 1  # window size = k
    leftA = [0] * n
    rightA = [0] * n
    result = [0] * k

    for i in range(n):
        if i % w == 0:
            leftA[i] = Arr[i]
        else:
            leftA[i] = max(Arr[i], leftA[i - 1])
    for i in range(n - 1, -1, -1):
        if i % w == (w - 1) or i == n - 1:
            rightA[i] = Arr[i]
        else:
            rightA[i] = max(Arr[i], rightA[i + 1])

    for i in range(k):
        result[i] = max(rightA[i], leftA[i + w - 1])

    return result

if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())
    for i in max_sliding_window_naive(input_sequence, window_size):
        print(i, end=' ')


#input_sequence = [2, 7, 3, 1, 5, 2, 6, 2]
#window_size = 4
#print(max_sliding_window_naive(input_sequence, window_size))

