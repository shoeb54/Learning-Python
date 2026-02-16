"""
Basic Python Practice Program
Covers:
- Printing
- Data types
- Type casting
- User input
- Math operations
- Conditional statements
"""

# -----------------------------------
# 1. Printing Output
# -----------------------------------

print("Hello World!")
print("This is my first Python program!\n")


# -----------------------------------
# 2. Python Variables & Data Types
# -----------------------------------

# Integer
age_number = 10

# Float
height = 2.6

# String
character_name = "Hamza"

# Boolean
is_student = True

# Display variable types
print(type(age_number))
print(type(height))
print(type(character_name))
print(type(is_student))

# Using formatted strings (f-strings)
print(f"\nHello {character_name}, you are {age_number} years old!\n")


# -----------------------------------
# 3. Type Casting
# -----------------------------------

# Type casting means converting one data type into another
converted_int = int(height + 1)

print(type(converted_int))
print(height, "\n")


# -----------------------------------
# 4. User Input
# -----------------------------------

# Note: input() always returns a string
user_number = int(input("Enter a number: "))
print(f"The number is {user_number}\n")


# -----------------------------------
# 5. Math Operations
# -----------------------------------

# Arithmetic Operators:
# +  (Addition)
# -  (Subtraction)
# *  (Multiplication)
# /  (Division)
# %  (Modulus)
# ** (Exponent)

# Some useful math functions:
# round(), abs(), pow(), max(), min()

# Using the math module
import math


# -----------------------------------
# 6. Area of a Circle Calculator
# -----------------------------------

radius = float(input("Enter the radius of a circle: "))

area = math.pi * pow(radius, 2)

print(f"The area of the circle is {round(area, 2)} sq cm\n")


# -----------------------------------
# 7. Conditional Statement (if-else)
# -----------------------------------

user_age = int(input("Enter your age: "))

if user_age >= 18:
    print("You are eligible to sign up.")
else:
    print("You must be 18+ to sign up.")
