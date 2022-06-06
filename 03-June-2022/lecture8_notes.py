"""

Tuples: allows you to pack values

It allows accessing individual values
but does not allow changing of values

x = (1,2)
print (x[0], x[1])

used predominantly for packing and unpacking
values, returning multiple values from functions

x = (1,2)   ## pack two values, x is a tuple
a,b = x     ## unpack the two values in x to two variables, a and b

consider two ways to import and use
modules:

import math

print (math.pi)

from math import pi
(or from math import *)

print (pi)

## be careful with this second method,
## names of functions from different modules
## may clash, use rarely

from PIL import Image

Image functions:

functions for input output:

.open()    ## returns an image object
.save()    ## saves an image object to a file
.show()    ## shows image on screen
.new()     ## create a new image

image object attributes

.size, .format, .mode

functions for image processing, do not 
modify the image but return a new image

.crop()
.resize()
.convert()

functions for image processing that modify
the input image and not return anything

.paste()

Be careful, many Image function inputs are
tuples

"""

def tens_ones(x):
    tens = x//10
    ones = x%10
    return tens, ones

def swap(x,y):
    return y,x

x = 4
y = 7

print ("x: {}, y: {}".format(x,y))

###x,y = swap(x,y)
x,y = y,x  ## also swaps values (called multiple assignment)
print ("After swapping")
print ("x: {}, y: {}".format(x,y))

### Run and get a tuple value

vals = tens_ones(82)
print ("Result is", vals)
print ("Results is: tens: {}, ones: {}".format(vals[0], vals[1]))

## Run function and unpack values at the 
## same time

t,o = tens_ones(65)
print ("Results is: tens: {}, ones: {}".format(t,o))
