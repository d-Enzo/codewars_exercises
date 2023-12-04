def repeats(arr):
    sum_of_arr = 0
    for number in arr:
        ocurrences = arr.count(number)
        if ocurrences > 1:
            pass
        else:
            sum_of_arr = sum_of_arr + number
    return sum_of_arr