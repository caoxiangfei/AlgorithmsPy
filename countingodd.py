count = 0
for i in range(1000000):
    temp_odd = 0
    temp_str = str(i)
    for index in range(len(temp_str)):
        if int(temp_str[index]) % 2 == 1:
            temp_odd += 1
    if temp_odd == 3:
        count += 1


print(count)


