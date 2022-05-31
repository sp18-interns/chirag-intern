"""

Topics:

Files
Set
Dictionary
Class

List
Aliasing, deep vs. shallow copy

"""

### file reading

##for line in open("imdb_data.txt"):
##    do_something

a = set()
a = set([])
a.add ('a')
a.add('b')
a.add('a')

## No order

## Set operations:

## Union: everything in two sets [OR]
### s1|s2 -> everything in s1 or in s2

### Intersection: things in common between two sets [AND]
## s1&s2 -> everything in s1 AND in s2

## Difference: (not)
## s1-s2 -> everything in s1 that is NOT in s2

## s1 ^ s2 = (s1-s2) | (s2-s1)

### All operations return a new set (shallow copy)

## Dictionary

## Keys: are sets
## Values: can be anything (list)

d = dict()
d = {}


d[1] = ['a','b']
d[2] = ['c', 'd']

### If a value is stored in a 
## list, set, or dictionary

L = [1,2,3,4]

3 in L

3 not in L

SL = set(L)

3 in SL   ### more efficient than lists

d = dict()
d = {}


d[1] = ['a','b']
d[2] = ['c', 'd']

## check if the value is in the key of values

1 in d  ## set operation: check if 1 is a key in d


## check if 'a' is stored in the values

val = 'a'
is_found = False
found_key = None
for key in d.keys():
    if val in d[key]:
        is_found = True
        found_key = key
        break
    
is_found = False
for val_list in d.values():
    if val in val_list:
        is_found = True
        break
    
is_found = False
for key,val_list in d.items():
    if val in val_list:
        is_found = True
        found_key = key
        break
    
