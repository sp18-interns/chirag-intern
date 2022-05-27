# import datetime
from experience import Experience

class Person(Experience):

    def __init__(self, name):
        super().__init__()
        self.name = name
        self.list_of_experience= []
        self.total_experience_in_days = 0

    def __str__(self):
        return f'{self.name} and the list of experience of that person is {self.list_of_experience}'

    def num_of_days(self):
        return (self.end_date - self.start_date).days
        # return self.total_experience_in_days//30


    # def get_total_experience_in_days(self):
    #     return self.total_experience_in_days
    #
    # def get_total_experience_in_months(self):
    #     return self.total_experience_in_days//30
    #
    # def get_total_experience_in_years(self):
    #     return self.total_experience_in_days//365
    #
    #
    def add_experience(self,Experience):
        self.list_of_experience.append(Experience)


    def currently_in_which_company(self):
        pass


