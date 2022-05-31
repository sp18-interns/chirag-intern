

## remove vowels

phrase = "antidisestablishmentarianism"
phrase = phrase.replace("a","")
phrase = phrase.replace("e","")
phrase = phrase.replace("o","")
phrase = phrase.replace("i","")
phrase = phrase.replace("u","")
print (phrase)


## repeat a as many times it appears in name

name = "amos eaton"
num = name.count("a")
val = "a"*num
name = name.replace("a",val)
print(name)

name = "abracadabra"

print (name.replace("a", "a"*(name.count("a"))))

## switch a and e

name = "Rensselaer Polytechnic Institute"
name = name.replace("a","#")
name = name.replace("e", "a")
name = name.replace("#", "e")
print (name)