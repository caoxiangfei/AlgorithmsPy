def stableMatching(n, menPreferences, womenPreferences):
    # Do not change the function definition line.

    # Initially, all n men are unmarried
    unmarriedMen = list(range(n))
    # None of the men has a spouse yet, we denote this by the value None
    manSpouse = [None] * n
    # None of the women has a spouse yet, we denote this by the value None
    womanSpouse = [None] * n

    # While there exists at least one unmarried man:
    while unmarriedMen:
        he = unmarriedMen[0]
        she = menPreferences[he][0]
        menPreferences[he].pop(0)
        currentHusband = womanSpouse[she]
        if currentHusband != None:
            if womenPreferences[she].index(currentHusband) > womenPreferences[she].index(he):
                manSpouse[he], womanSpouse[she] = she, he
                manSpouse[currentHusband] = None
                unmarriedMen.remove(he)
                unmarriedMen.append(currentHusband)
        else:
            manSpouse[he], womanSpouse[she] = she, he
            unmarriedMen.remove(he)


    return manSpouse


assert (stableMatching(4, [[0, 1, 3, 2], [0, 2, 3, 1], [1, 0, 2, 3], [0, 3, 1, 2]],
                       [[3, 1, 2, 0], [3, 1, 0, 2], [0, 3, 1, 2], [1, 0, 3, 2]]) == [1, 2, 3, 0])