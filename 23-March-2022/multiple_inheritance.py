class Freelancer:
    company = "Fiverr"
    level = 0

    def upgradeLevel(self):
        self.level = self.level + 1


class Employee:
    company = "Visa"
    eCode = 120


class Programmer(Employee, Freelancer):
    name = "Rohit"


p = Programmer()
p.upgradeLevel()
print(p.company)
f = Freelancer()
print(f.company)
