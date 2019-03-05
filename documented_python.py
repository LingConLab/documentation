"""This module multiplies 4 and 5

It is created as an example for documented code and is not intended to be used for anythong else.
Variables:
    a: int
        a is 4
    b: int
        b is 5
"""

a = 4
b = 5

class Multiplication(object):
    """This class is here to multiply numbers

    Attributes:
        a: int
            The first number.
        b: int, default 1
            The second number.
    """
    def __init__(self, a, b=1):
        """Takes two numbers and sets a to the first number and b to the second

        Parameters:
            a: int
                The first number.
            b: int, default 1
                The second number.
        """
        self.a = a
        self.b = b

    def multiply(self):
        """Multiplies the attributes a and b

        Returns int
            The result of multiplication.
        """
        return a * b

if __name__ == '__main__':
    print(Multiplication(a, b).multiply())
        
