def count_sheeps(sheep):
    sheepPresent = 0
    for c in sheep:
        if c == True:
            sheepPresent += 1
    return sheepPresent