from experience import Experience
import datetime

from person import Person

if __name__ == '__main__':
    start_date = datetime.datetime(2021,3,2)
    end_date = datetime.datetime(2021,5,11)
    exp1 = Experience(start_date,end_date,"SP18",'Intern',False)
    print(exp1)

    start_date = datetime.datetime(2021, 5, 2)
    end_date = datetime.datetime(2022, 5, 11)
    exp2 = Experience(start_date, end_date, "Techno", "SD", False)
    print(exp2)

    chirag = Person("Chirag")
    chirag.add_experience("Chirag")
    chirag.add_experience(exp1)
    chirag.add_experience(exp2)

    # print(chirag.get_total_experience_in_years())
    # print(chirag.get_total_experience_in_months())
    # print(chirag.name)
    # start_date = datetime.datetime(2022,3,2)
    # end_date = datetime.datetime(2022,5,11)
    # exp = Experience(start_date,end_date,"SP-18","Intern",True)


    # exp = Experience(29,11,2000,29,11,2001,"Sp18",'PUNE',True)
    # print(exp)

    # print(f' The total experience in years : {chirag.get_total_experience_in_years()}')
    # print(f'{chirag.get_total_experience_in_months()}')
    # print(f'{chirag.get_total_experience_in_days()}')
    # print(f'{chirag.add_experience()}')


