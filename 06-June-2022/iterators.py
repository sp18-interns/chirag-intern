# iterator:
# An iterator is an object that contains a countable number of values.
# Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().

nums = [7,12,9,5]

for i in nums:
    print(i)

print('--'*10)
it = iter(nums)
print(it.__next__())    # it will print the first value of the list which is 7
print(it.__next__())    # it will print the next of first value of the list which is 12



class Top_ten:

    def __init__(self):
        self.num =1

    def __iter__(self):
        return self

    def __next__(self):

        if self.num <=10:
            val = self.num
            self.num +=1
            return val
        else:
            raise StopIteration

values=Top_ten()

for i in values:
    print(i)
