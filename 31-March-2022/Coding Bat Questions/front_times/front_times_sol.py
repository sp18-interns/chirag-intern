def front_times(str, n):
    len1 = 3
    if len(str) >= len1:
        return str[:len1]*n
    if n == 0 or str == '':
        return ''

    elif str[:n]:
        return str[:n]*n
