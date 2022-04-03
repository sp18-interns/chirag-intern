
def string_splosion(str):
    #n = len(str)
    # return str[0:n-(n-1)]+str[0:n-2]+str[0:n-1]+str[0:n]
    n = ''
    for i in range(len(str)):
        n = n + str[:i+1]
    return n
