# def apple():
#     print('I am Apples!')
#
# tangerine = "Living reflection of a dream"
#
#
#
#
# class MyStuff(object):
#     def __init__(self):
#         self.tangerine = "And now a thousands years between"
#     def apple(self):
#         print('I am Classy Apples!')


# class Song:
#     def __init__(self,lyrics):
#         self.lyrics = lyrics
#
#     def sing_me_a_song(self):
#         for line in self.lyrics:
#             print(line)
#
# happy_bday = Song(["Happy birthday to you",
#                     "I don't want to get sued",
#                     "So I'll stop right there"])
#
# bulls_on_parade = Song(["They rally around the family",
#                         "With pockets full of shells"])
#
# Jingle_Bell_Song = Song(["jingle bells, jingle bells",
#                          "Jingle all the way",
#                          "Oh, what fun it is to ride",
#                          "In a one horse open sleigh",
#                          "Jingle bells, jingle bells",
#                          "Jingle all the way"])
#
#
# happy_bday.sing_me_a_song()
#
# bulls_on_parade.sing_me_a_song()
#
# Jingle_Bell_Song.sing_me_a_song()









## Animal is- a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## ?? Inherit Dog class from Animal
class Dog(Animal):
    def __init__(self, name):
        ## ?? Instantiate name
        self.name = name

## ??Inherit Cat class from Animal
class Cat(Animal):
    def __init__(self, name):
        ## ?? Instantiate name
        self.name = name

## ?? Making an object named as Person
class Person(object):
    def __init__(self, name):
    ## ??
        self.name = name
## Person has- a pet of some kind
        self.pet = None
## ??Employee is inherinting from Person
class Employee(Person):
    def __init__(self, name, salary):
## ?? hmm what is this strange magic?
        super(Employee, self).__init__(name)
## ??
        self.salary = salary

class Fish(object):
    pass
class Salmon(Fish):
    pass
class Halibut(Fish):
    pass
rover = Dog("Rover")
satan = Cat("Satan")
mary = Person("Mary")
mary.pet = satan
frank = Employee("Frank", 120000)

## ??
frank.pet = rover
## ??
flipper = Fish()



## ??
crouse = Salmon()
## ??
harry = Halibut()
