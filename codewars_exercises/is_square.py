import math
def is_square(n):
    if n < 0:
        return False
    if n == 0:
        return True
    
    sqrt_num = math.sqrt(n)

    if sqrt_num.is_integer():
        return True
    else:
        return False