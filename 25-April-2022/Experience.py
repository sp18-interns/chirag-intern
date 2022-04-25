import datetime


class Experience:
    def __init__(self,start_date,end_date ,company_name='',designation='',is_present= True):
        self.start_date = start_date
        self.end_date = end_date
        self.company_name = company_name
        self.designation = designation
        self.is_present = is_present


    def __str__(self):
        if self.is_present == False:
        # date = self.end_date - self.start_date
            return f'The total experience at {self.company_name} is from {self.start_date} to {self.end_date} which is {(self.end_date - self.start_date)} at the designation of {self.designation}' #year,{(self.end_date - self.start_date)} months,{(self.end_date.day - self.start_date.day)} days '

exp = Experience(datetime.datetime(2021,10,1),datetime.datetime(2022,3,11),'SP18','Intern',False)
print(exp)

