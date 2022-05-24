import datetime

from experience import Experience
from person import Person

if __name__ == '__main__':
    start_date =datetime.datetime(2019, 4, 1)
    end_date =datetime.datetime(2020, 2, 1)
    exp1 = Experience(start_date,end_date, 'SP18','intern', False)


    start_date = datetime.datetime(2021, 1, 1)
    end_date = datetime.datetime(2022, 2, 2)
    exp2 = Experience(start_date, end_date, "Amazon", "SDE", False)

    start_date = datetime.datetime(2022, 2, 3)
    end_date = datetime.datetime(2022, 5, 23)
    exp3 = Experience(start_date, end_date, "Google", "Backend Engineer", True)



    chirag = Person("Chirag")
    # chirag.add_experience("Chirag")
    # TODO :- Why do use _ before the name of function or the attribute.---> A single leading underscore in front of a variable, a function, or a method name means that these objects are used internally
    chirag.add_experience(exp1)
    chirag.add_experience(exp2)
    chirag.add_experience(exp3)

    print(f"Chirag experience in days is {chirag.total_experience_in_days()}")

    print(f'Chirag experience in months is {chirag.total_experience_in_months()}')

    print(f'Chirag experience in years is {chirag.total_experience_in_years()}')

    print(exp1)
    print(exp2)
    print(exp3)
    print('*' * 100)
    print(f"Most worked company name is {chirag.which_company_he_worked_most()[1]} and working days is {chirag.which_company_he_worked_most()[0]} days ")
    print('*' * 100)
    print(f"Least worked company name is {chirag.which_company_he_worked_least()[1]} and working days is {chirag.which_company_he_worked_least()[0]} days ")
    print('*' * 100)
    print(f'Person is currently in {chirag.currently_in_which_company()} ')
    print('*' * 100)
    print(f'The first company of the person is :{chirag.first_company()}')
