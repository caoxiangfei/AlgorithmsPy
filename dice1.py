import itertools as it

def count_wins(dice1, dice2):

    assert len(dice1) == 6 and len(dice2) == 6

    num_dice1_wins = 0
    num_dice2_wins = 0

    for d in it.product(dice1, dice2):
        if d[0] > d[1]:
            num_dice1_wins += 1
        elif d[0] < d[1]:
            num_dice2_wins += 1
    return (num_dice1_wins , num_dice2_wins )

def find_the_best_dice(dices):
    assert all(len(dice) == 6 for dice in dices)
    for i in range(len(dices)):
        temp = 0
        for dice1 in dices:
            if dice1 == dices[i]:
                continue
            if count_wins(dices[i], dice1)[0] > count_wins(dices[i], dice1)[1]:
                temp += 1
        if temp == len(dices) - 1:
            return i
    return -1


def compute_strategy(dices):
    assert all(len(dice) == 6 for dice in dices)

    strategy = dict()
    strategy["choose_first"] = True

    if find_the_best_dice(dices) != -1:
        return {"choose_first": True, "first_dice": find_the_best_dice(dices)}
    else:
        strategy["choose_first"] = False
        for i in range(len(dices)):
            for j in range(len(dices)):
                if dices[i] == dices[j]:
                    continue
                if count_wins(dices[i], dices[j])[0] <  count_wins(dices[i], dices[j])[1]:
                    strategy[i] = j
        return strategy

    # write your code here






dice1=[8, 8, 8, 8, 5, 6]
dice2=[1, 2, 3, 4, 4, 4]
dice3=[8, 7, 7, 4, 4, 4]
dices1 = [dice1, dice2, dice3]
dices =   [[1, 4, 5, 6, 9, 10], [2, 2, 3, 7, 11, 11], [3, 4, 4, 5, 6, 12]]
dice4 = [1, 2, 4, 5, 7, 8]
dice5 = [1, 2, 3, 6, 7, 10]
dice6 = [2, 3, 4, 5, 6, 8]

print(find_the_best_dice(dices))
print(compute_strategy(dices) )

