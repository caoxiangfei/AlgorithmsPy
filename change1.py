def change(amount):
    if amount in (1, 2, 3, 4, 6, 8, 9, 11, 13, 16, 18, 23):
        return None
    else:
        if amount == 12:
            return [5, 7]
        if amount == 10:
            return [5, 5]
        if amount == 14:
            return [7, 7]
        if amount % 7 == 0:
            coins = change(amount - 7)
            coins.append(7)
            return coins
        else:
            coins = change(amount - 5)
            coins.append(5)
            return coins







print(change(88))