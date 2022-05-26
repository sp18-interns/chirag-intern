from datetime import date
from experience import Experience

class Person:

    def __init__(self, name = '' ):
        self.name = name
        self.list_of_experience= []
        self.total_experience_in_days = 0

    def num_of_days(self, start_date, end_date):
        return (self.end_date - self.start_date).days

    def get_total_experience_in_months(self):
        return ((self.end_date - self.start_date).days)//30

    def get_total_experience_in_years(self):
        return ((self.end_date - self.start_date).days)//365

    # def get_total_experience_in_months(self):
    #     return ((self.start_date - self.end_date).days)//30

    def currently_in_which_company(self):
        pass


