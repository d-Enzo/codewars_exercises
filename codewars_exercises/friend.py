def friend(names):
    friends = []
    for i in names:
        if len(i) == 4:
            friends.append(i)
    return friends