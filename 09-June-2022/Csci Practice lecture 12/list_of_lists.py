temp = [ [ 12.12, 13.25, 11.17, 10.4],
         [ 22.1, 29.3, 25.3, 20.2, 26.4, 24.3 ],
         [ 18.3, 17.9, 24.3, 27.2, 21.7, 22.2 ],
         [ 12.4, 12.5, 12.14, 14.4, 15.2 ] ]

## In general lists of lists operate very similar to the image
## each item in the list is a list
for i in range(len(temp)):
    item = temp[i]
    print (item)
    
## How about we access each item:
    
for i in range(len(temp)):
    for j in range(len(temp[i])):
        print (temp[i][j])

