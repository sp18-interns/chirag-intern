# iterators and generators HW
# Problem 1
# Create a generator that generates the squares of numbers up to some number N.
import random


def gen_square(N):
    for i in range(N):
        yield i**2


for i in gen_square(10):
    print(i)


# Problem 2
# Create a generator that yields "n" random numbers between a low and high number (that are inputs).
random.randint(1, 10)


def rand_num(low, high, n):
    for i in range(n):
        yield random.randint(low, high)


for num in rand_num(1, 10, 12):
    print(num)


# Problem 3
# Use the iter() function to convert the string below into an iterator:
s = "chirag"
s = iter(s)
print(next(s))

# problem 4
# Explain a use case for a generator using a yield statement where you would not want to use a normal function with a return statement.
my_list = [1, 2, 3, 4, 5]

gen_comp = (item for item in my_list if item > 3)

for item in gencomp:
    print(item)
