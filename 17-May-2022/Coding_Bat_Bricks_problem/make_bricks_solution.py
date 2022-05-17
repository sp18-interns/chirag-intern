def make_bricks(small, big, goal):
    if (small + big*5) < goal:
        return False
    elif small < goal % 5:
        return False
    else:
        return True
