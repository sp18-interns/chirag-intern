import datetime

# from person import Person

class Experience:
    def __init__(self, start_date = datetime.datetime.now(), end_date= datetime.datetime.now(), company_name = '', designation= '', is_present= True):
        self.start_date= start_date
        self.end_date = end_date
        self.company_name= company_name
        self.designation = designation
        self.is_present = is_present



    def __repr__(self):
        return str(self)

    def __str__(self):
        return f'The person experience he get from {self.company_name} is {(self.end_date-self.start_date).days} days and the role of the person is {self.designation}'

    def num_of_days(self):
        return (self.end_date - self.start_date)//30
