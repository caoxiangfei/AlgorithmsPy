# Uses python3
import sys

def get_majority_element(a, left, right):


    #write your code here

    count1 = 0
    count2 = 0
    index = 0
    if right == 1:
        return 1
    for i in range(right):
        if a[index] != a[i]:
            count1 = count1 - 1
        else:
            count1 += 1
        if count1 == 0:
            index = i
            count1 = 1
    for j in range(right):
        if a[index] == a[j]:
            count2 += 1
    if count2 > right/2:
        return 1
    return -1




if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)





