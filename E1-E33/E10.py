## Arithmetic

import math as math

# Read input from user
a = int(input("Pick a whole number:"))
b = int(input("Pick another whole number:"))

# Compute and Display
print("The sum of a and b is: " + str(a+b))
print("The difference when b is subtracted from a is: " + str(b - a))
print("The product of a and b is: " + str(a * b))
print("The result of a divided by b is: " + str(a / b))
print("The remainder of a divided by b is: " + str(a % b))
print("The result of log10 of a is: " + str(math.log10(a)))
print("The result of a to the power of b is: " + str(math.pow(a, b)))

