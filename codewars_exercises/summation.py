def summation(num):
    sum = 0
    while num > 0:
        sum = num + sum
        num = num - 1
    return sum