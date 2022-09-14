# Uses python3
import sys

def binary_search(a, x):
    left, right = 0, len(a)
    b =


    mid = int(left + (right-left)/2)
    if x == a[mid]:
        return mid
    elif x < a[mid] and right > 1:
        a = a[left:mid]
        return binary_search(a, x)
    elif x > a[mid] and right > 1:
       a = a[mid:]
       return binary_search(a, x)
    else:
        return -1






    # write your code here


#if __name__ == '__main__':
    #input = sys.stdin.read()
    #data = list(map(int, input.split()))
    #n = data[0]
    #m = data[n + 1]
    #a = data[1 : n + 1]
a = [1, 5, 8, 12, 13]
x = [8, 12, 23, 12, 11]
    #for x in data[n + 2:]:
for l in x:
        # replace with the call to binary_search when implemented
        print(binary_search(a, l), end = ' ')
