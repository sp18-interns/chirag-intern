

animals = ["alpaca", "Walrus", "rooster", "Eagle", "reindeer", "whale", "Beaver"]

### first method
i = 0
while i < len(animals):
    animals[i] = animals[i].capitalize()
    print ( animals[i] )    
    i += 1
    
print (animals)

print ()
print ("For loop example over items ")
animals = ["alpaca", "Walrus", "rooster", "Eagle", "reindeer", "whale", "Beaver"]


for item in animals:
    item = item.capitalize()
    print (item)
    
print (animals)

print ()
print ("For loop example over indices")

for i in range(len(animals)):
    animals[i] = animals[i].capitalize()
    print (i, animals[i])
    
    