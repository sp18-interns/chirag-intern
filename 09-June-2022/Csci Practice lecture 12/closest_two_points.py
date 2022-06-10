"""
Finding closest two points, requires we iterate over all
pairs of points and check the distance

If the distance is smaller than the current minimum,
assign it to the min value. Also keep track of the current
best pair using a tuple of indices

Note that to do this, we need to start with a min distance
value: which we can do by looking at the distance between
first two points (assumes there are at least two points in the
list)
"""

def distance(p1, p2):
    x1,y1 = p1
    x2,y2 = p2
    return ( (x1-x2)**2 + (y1-y2)**2)**0.5

points = [ (1,5), (13.5, 9), (10, 5), (8, 2), (16,3) ]

minval = distance( points[0], points[1] )
bestpair = 0,1
for i in range(len(points)):
    for j in range(len(points)):
        if i != j:
            d = distance ( points[i], points[j] )
            if d < minval:
                minval = d
                bestpair = i,j

print ("Closest two points", bestpair)
print ("Min distance", minval)