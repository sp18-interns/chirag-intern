# from experience import Experience
# from person import Person


import datetime

if __name__ == '__main__':
    start_date = datetime.datetime(2020,12,1)
    end_date = datetime.datetime(2021,12,1)
    experience_object = Experience(start_date,end_date,'Spark Eighteen','backendEngineer', True)
    print(experience_object)
    chirag = Person('chirag')
    