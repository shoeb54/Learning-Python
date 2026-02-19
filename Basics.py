# =================================================================
# COMPREHENSIVE PYTHON TUTORIAL
# Covers Topics #1 to #74 (Tutorials Only)
# =================================================================

import math
import random
import datetime
import threading
import os

# ---------------------------------------------------------
# 1. BASICS: VARIABLES, INPUT, & TYPE CASTING (#1 - #4)
# ---------------------------------------------------------

# Printing and Strings
print("Hello World!") 

# Variables (Strings, Integers, Floats, Booleans)
name = "Bro"          # string
age = 21              # int
gpa = 3.4             # float
is_student = True     # boolean

# Type Casting (Converting types)
gpa = int(gpa)        # 3.4 becomes 3
age = str(age)        # 21 becomes "21"

# User Input (Always returns a string)
name = input("Enter your name: ")
age = int(input("Enter your age: "))

# ---------------------------------------------------------
# 2. MATH & ARITHMETIC (#6)
# ---------------------------------------------------------

friends = 5
friends += 1          # Addition (6)
friends **= 2         # Exponent (36)
remainder = friends % 5 # Modulus (1)

print(round(3.14))    # Rounding
print(abs(-5))        # Absolute value
print(pow(2, 3))      # Power
print(math.sqrt(64))  # Square root

# ---------------------------------------------------------
# 3. CONDITIONALS & LOGIC (#7, #11, #12, #38)
# ---------------------------------------------------------

# If Statements
if age >= 100:
    print("You are too old!")
elif age >= 18:
    print("You are signed up!")
else:
    print("Too young!")

# Logical Operators (and, or, not)
temp = 25
if temp > 0 and temp < 30:
    print("The weather is good")

# Conditional Expression (Ternary Operator)
# X if condition else Y
status = "Adult" if age >= 18 else "Child"

# Match-Case (Python 3.10+)
day = "Monday"
match day:
    case "Monday": print("Start of week")
    case "Friday": print("Weekend soon")
    case _: print("Invalid day")

# ---------------------------------------------------------
# 4. STRING MANIPULATION (#13 - #15)
# ---------------------------------------------------------

# String Methods
name = "Bro Code"
print(name.upper())     # BRO CODE
print(name.isdigit())   # False
print(name.replace("o", "a")) # Bra Cade

# Indexing [start:end:step]
phone_number = "123-456-7890"
area_code = phone_number[0:3]
last_digits = phone_number[-4:]

# Format Specifiers {value:flags}
price = 3.14159
print(f"Price is ${price:.2f}") # 3.14
print(f"Price is {price:10}")   # padding

# ---------------------------------------------------------
# 5. LOOPS (#16, #18, #20)
# ---------------------------------------------------------

# While Loop
while name == "":
    name = input("Enter name: ")

# For Loop (Iterating over a range or sequence)
for i in range(1, 11, 2): # start, stop, step
    print(i)

# Nested Loops
rows = 2
columns = 3
for i in range(rows):
    for j in range(columns):
        print("*", end="")
    print()

# ---------------------------------------------------------
# 6. COLLECTIONS (#21, #23, #25, #35, #37)
# ---------------------------------------------------------

# Lists (Ordered, changeable)
fruits = ["apple", "orange", "banana"]
fruits.append("pineapple")

# Sets (Unordered, unique)
colors = {"red", "green", "blue"}

# Tuples (Ordered, unchangeable)
coordinates = (10, 20)

# 2D Collections
grid = [[1, 2, 3], [4, 5, 6]]

# Dictionaries (Key:Value pairs)
capitals = {"USA": "Washington D.C.", "India": "New Delhi"}
print(capitals.get("USA"))

# List Comprehensions
doubles = [x * 2 for x in range(1, 6)] # [2, 4, 6, 8, 10]

# ---------------------------------------------------------
# 7. FUNCTIONS & SCOPE (#31 - #34, #40, #41)
# ---------------------------------------------------------

def hello(name, count=1): # Default argument
    global x # Global scope
    for _ in range(count):
        print(f"Hello {name}")

# *args (Tuple of arguments)
def add(*nums):
    return sum(nums)

# **kwargs (Dictionary of arguments)
def print_address(**kwargs):
    for value in kwargs.values():
        print(value)

# Scope Resolution (LEGB: Local, Enclosing, Global, Built-in)
# if __name__ == '__main__': (Ensures script runs only if executed directly)

# ---------------------------------------------------------
# 8. OBJECT ORIENTED PROGRAMMING (#46 - #57)
# ---------------------------------------------------------

class Animal:
    alive = True # Class variable

    def __init__(self, name):
        self.name = name # Instance variable

    def eat(self):
        print(f"{self.name} is eating")

class Dog(Animal): # Inheritance
    def speak(self):
        print("Woof!")

# super(), Static methods, and Class methods
class Employee:
    @staticmethod
    def is_workday(day): # No 'self' needed
        return day.weekday() < 5

# @property (Getters/Setters)
class Rectangle:
    def __init__(self, width):
        self._width = width
    @property
    def width(self):
        return self._width

# ---------------------------------------------------------
# 9. ADVANCED TOPICS (#58 - #65)
# ---------------------------------------------------------

# Exception Handling
try:
    number = int(input("Enter a number: "))
    print(1 / number)
except ZeroDivisionError:
    print("Can't divide by zero")
except Exception as e:
    print(e)

# File Handling
if os.path.exists("test.txt"):
    with open("test.txt", "r") as file:
        print(file.read())
else:
    with open("test.txt", "w") as file:
        file.write("Hello File!")

# Multithreading
def task():
    print("Task running")
x = threading.Thread(target=task)
x.start()

# ---------------------------------------------------------
# 10. GUI INTRO (PyQt5) (#66 - #74)
# ---------------------------------------------------------
# (Conceptual logic as PyQt5 requires installation)
# 1. Initialize QApplication
# 2. Create QWidget/QMainWindow
# 3. Add Labels, Buttons, Layouts (QVBoxLayout/QHBoxLayout)
# 4. Connect signals (clicks) to slots (functions)
# 5. Show window and execute app.exec_()