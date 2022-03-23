class Programmer:

    def __init__(self, company, name, age, salary, position):
        self.company = company
        self.name = name
        self.age = age
        self.salary = salary
        self.position = position
        print("Programmer is hired!")

    def getdetails(self):
        print(f'The name of the company is {self.company}')
        print(f'The name of the Programmer is {self.name}')
        print(f'The age of the Programmer is {self.age}')
        print(f'The salary of the Programmer is {self.salary}')
        print(f'The position of the Programmer is {self.position}')


obj = Programmer('SparkEighteen', 'Chirag', '21', '500', 'SD Role')
obj.getdetails()
