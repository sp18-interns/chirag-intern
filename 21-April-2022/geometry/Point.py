class Point:
    """
    Point class
    @todo : Rephrase the docstring
    """

    def __init__(self, x, y, label):
        """

        @param x:
        @param y:
        @param label:
        """
        self.x = x
        self.y = y
        self.label = label

    def __str__(self):
        return f"{self.label}: ({self.x}, {self.y})"
        # return f"The point is : {self.label}({self.x},{self.y})"

    def set_x(self, x):
        """

        @param x:
        @return:
        """
        self.x = x

    def get_x(self):
        """

        @return:
        """
        return self.x

    def set_y(self, y):
        """

        @param y:
        @return:
        """
        self.y = y

    def get_y(self):
        """

        @return:
        """
        return self.y

    def set_label(self, label):
        """

        @param label:
        @return:
        """
        self.label = label

    def get_label(self):
        """

        @return:
        """
        return self.label

    # TODO assertion datatype
    # TODO if x & y is 0 then point will not move

    def move(self, x=0, y=0):
        """

        @param x:
        @param y:
        @return:
        """
        self.x = self.x + x
        self.y = self.y + y
        print(f'Moving x Co-ordinate by {x} & y Co-ordinate by {y}')

    def check_quadrant(self):
        """

        @return:
        """
        if self.x > 0 and self.y > 0:
            print(f"{self} is at first quadrant")
        if self.x < 0 and self.y > 0:
            print(f"{self} is at Second quadrant")
        if self.x < 0 and self.y < 0:
            print(f"{self} is at Third quadrant")
        if self.x > 0 and self.y < 0:
            print(f"{self} is at fourth quadrant")
        if self.x == 0 and self.y == 0:
            print(f"{self} is at origin")
