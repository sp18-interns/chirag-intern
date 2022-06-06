def split(n):
    ten = n // 10
    one = n % 10
    return (ten, one)
x = 83
ten,one = split(x)
print( x, "has tens digit", ten, "and ones digit", one )

print('*'*50)

def combine( digits ):
    return digits[0]*100 + digits[1]*10 + digits[2]
d = (5, 2, 7)
print(combine(d))

print('*'*50)
thistuple = ("apple", "banana", "cherry")
print(thistuple)

print('*'*50)
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

print('*'*50)
# Different types of tuples

# Empty tuple
my_tuple = ()
print(my_tuple)

# Tuple having integers
my_tuple = (1, 2, 3)
print(my_tuple)

# tuple with mixed datatypes
my_tuple = (1, "Hello", 3.4)
print(my_tuple)

# nested tuple
my_tuple = ("mouse", [8, 4, 6], (1, 2, 3))
print(my_tuple)