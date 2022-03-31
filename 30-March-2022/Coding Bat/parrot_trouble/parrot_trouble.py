def parrot_trouble(talking, hour):
    if talking == True and hour < 7:
        return True
    elif talking == True and hour > 20:
        return True
    else:
        return False
