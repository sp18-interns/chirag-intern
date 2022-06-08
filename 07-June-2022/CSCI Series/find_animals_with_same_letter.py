"""
Find and print the number and list of all
animal names in the list that start and end
with the same letter
"""

def find_ifsame(word):
    """Return true if word starts and
    ends with the same letter, and false
    otherwise. """
    
    word = word.lower()
    if len(word) == 0:
        return True
    elif word[0] == word[-1]:
        return True
    else:
        return False



####

animals = ["alpaca", "Walrus", "rooster", "Eagle", "reindeer", "whale", "Beaver"]

same_letter = []

for animal in animals:
    if find_ifsame(animal):
        same_letter.append(animal.capitalize())

print ("Animals with names that start and end with the same letter")
print (same_letter)
print ("{} such animals in the list".format(len(same_letter)))