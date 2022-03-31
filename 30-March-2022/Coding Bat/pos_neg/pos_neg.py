def pos_neg(a, b, negative):
    if a > 0 and b < 0 and negative == False:
        return True
    if a < 0 and b > 0 and negative == False:
        return True
    if a < 0 and b < 0 and negative == True:
        return True
    # if a<0 and b<0 and negative == False:
    #   return False
    else:
        return False
