# python3


def max_pairwise_product(numbers):
    n = len(numbers)
    index1 = 0
    index2 = 0
    for first in range(1,n-1):
        if numbers[first] > numbers[index1]:
            index1=first
    if index1==0:
        index2 = 1
    else:
        index2 = 0

    for second in range(n):
        if second != index1 and numbers[second] > numbers[index2]:
            index2 = second

    return numbers[index1]*numbers[index2]


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
