from experience import Experience
from person import Person


import datetime


def print_info(ob):
    print(f'The experience of the person in days is: {ob.num_of_days()}')
    print(f'The experience of the person in months is: {ob.num_of_months()}')
    print(f'The experience of the person in years is: {ob.num_of_years()}')
    return


if __name__ == '__main__':
    start_date = datetime.datetime(2019, 12, 1)
    end_date = datetime.datetime(2021, 12, 1)
    experience_object1 = Experience(start_date, end_date, 'Spark Eighteen', 'backendEngineer', False)
    chirag = Person('chirag', start_date, end_date)
    print(experience_object1)
    print_info(chirag)

    start_date = datetime.datetime(2020, 12, 2)
    end_date = datetime.datetime(2021, 12, 2)
    experience_object2 = Experience(start_date, end_date, 'Google', 'Python Developer', False)
    print(experience_object2)
    chirag = Person('chirag', start_date, end_date)
    # delta_days2 = (end_date - start_date).days
    print_info(chirag)

    start_date = datetime.datetime(2021, 12, 2)
    end_date = datetime.datetime(2022, 12, 12)
    experience_object3 = Experience(start_date, end_date, 'Amazon', 'Backend Engineer', True)
    chirag = Person('chirag', start_date, end_date)

    print(experience_object3)
    print_info(chirag)

    chirag.add_experience(experience_object1)

    chirag.add_experience(experience_object2)

    chirag.add_experience(experience_object3)

    print(f'The first company of the person is : {chirag.first_company()}')

    print(f'The person is currently in which company : {chirag.currently_in_which_company()} ')

    print(f'The company he worked at the least : {chirag.which_company_he_worked_least()}')
    print(f'The company he worked at the most : {chirag.which_company_he_worked_most()}')

