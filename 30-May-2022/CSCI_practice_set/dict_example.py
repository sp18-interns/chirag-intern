

### Use this to create a new dictionary where keys are courses
### and values are students in those courses

def find_course_enrollment(students):
    courses = dict()
    for id, student in students.items():
        ## student is a dictionary
        student_name = student["NAME"] ## string
        student_courses = student["COURSES"] ### list of courses
        for course_name in student_courses:
            if course_name not in courses:
                courses[course_name] = [student_name]
            else:
                courses[course_name].append(student_name)
    return courses
    
    
s1 = { "NAME": "John Cleese", "COURSES": ["CSCI1100", "ENGR1100"], "GRADES": ["A", "B"]  }
s2 = { "NAME": "Michael Palin", "COURSES": ["CSCI2200", "BIOL2200", "CHEM1200"], "GRADES": ["A",
       "B", "A"]  }
s3 = { "NAME": "Eric Idle", "COURSES": ["CSCI1100", "BIOL2200", "CSCI4380"], "GRADES": ["C", "C"]  }
s4 = { "NAME": "Terry Gilliam", "COURSES": ["CSCI1100"], "GRADES": ["A"]  }
students = {"MP0001": s1, "MP0002": s2, "MP0003": s3, "MP0004": s4 }
    


courses_dict = find_course_enrollment(students)


for course, student_list in courses_dict.items():
    print (course + ": " + ", ".join(sorted(student_list)))

print()

### Find courses that only has Eric Idle in them

## Step 1: Find id of the student whose name is Eric Idle
### Instead: Find the dictionary for Eric Idle and courses for him

searched_student = None
for id in students:
    if students[id]["NAME"] == "Eric Idle":
        searched_student = students[id]  ### storing the student dictionary
        courses_for_student = set(students[id]["COURSES"])
        
for id in students:
    courses_taken = set(students[id]["COURSES"])
    if students[id]["NAME"] != 'Eric Idle':
        courses_for_student = courses_for_student - courses_taken
    
print (   courses_for_student ) 