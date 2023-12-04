def min_max(lst):
    lst.sort()
    output = []
    output.append(lst[0])
    output.append(lst[-1])
    return output