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


    def set_name(self,student_name):
        """

        :param student_name:
        :return:
        """
        self.name = student_name
        assert type(student_name)==str , 'string object expected'


    def get_name(self,student_name):
        """

        :param student_name:
        :return:
        """
        return self.student_name

    def set_marks(self,student_marks):
        """

        :param student_marks:
        :return:
        """
        self.marks = student_marks
        assert type(student_marks)== float , 'Float object expected'


    def get_marks(self,student_marks):
        """

        :param student_marks:
        :return:
        """
        return self.student_marks












