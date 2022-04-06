def sorta_sum(a, b):
    if a+b in range(10, 20):  # and b in range(10,20):
        return 20
    else:
        if 10 <= a+b < 20:
            return 20
        else:
            return a+b
