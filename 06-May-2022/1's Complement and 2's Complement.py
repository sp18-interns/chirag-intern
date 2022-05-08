# Problem 1's complement and 2's complement :

n = 8


a = []
while (n > 0):
    digit = n % 2
    a.append(digit)
    n = n // 2
a.reverse()
print("The binary number of the given integer number is: ")

for i in a:
    print(i, end=" ")
print("\nThe 1's complement of the numbers is:")

for i in a:
    if i == 0:
        print('1', end=' ')
    elif i == 1:
        print('0', end=' ')

# for i in range(1):
#     if a[-i] == 1:
#         print('\n0', end = ' ')



# b = []
# while (Num > 0):
#     digit = Num % 2
#     b.append(digit)
#     Num = Num // 2
# b.reverse()
# for i in b:
#     print(i, end=" ")


