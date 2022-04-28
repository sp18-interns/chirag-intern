from datetime import date, timedelta


class Person:
    def __init__(self, first_name, last_name, date_of_birth):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.age = self.Calculate_Age()

    def __str__(self):
        return f" My name is {self.first_name} {self.last_name} and date of birth year is {self.date_of_birth} and age is {self.age}"

    def Calculate_Age(self):
        # timedelta(days=365.2425)
        age = (date.today().year - self.date_of_birth)
        return age


class Sort_Person():
    def __init__(self, person_list):
        # super().__init__(first_name,last_name,date_of_birth)
        self.person_list = person_list

    # def get_person_by_first_name(self, first_name):
    #     for person in self.person_list:
    #         if person.first_name == first_name:
    #             return person

    def __str__(self):
        for person in self.person_list:
            print(person)
        return ""

    def Sort_By_First_Name_Ascending(self):
        list_name = []
        sorted_person = []
        for person in self.person_list:
            list_name.append(person.first_name)
        list_name.sort()
        # Change
        #self.person_list = list_name

        # for first_name in list_name:
        #     # print(self.get_person_by_first_name(first_name))
        #     sorted_person.append(self.get_person_by_first_name(first_name))
        # self.person_list = sorted_person
        # return None

    def Sort_By_Last_Name_Ascending(self):
        return sorted(self.last_name)

    def Sort_By_First_Name_Descending(self):
        return sorted(self.first_name, reverse=True)

    def Sort_By_Last_Name_Descending(self):
        return sorted(self.last_name, reverse=True)

    def Sort_By_Age_Ascending(self):
        return sorted(Person.Calculate_Age())

    def Sort_By_Age_Descending(self):
        return sorted(Person.Calculate_Age(), reverse=True)


p1 = Person('yash', 'mishra', 1991)
p2 = Person('parag', 'gunjal', 1993)
p3 = Person('abrar', 'gunjal', 1996)
p4 = Person('mukesh', 'yadav', 1994)
p5 = Person('chirag', 'sahu', 1992)

person_list = []
person_list.append(p1)
person_list.append(p2)
person_list.append(p3)
person_list.append(p4)
person_list.append(p5)

sort_person = Sort_Person(person_list)
print("before sorting")
print(sort_person)
print("after sorting")
sort_person.Sort_By_First_Name_Ascending()
print(sort_person)
# sort_first_name = sorted(p, key=lambda p: p.first_name)
# print(sort_first_name)
# print(sorted(p,reverse=True))
