import math
import unittest

from hw_05_xywang import classify_triangle


class AutoTest(unittest.TestCase):
    """Test Case"""

    def test_classify_triangle(self):
        """Auto test for classify_triangle(a, b, c)"""
        self.assertEqual(classify_triangle(-1, 0, 2), 'InvalidInput', '-1, 0, 2 are invalid input')
        self.assertEqual(classify_triangle(200, 300, 250), 'InvalidInput', '200,300,250 are invalid input')
        self.assertEqual(classify_triangle(1, 2, 3), "Not a triangle")
        self.assertEqual(classify_triangle(2, 3, 1), "Not a triangle")
        self.assertEqual(classify_triangle(1, 1, 10), "Not a triangle")
        self.assertEqual(classify_triangle(1, 2, 2.5), "Scalene triangle")
        self.assertEqual(classify_triangle(3, 4, 5), "Right triangle")
        self.assertEqual(classify_triangle(10, 15, math.sqrt(325)), "Right triangle")
        self.assertEqual(classify_triangle(2.5, 3, math.sqrt(15.25)), "Right triangle")
        self.assertEqual(classify_triangle(2.5, 3, math.sqrt(15.25006)), "Scalene triangle")
        self.assertEqual(classify_triangle(2.5, 3, math.sqrt(15.24996)), "Right triangle")
        self.assertEqual(classify_triangle(math.sqrt(2), math.sqrt(2), 2),
                         "Isosceles right triangle")
        self.assertEqual(classify_triangle(1, 1, math.sqrt(2)), "Isosceles right triangle")
        self.assertEqual(classify_triangle(1.001, 1.001, math.sqrt(2.004)),
                         "Isosceles right triangle")
        self.assertEqual(classify_triangle(3, 3, 3), "Equilateral triangle")
        self.assertEqual(classify_triangle(3, 3, 5), "Isosceles triangle")


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
