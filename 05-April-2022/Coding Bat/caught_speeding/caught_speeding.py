def caught_speeding(speed, is_birthday):
    if speed <= 60:
        return 0
    elif speed <= 65 and is_birthday == True:
        return 0
    elif 61 <= speed <= 80:
        return 1
    elif speed <= 85 and is_birthday == True:
        return 1
    elif speed <= 85 and is_birthday == False:
        return 2
    elif speed >= 81:
        return 2
