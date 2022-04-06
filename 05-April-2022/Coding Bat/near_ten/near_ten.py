def near_ten(num):
    a = num % 10
    if (10 - (10-a)) <= 2 or (10 - a) <= 2:
        return True
    else:
        return False
