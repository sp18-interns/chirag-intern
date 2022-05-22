# Problem 1's complement and 2's complement :

n = 9


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


# for 2's Complement :

# for i in a:
# if a[0]==1:
#     print('\n8')
# if a[1]==1:
#     print('\n4')
# if a[2]==1:
#     print('\n2')
# if a[3]==1:
#     print('\n1')




