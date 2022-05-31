"""

Max, min, middle value

Purpose: Read three values 
        Then print min, max and middle value

Method:
      Read three values
      Compute min, max, 
          middle (by subtracting min and max from sum)
      Print them

"""

first = input("First value => ")
print (first)

second = input("Second value => ")
print (second)

third = input("Third value => ")
print (third)

## now for the computation
first = int(first)
second = int(second)
third = int(third)

min_val = min(first,second,third)
print ("Min value is:", min_val)

max_val = max(first,second,third)
print ("Max value is:", max_val)

middle_val = (first+second+third)-min_val - max_val
print ("Middle value is:", middle_val)