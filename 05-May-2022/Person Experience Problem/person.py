from datetime import date
from experience import Experience

class Person:
    def __init__(self,name:str = "Chirag"):
        self.name = name
        self._experience_list = list()
        self._total_experience_in_months = 0
        self._total_experience_in_years = 0
        self._total_experience_in_days = 0

    def __str__(self):
        return f'The person name is {self.name}  '

    # def add_experience(self,exp = Experience):
    #     exp.append
    def get_total_experience_in_years(self):
        return self._total_experience_in_days // 365

    def get_total_experience_in_months(self):
        return self._total_experience_in_days // 30
        # return f'The total experience of that employee in months is {(Experience.end_date.days - Experience.start_date.days) // 30}'

    def get_total_experience_in_days(self):
        return self._total_experience_in_days

    def add_experience(self, Experience = None ):
        return self._experience_list.append(Experience)

    def __calculate_experience_month(self,experience:Experience = None):
        return (experience.end_date - experience.start_date)//30

    def _calculate_experience_year(self, experience: Experience = None):
        return (experience.end_date - experience.start_date)//365

    def _calculate_experience_days(self, experience: Experience = None):
        return (experience.end_date - experience.start_date)

    def currently_in_which_company(self):
        for i in self._experience_list:
            if i.is_present:
                return i.company_name


    def first_company(self):
        return self._experience_list[0].company_name



