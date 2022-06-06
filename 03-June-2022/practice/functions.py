import math


def area_circle(radius):
    area = math.pi*radius**2
    return area


def full_name(first, last):
    first = first.strip()
    first = first.capitalize()
    last = last.strip()
    last = last.capitalize()
    return (first + " " + last)


f = input("First => ")
l = input("Last => ")
fn = full_name(f, l)

print(fn)
