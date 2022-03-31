def diff21(n):
    if n > 21:
        return (2*abs(n-21))
    elif n < 21:
        return abs(n-21)
    elif n == 21:
        return 0
