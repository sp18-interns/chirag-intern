class Student:
    def __init__(self,student_name,student_marks):
        """

        :param student_name:
        :param student_marks:
        """
        self.student_name= student_name
        self.student_marks = student_marks


    def __str__(self):
        """

        :return:
        """
        return f"The Name of the student is {self.student_name} and obtained  marks  :{self.student_marks}"









