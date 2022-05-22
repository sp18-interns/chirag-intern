import datetime

# from experience import Experience


class Person:

    def __init__(self, name):
        self.name = name
        self._list_of_experience = []
        self._total_experience_in_months = 0
        self._total_experience_in_years = 0
        self._total_experience_in_days = 0

    def total_experience_in_years(self):
        return self._total_experience_in_days // 365

    def total_experience_in_months(self):
        return self._total_experience_in_days // 30

    def total_experience_in_days(self):
        return self._total_experience_in_days

    def add_experience(self , Experience):
        self._list_of_experience.append(Experience)
        if not Experience.is_present:
            self._total_experience_in_days = self._total_experience_in_days + self._calculate_experience_days(Experience)
        else:
            delta = datetime.datetime.now() - Experience.start_date
            self._total_experience_in_days = self._total_experience_in_days + delta.days

    def _calculate_experience_month(self, Experience):
        delta = Experience.end_date - Experience.start_date
        print(delta)
        return delta.days//30

    def _calculate_experience_year(self, Experience ):
        delta = Experience.end_date - Experience.start_date
        print(delta)
        return delta.days // 365

    def _calculate_experience_days(self, Experience):
        if Experience.is_present:
            delta = datetime.datetime.now() - Experience.start_date
        else:
            delta = Experience.end_date - Experience.start_date
        return delta.days

    def currently_in_which_company(self):
        for i in self._list_of_experience:
            if i.is_present:
                return i.company_name

    def first_company(self):
        return self._list_of_experience[0].company_name

    def which_company_he_worked_most(self):
        experience_per_company = dict()
        for i in self._list_of_experience:
            experience_per_company[i.company_name] = self._calculate_experience_days(i)
        max_company = max(experience_per_company.values(),experience_per_company.keys())
        return max_company

    def which_company_he_worked_least(self):
        pass

