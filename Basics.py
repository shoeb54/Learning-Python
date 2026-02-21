# ============================================================
# COMPREHENSIVE PYTHON MASTER SCRIPT
# ============================================================

import math
import random
import datetime
import threading
import os


# ============================================================
# 1️⃣ BASICS: VARIABLES, INPUT, TYPE CASTING
# ============================================================

print("Hello World!")

# Primitive Data Types
name = "Bro"          # str
age = 21              # int
gpa = 3.4             # float
is_student = True     # bool

# Type Casting
gpa = int(gpa)        # 3
age = str(age)        # "21"

# User Input (always string)
# name = input("Enter your name: ")
# age = int(input("Enter your age: "))


# ============================================================
# 2️⃣ MATH & ARITHMETIC
# ============================================================

friends = 5
friends += 1          # 6
friends **= 2         # 36
remainder = friends % 5

print(round(3.14159))
print(abs(-5))
print(pow(2, 3))
print(math.sqrt(64))
print(math.factorial(5))
print(math.log(10))


# ============================================================
# 3️⃣ CONDITIONALS & LOGIC
# ============================================================

age = 20

if age >= 100:
    print("Too old!")
elif age >= 18:
    print("Adult")
else:
    print("Minor")

temp = 25
if 0 < temp < 30:
    print("Weather is good")

status = "Adult" if age >= 18 else "Child"

day = "Monday"
match day:
    case "Monday":
        print("Start of week")
    case "Friday":
        print("Weekend soon")
    case _:
        print("Invalid day")


# ============================================================
# 4️⃣ STRING MANIPULATION
# ============================================================

name = "Bro Code"
print(name.upper())
print(name.replace("o", "a"))
print(name.isdigit())

phone = "123-456-7890"
area_code = phone[:3]
last_digits = phone[-4:]

price = 3.14159
print(f"Price: ${price:.2f}")


# ============================================================
# 5️⃣ LOOPS
# ============================================================

for i in range(1, 11, 2):
    print(i)

rows, cols = 2, 3
for i in range(rows):
    for j in range(cols):
        print("*", end="")
    print()

count = 0
while count < 3:
    print("Count:", count)
    count += 1


# ============================================================
# 6️⃣ COLLECTIONS
# ============================================================

# List
fruits = ["apple", "orange", "banana"]
fruits.append("pineapple")

# Set
colors = {"red", "green", "blue"}

# Tuple
coordinates = (10, 20)

# Dictionary
capitals = {"USA": "Washington D.C.", "India": "New Delhi"}
print(capitals.get("USA"))

# 2D List
grid = [[1, 2, 3], [4, 5, 6]]

# List Comprehension
doubles = [x * 2 for x in range(1, 6)]
even_squares = [x**2 for x in range(10) if x % 2 == 0]


# ============================================================
# 7️⃣ FUNCTIONS & ADVANCED FUNCTION FEATURES
# ============================================================

def hello(name, count=1):
    for _ in range(count):
        print(f"Hello {name}")

def add(*nums):  # *args
    return sum(nums)

def print_address(**kwargs):  # **kwargs
    for key, value in kwargs.items():
        print(f"{key}: {value}")

# Lambda
square = lambda x: x**2
print(square(5))

# map, filter
nums = [1, 2, 3, 4, 5]
print(list(map(lambda x: x * 2, nums)))
print(list(filter(lambda x: x % 2 == 0, nums)))

# Scope Example (LEGB)
x = 10
def scope_test():
    x = 5  # local
    print("Local x:", x)

scope_test()
print("Global x:", x)


# ============================================================
# 8️⃣ OBJECT ORIENTED PROGRAMMING
# ============================================================

class Animal:
    alive = True  # class variable

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

class Dog(Animal):
    def speak(self):
        print("Woof!")

dog = Dog("Buddy")
dog.eat()
dog.speak()

# Static Method
class Employee:
    @staticmethod
    def is_workday(day):
        return day.weekday() < 5

today = datetime.datetime.now()
print("Is workday:", Employee.is_workday(today))

# Property Decorator
class Rectangle:
    def __init__(self, width):
        self._width = width

    @property
    def width(self):
        return self._width

rect = Rectangle(10)
print("Rectangle width:", rect.width)


# ============================================================
# 9️⃣ EXCEPTION HANDLING
# ============================================================

try:
    number = 5  # change to 0 to test
    print(1 / number)
except ZeroDivisionError:
    print("Cannot divide by zero")
except Exception as e:
    print("Error:", e)
finally:
    print("Execution completed")


# ============================================================
# 🔟 FILE HANDLING
# ============================================================

filename = "test.txt"

if os.path.exists(filename):
    with open(filename, "r") as file:
        print(file.read())
else:
    with open(filename, "w") as file:
        file.write("Hello File!")

# ============================================================
# 1️⃣1️⃣ MULTITHREADING
# ============================================================

def task():
    print("Task running")

thread = threading.Thread(target=task)
thread.start()
thread.join()  # Wait for thread to finish


# ============================================================
# 1️⃣2️⃣ RANDOM & DATETIME
# ============================================================

print("Random number:", random.randint(1, 10))
print("Current time:", datetime.datetime.now())


# ============================================================
# 1️⃣3️⃣ ENTRY POINT (BEST PRACTICE)
# ============================================================

if __name__ == "__main__":
    print("Script executed directly.")