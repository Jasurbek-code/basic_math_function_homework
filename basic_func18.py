# Create a function called main.
# Create function arguments a.
# Assign the value pi to the variable "a" and return.
# Round the result to 2 decimal places.

# Example:
# Input: a = pi
# Output: 3.14
import math
from math import pi         # math kutubxonasidan faqat pi funksiyani o'zini chaqirdik

def main(a):
    return round(a, 2)      # pi ni yaxlitlab chiqaramiz

print(main(math.pi))        # pi qiymatini a argumentga berdik

