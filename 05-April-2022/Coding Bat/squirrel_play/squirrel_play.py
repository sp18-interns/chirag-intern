def squirrel_play(temp, is_summer):
    if 60 <= temp <= 90 and is_summer == False:
        return True

    elif 60 <= temp <= 100 and is_summer == True:
        return True

    else:
        return False
