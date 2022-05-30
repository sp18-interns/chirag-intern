# import datetime
from experience import Experience

class Person(Experience):

    def __init__(self, name, start_date, end_date):
        '''

        :param name: Name of the person
        :param start_date: Joining date of the person in company
        :param end_date: last day of the person in company
        '''
        super().__init__(start_date, end_date)
        self.name = name
        self.list_of_experience = []
        self.total_experience_in_days = 0
        self.experience_count = {}  # {name_of_company : Days worked there}

    def __str__(self):
        '''

        :return: __str__ represents the class objects as string
        '''
        return f'The employee name is: {self.name} and the total company he worked in : {len(self.list_of_experience)}'

    def add_experience(self, Experience):
        '''

        :param Experience: Experience is added in the list of the person experience
        :return: returns list of experience
        '''
        self.list_of_experience.append(Experience)
        company_name = Experience.company_name
        no_of_days_stayed = (Experience.end_date - Experience.start_date).days
        if company_name in self.experience_count:
            self.experience_count[company_name] += no_of_days_stayed
        else:
            self.experience_count[company_name] = no_of_days_stayed

    def num_of_days(self):
        '''

        :return: number of days in datetime format
        '''
        return ((self.end_date - self.start_date).days)

    def num_of_months(self):
        '''

        :return:number of months
        '''
        return ((self.end_date - self.start_date).days)//30

    def num_of_years(self):
        '''

        :return: return number of year
        '''
        return ((self.end_date - self.start_date).days)//365

    def currently_in_which_company(self):
        '''

        :return: The person is currently in which company
        '''
        return self.list_of_experience[-1]

    def first_company(self):
        '''

        :return: The first company of the person
        '''
        for i in range(1, len(self.list_of_experience)):
            return self.total_company(i)

    def total_company(self, n):
        '''

        :param n: variable
        :return: how many company the person has
        '''
        if 0 <= n <= len(self.list_of_experience):
            return self.list_of_experience[n-1].company_name

    def which_company_he_worked_most(self):
        '''

        :return:return person experience days in which company he worked most
        '''
        companies = [[company, days] for company, days in self.experience_count.items()]

        companies = sorted(companies, key=lambda x:x[1], reverse=True)
        print(companies)
        return companies[0][0]


    def which_company_he_worked_least(self):
        '''

        :return: return person experience days which he worked least
        '''
        companies = [[company, days] for company, days in self.experience_count.items()]
        companies = sorted(companies, key=lambda x:x[1])
        return companies[0][0]




