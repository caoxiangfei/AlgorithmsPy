from random import randint#, seed
#from datetime import datetime

#seed(datetime.now())


def count_wins(dice1, dice2):
    num_rounds = 10 ** 5

    assert len(dice1) == 6 and len(dice2) == 6

    num_dice1_wins = 0
    num_dice2_wins = 0

    for _ in range(num_rounds):
        dice1_result = dice1[randint(0, 5)]
        dice2_result = dice2[randint(0, 5)]

        if dice1_result > dice2_result:
            num_dice1_wins += 1
        elif dice2_result > dice1_result:
            num_dice2_wins += 1
    return (num_dice1_wins , num_dice2_wins )

dice1=[1, 2, 5, 6, 7, 8]
dice2=[2, 2, 4, 5, 8, 9]

print(count_wins(dice1, dice2))