def string_match(a, b):
    count = 0
    for i in range(len(a)-1) and range(len(b)-1):
        # for j in range(len(b)-1):
        if a[i:i+2] == b[i:i+2]:
            #print(f"{a[i:i+2]} and {b[j:j+2]}")
            count += 1
    return count
