def spin_around(lst):
    spins = 0
    for i in lst:
        if i == "right":
            spins = spins + 0.25
        elif i == "left":
            spins = spins - 0.25
    return abs(int(spins))