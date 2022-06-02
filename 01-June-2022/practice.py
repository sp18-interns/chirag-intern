import math

def circle(radius):
    return math.pi * radius**2

def cylinder(radius,height):
    circle_area = circle(radius)
    height_area = 2 * radius * math.pi * height
    return 2*circle_area + height_area

def sphere(radius):
    return 4 * math.pi * radius**2



print(circle(2))
print(cylinder(2,3))
print(sphere(4))


import math

def area_circle(radius):
    area = math.pi*radius**2
    return area

def full_name(first, last):
    first = first.strip()
    first = first.capitalize()
    last = last.strip()
    last = last.capitalize()
    return ( first + " " + last )

f = input("First => ")
l = input("Last => ")
fn = full_name(f, l)

print (fn)