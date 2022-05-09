from person import Person
from experience import Experience


if __name__ == '__main__':
    chirag = Person('Chirag',21.6,'Pune','Male',365,12,1)
    # print(chirag)
    exp = Experience(datetime.date())

    print(chirag.get_total_experience_in_years())
    print(chirag.get_total_experience_in_months())
    print(chirag.get_total_experience_in_days())


