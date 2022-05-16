def cat_dog(str):
    count_cat = 0
    count_dog = 0
    for i in range(len(str)):
        x = str[i:i+3]
        if x == "cat":
            count_cat += 1
        if x == "dog":
            count_dog += 1
    return (count_cat == count_dog)
