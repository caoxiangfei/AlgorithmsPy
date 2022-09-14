count = 0
for i in range(10000):
    str1 = str(i)
    temp = 0
    for letter in str1:
        temp += int(letter)
    if temp == 10:
        count += 1

list1 = [1,2, 3, 4, 5]
list1.__delitem__()