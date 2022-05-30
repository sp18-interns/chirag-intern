import datetime

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
        return f'Company Name is : {self.company_name}'

