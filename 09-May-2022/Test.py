from person import Person
from experience import Experience


if __name__ == '__main__':
    chirag = Person('Chirag',21.6,'Pune','Male',365,12,1)
    print(chirag)
    # exp = Experience(29,11,2000,29,11,2001,"Sp18",'PUNE',True)
    # print(exp)

    print(chirag.get_total_experience_in_years())
    print(chirag.get_total_experience_in_months())
    print(chirag.get_total_experience_in_days())


