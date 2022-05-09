from datetime import date
from experience import Experience

list_of_experience = []
class Person():
    def __init__(self, name='',age = 0.0,address= '',gender = '',total_experience_in_days=0,total_experience_in_months = 0.0,total_experience_in_years=0.0):
        self.name = name
        self.age = age
        self.address = address
        self.gender = gender
        self.list_of_experience = []
        self.total_experience_in_days = total_experience_in_days
        self.total_experience_in_months = total_experience_in_months
        self.total_experience_in_years = total_experience_in_years


    def __str__(self):
        return f'The person name is {self.name}  the age is {self.age} and the gender is {self.gender}, lives in {self.address} '


    # def add_experience(self,exp = Experience):
    #     exp.append
    def get_total_experience_in_years(self):
        return self.total_experience_in_days // 365

    def get_total_experience_in_months(self):
        return self.total_experience_in_days // 30
        # return f'The total experience of that employee in months is {(Experience.end_date.days - Experience.start_date.days) // 30}'

    def get_total_experience_in_days(self):
        return self.total_experience_in_days

    def add_experience(self,experience= Experience):
        return self.list_of_experience.append(experience)



    def currently_in_which_company(self):
        return self.list_of_experience[-1]


    def first_company(self):
        return self.list_of_experience[0]


    def which_company_he_worked_most(self):
        pass
        # for i in self.list_of_experience:




    def which_company_he_worked_least(self):
        pass
    def how_much_gap_between_company(self):
        pass
    def how_many_company_has_person_worked(self):
        pass





# if __name__ == '__main__':
#     chirag = Person('Chirag',21.6,'Pune','Male',['SP18','Tudip'],365,12,1)
#     print(chirag)

# chirag = Person('Chirag')

# exp = Experience(datetime.date(2021,10,1), datetime.date(2022,3,11), 'SP18', 'Intern', False)
# chirag.get_total_experience_in_months()
