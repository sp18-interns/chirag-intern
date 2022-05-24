# def closest_value(input_list, input_value):
#     difference = lambda input_list: abs(input_list - input_value)
#
#     res = min(input_list, key=difference)
#
#     return res
#
#
# if __name__ == "__main__":
#     list1 = [22, 12, 51, 23, 48, 16, 34, 61]
#
#     num = int(input("Enter the value: "))
#
#     val = closest_value(list1, num)
#
#     print("The closest value to the " + str(num) + " is", val)


def closest_value(input_list, input_value):
    input_list.sort(reverse=True)

    difference = lambda input_list: abs(input_list - input_value)

    res = min(input_list, key=difference)

    return res


if __name__ == "__main__":
    list1 = [29, 32, 14, 56, 97, 24, 46, 74]

    num = int(input("Enter the value: "))

    val = closest_value(list1, num)

    print("The closest value to the " + str(num) + " is", val)