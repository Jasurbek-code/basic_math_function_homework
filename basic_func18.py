# Create a function called main.
# Create function arguments a.
# Assign the value pi to the variable "a" and return.
# Round the result to 2 decimal places.

# Example:
# Input: a = pi
# Output: 3.14

from math import pi         # math kutubxonasidan faqat pi funksiyani o'zini chaqirdik

def main(a):
    a = a
    return round(a, 2)      # pi ni yaxlitlab chiqaramiz

print(main(pi))        # pi qiymatini a argumentga berdik

