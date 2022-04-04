def make_pi():
    pi = 22/7.0
    pi = str(pi)
    pi = list(pi)
    pi = pi[:1]+pi[2:4]
    pi = [int(x) for x in pi]
    return pi
