# Uses python3
import sys

def get_fibonacci_last_digit_naive(n):
    F = [0, 1]
    if n > 1:
        for i in range(2, n + 1):
            F.append((F[i - 1] + F[i - 2])%10)
    return F[n]%10


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(get_fibonacci_last_digit_naive(n))
