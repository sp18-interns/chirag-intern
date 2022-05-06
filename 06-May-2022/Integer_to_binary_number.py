# n = 8
# num = [1,2,4,8,16]

# Approch 1
# for i in range(0,n):
#     print( 2**i , end = '')
    # num = [].append(2**i)
    # print(num)
    # for j in range(0):
    #
    #     if 2**i + 2**j == n:
    #         print(num[i] = 1)

# Approch 2
# n = 3

# # for i in n:
# if remainder

n=8
a=[]
while(n>0):
    dig=n%2
    a.append(dig)
    n=n//2
a.reverse()

for i in a:
    print(i,end=" ")

