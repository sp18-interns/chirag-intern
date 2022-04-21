# s1 = '"Hi mom", I said.  "How are you?"'
# s2 = '"Hi mom", I said.  '"How are you?"
# # s3 = '"Hi mom", I said.  '"How are you?"'
# s4 = """'Hi mom", I said.  '"How are you?"'"""
# # s5 = ""I want to be a lion tamer!"'
# s6 = "\"Is this a cheese shop?\"\n\t'Yes'\n\t\"We have all kinds!\""
# print(s2)


# s = "Cats\tare\n\tgood\tsources\n\t\tof\tinternet\tmemes"
# s
# print(s)


# print('\\'*4)
# print('\\\n'*3)
# print('Good-bye')


# print(len('George'))
# print(len(' Tom  '))
# s = """Hi
# sis!
# """
# print(len(s))


# x = input('Enter an integer ==> ')
# x = x*2
# x = int(x)
# x *= 2
# print("x is:", x)


# a = 97
# print('[%c]' % a)


# a = area_circle(1)
# print(a)
# print('A circle with radius 2 has area {:.2f}'.format(area_circle(2)))
# r = 75.1
# a = area_circle(r)
# print("A circle with radius {:.2f} has area {:.2f}".format(r, a))


import math


def area_circle(radius):
    return math.pi * radius ** 2


def area_cylinder(radius, height):
    circle_area = area_circle(radius)
    height_area = 2 * radius * math.pi * height
    return 2*circle_area + height_area


print('The area of a circle of radius 1 is', round(area_circle(1), 2))
r = 2
height = 10
print('The surface area of a cylinder with radius', r)
print('and height', height, 'is', round(area_cylinder(r, height), 2))
