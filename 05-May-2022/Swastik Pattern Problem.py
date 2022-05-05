


n = 11
for i in range(0,n):
    for j in range(0,n):
        if j == n//2 or i ==n//2 or (i>n//2 and j ==n-1) or ( i == n-1 and j <=n//2) or ( i<n//2 and j==0) or (i ==0 and j >n//2) or (( i == ((n//2 + (n//2)//2)+1) and ( j == ((n//2 + (n//2)//2))+1) ) or ((i ==((n//2) + (n//2)//2+1)) and j ==((((n//2)//2)//2 )+1) or (i == n%10+1 and j == n%10+1)) or (i==(n//2)//2 and j ==(n//2)+3) ):
            print(" * ", end = '')
        else:
            print('   ',end= '')
    print("")




