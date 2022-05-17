class Fraction:
    def __init__(self, numerator, denominator=1):
        self.numerator = numerator
        self.denominator = denominator
        # if self.denominator < 0:
        #     self.numerator *= -1
        #     self.denominator *= -1
        self._reduce()

    def show(self):
        print(f'{self.numerator}/{self.denominator}')

    def multiply(self, other):
        f = Fraction(self.numerator * other.numerator, self.denominator * other.denominator)
        f._reduce()
        return f

    def add(self, other):
        f = Fraction(self.numerator * other.denominator + other.numerator * self.denominator, self.denominator * other.denominator)
        f._reduce()
        return f

    def _reduce(self):
        h = Fraction.hcf(self.numerator, self.denominator)
        if h == 0:
            return

        self.numerator //= h
        self.denominator //= h

    
    def hcf(x, y):
        x = abs(x)
        y = abs(y)
        smaller = y if x > y else x
        s = smaller
        while s > 0:
            if x % s == 0 and y % s == 0:
                break
            s -= 1
        return s


f1 = Fraction(6, 36)
f1.show()
f2 = Fraction(2, -12)
f2.show()
f3 = f1.multiply(f2)
f3.show()
f3 = f1.add(f2)
f3.show()
f3 = f1.add(5)
f3.show()
f3 = f1.multiply(5)
f3.show()