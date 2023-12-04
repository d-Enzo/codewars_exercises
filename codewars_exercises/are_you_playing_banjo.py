def are_you_playing_banjo(name):
    if name[0] == "R" or name[0] == "r":
        name = (name + " plays banjo")
        return name
    return name + " does not play banjo"