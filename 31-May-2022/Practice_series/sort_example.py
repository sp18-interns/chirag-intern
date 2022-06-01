

"""
Sort example

"""

scores = [59, 61, 63, 45, 68, 64, 58]

print(scores)

scores.sort()

print(scores)
print("Min value is", scores[0])
print("Max value is", scores[-1])

midpoint = len(scores)//2
print("Middle value is", scores[midpoint])


x = [1, 4, 5]
print("Value of x when I start:", x)

val = input('Enter a value to add => ')

val = int(val)

print("Add this value to the list")
x.append(val)
print(x)

val = input('Enter a value to remove => ')
val = int(val)

if x.count(val) >= 1:
    x.remove(val)
else:
    print("Value not in the list to remove")
print(x)

val = input("Enter a value to insert => ")
val = int(val)

index = input("Which index to insert? => ")
index = int(index)

x.insert(index, val)
print("Value of x after:", x)

index = input("Enter an index to pop => ")
index = int(index)

if index < len(x) and index > 0:
    val = x.pop(index)
    print("Popped value is", val)
    print("Value of x after pop is", x)
else:
    print("This is not a valid index to pop")
    print("Popping the last value")
    val = x.pop()
    print("Popped value is", val)
    print("Value of x after pop is", x)
