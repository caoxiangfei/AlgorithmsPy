temp = 0
str1 = ''
for i in range(0, 10000):
    temp1 = 0
    temp3 = 0
    str1 = str(i)
    for a in str1:
        if a == '1':
            temp1 += 1
        if a == '3':
            temp3 += 1
    if temp1 == 1 and temp3 == 1:
       temp += 1
       print(i)



print(temp)