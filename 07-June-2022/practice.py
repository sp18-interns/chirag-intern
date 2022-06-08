name = 'Mosh'
message = f'Hi, my name is {name}'
print(message.upper()) # to convert to uppercase
print(message.lower()) # to convert to lowercase
print(message.title()) # to capitalize the first letter of every word
print(message.find('s'))
print(message.replace('M', 'q'))



i = 1
while i < 5:
    print(i)
    i += 1


def fun():
    print('fun')
print(fun())



# Exceptions
# Exceptions are errors that crash our programs. They often happen because of bad
# input or programming errors. It’s our job to anticipate and handle these exceptions
# to prevent our programs from cashing.
try:
    age = int(input('Age: '))
    income = 20000
    risk = income / age
    print(age)
except ValueError:
    print('Not a valid number')
except ZeroDivisionError:
    print('Age cannot be 0')




scores = [ 59, 61, 63, 63, 68, 64, 58 ]
new_scores = scores.sort()
scores=[58, 59, 61, 63, 63, 64, 68]
print(new_scores)