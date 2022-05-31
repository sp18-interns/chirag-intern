"""
Name printing program

Purpose: To take a name and print it in
different formats
"""

first = input("Enter firstname => ")
print (first)

last = input("Enter lastname => ")
print (last)


####

first = first.strip()
first = first.capitalize()

last = last.strip()
last = last.capitalize()

##print firstname lastname

name = first + " " + last

print ("Name:", name)

## print last, first

name = last + ", " + first

print ("Name: ", name, sep="")

## other

name =  " " + last

print ("Name: ", name)