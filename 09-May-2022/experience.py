import datetime
# date_format = "%d/%m/%Y"

class Experience:

    def __init__(self,start_date = datetime.datetime.now(),end_date = datetime.datetime.now(),company_name= '', designation ='', is_present = False):
        self.start_date = start_date
        self.end_date = end_date
        self.company_name = company_name
        self.designation = designation
        self.is_present = is_present
        if self.is_present:
            self.end_date = None

    def __str__(self):
        return f'(The total experience at {self.company_name} is from {self.start_date} to {self.end_date} and the duration is {(self.end_date - self.start_date)} at the designation of {self.designation}'


# print(exp)
