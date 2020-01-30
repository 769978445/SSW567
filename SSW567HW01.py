"""SSW567P1
Xiangyu Wang"""

import unittest
import math

def classify_triangle(a, b, c):
    """Judge which kind of triangle is this input"""
    if not (a + b > c and a + c > b and b + c > a):    # The sum of any two lengths should be greater then the 3rd one
        return "Not a triangle"

    elif a == b:  # We only compare the first two elements because we sorted the tuple before we pass it in for classification
        if a == b == c:  # Check if it is a equilateral triangle
            return "Equilateral triangle"

        elif round((math.pow(a, 2) + math.pow(b, 2)), 4) == round(math.pow(c, 2), 4):  # Check if it is a right triangle
            return "Isosceles right triangle"

        else:
            return "Isosceles triangle"

    elif round(math.pow(a, 2) + math.pow(b, 2), 4) == round(math.pow(c, 2), 4):  # Check if it is a right triangle
        return "Right triangle"

    else:
        return "Scalene triangle"


def get_triangle():
    """ Get inputs for legnth and verify the validity of inputs(floats that are greater than 0),return them as sorted tuple"""

    a = input("Please enter a number for 1st side of triangle:")
    if float(a) <= 0:  # Check for validity
        raise ValueError("This is not a valid input!")  # Raise exceptions for invalid input

    else:
        b = input("Please enter a number for 2nd side of triangle:")
        if float(b) <= 0:
            raise ValueError("This is not a valid input!")

        else:
            c = input("Please enter a number for 3rd side of triangle:")
            if float(c) <= 0:
                raise ValueError("This is not a valid input!")

    return sorted((float(a), float(b), float(c)))  # Return three lengths as sorted tuple


def main():
    while True:
        try:
            (a, b, c) = get_triangle()
        except ValueError as err:
            print(err)
        else:
            False
            print(f"The numbers you entered is {classify_triangle(a, b, c)}")


class AutoTest(unittest.TestCase):

    def test_classify_triangle(self):
        """Auto test for classify_triangle(a, b, c)"""
        self.assertEqual(classify_triangle(1, 2, 3), "Not a triangle")
        self.assertEqual(classify_triangle(2, 3, 1), "Not a triangle")
        self.assertEqual(classify_triangle(0, 0, 0), "Not a triangle")
        self.assertEqual(classify_triangle(1, 1, 10), "Not a triangle")
        self.assertEqual(classify_triangle(1, 2, 2.5), "Scalene triangle")
        self.assertEqual(classify_triangle(3, 4, 5), "Right triangle")
        self.assertEqual(classify_triangle(10, 15, math.sqrt(325)), "Right triangle")
        self.assertEqual(classify_triangle(2.5, 3, math.sqrt(15.25)), "Right triangle")
        self.assertEqual(classify_triangle(2.5, 3, math.sqrt(15.25006)), "Scalene triangle")
        self.assertEqual(classify_triangle(2.5, 3, math.sqrt(15.24996)), "Right triangle")
        self.assertEqual(classify_triangle(math.sqrt(2), math.sqrt(2), 2), "Isosceles right triangle")
        self.assertEqual(classify_triangle(1, 1, math.sqrt(2)), "Isosceles right triangle")
        self.assertEqual(classify_triangle(1.001, 1.001, math.sqrt(2.004)), "Isosceles right triangle")
        self.assertEqual(classify_triangle(3, 3, 3), "Equilateral triangle")
        self.assertEqual(classify_triangle(3, 3, 5), "Isosceles triangle")


if __name__ == '__main__':
    main()
    unittest.main(exit=False, verbosity=2)