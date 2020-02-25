"""
Testing Program for SSW567_HW01
"""

import math


def classify_triangle(s_1, s_2, s_3):
    """require that the input values must >= 0 and <= 200"""
    if s_1 > 200 or s_2 > 200 or s_3 > 200:
        return 'InvalidInput'
    if s_1 <= 0 or s_2 <= 0 or s_3 <= 0:
        return 'InvalidInput'
    if not (s_1 + s_2 > s_3 and s_1 + s_3 > s_2 and s_2 + s_3 > s_1):
        return "Not a triangle"

    if s_1 == s_2:
        if s_1 == s_2 == s_3:  # Check if it is a equilateral triangle
            return "Equilateral triangle"
        # Check if it is a right triangle
        if round((math.pow(s_1, 2) + math.pow(s_2, 2)), 4) == round(math.pow(s_3, 2), 4):
            return "Isosceles right triangle"

        return "Isosceles triangle"
    # Check if it is a right triangle
    if round(math.pow(s_1, 2) + math.pow(s_2, 2), 4) == round(math.pow(s_3, 2), 4):
        return "Right triangle"

    return "Scalene triangle"
