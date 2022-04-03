def front_back(a):
    if len(a) <= 1:
        return a

    my_data = a[1:-1]
    return a[-1] + my_data + a[0]
