from experience import Experience
from person import Person


import datetime

if __name__ == '__main__':
    start_date = datetime.datetime(2019,12,1)
    end_date = datetime.datetime(2020,12,1)
    experience_object1 = Experience(start_date,end_date,'Spark Eighteen','backendEngineer', True)
    # print(experience_object1)

    start_date = datetime.datetime(2020,12,2)
    end_date = datetime.datetime(2021,12,1)
    experience_object2 = Experience(start_date,end_date,'Google','Python Developer', True)
    # print(experience_object2)

    start_date = datetime.datetime(2021,12,2)
    end_date = datetime.datetime(2022,12,1)
    experience_object3 = Experience(start_date,end_date,'Amazon','Backend Engineer', True)
    # print(experience_object3)



    chirag = Person('chirag')

    chirag.add_experience(experience_object1)

    # chirag.add_experience(experience_object2)
    #
    # chirag.add_experience(experience_object3)

    print(chirag.num_of_days())



    print(chirag)
    # print(chirag.get_total_experience_in_days())
    # list1 = [1,2,3]
    # list_experience = [experience_object1,experience_object2]
    # print(list_experience)
    # list_of_experience = []
    # list_of_experience.append(experience_object2)
    # print(list_of_experience)
    # list_of_experience.append(experience_object1)

    # print(list_of_experience)
