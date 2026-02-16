# This is my first program

print("Hello world!")
print("This is my first python program!")

# Python Variables (Integers, Floats, Strings, Booleans)

x = 10
y = 2.6
charName = 'Hamza'
charAge = True

print(type(x))
print(type(y))
print(type(charName))
print(type(charAge))

print(f"Hello {charName} You are {x} years old!")

#Typecasting means to covert one data type to another 

likeINt  = int(y+1)

print(type(likeINt))
print(y)

#User_input is always a string, for example:

isInput = int(input("Enter a number: "))
print(f"The number is {isInput}")

#Ex-01 Rectangle are calc

length = int(input("Enter the lenght: "))
width = int(input("Enter the width: "))
area = length * width
print(f"The area is {area} cm²")

#Ex02 Shopping Cart Pogram
print("-----------RUET Market------------")
item = input("What item would you like to buy? ")
price = float(input("What is the price of the item? "))
quantity = int(input("How many would you like? "))
total = price  * quantity

print(f"You have bought {quantity} x {item}\s.")
print(f"Your total price is {total} tk only. Thanks for coming.")

# Arithmatic Operators +,-,*,/,%,**
# friends = 0
# friend+-**/%
# print(friends)

#Some math related functions like round(),abs(),pow(),max()

# import math print(math.pi), math.e, math.sqrt(),math.ceil(),math.floor()

# Lets make a code to identify the area of a circle

import math
radius = float(input("Enter the radius of a circle: "))

area = math.pi * pow(radius,2)

print(f"The area of the circle is {round(area, 2)} sqrcm\n")

# Conditional Statement : if

age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to sign up.")

else :
    print("You have to 18+ to sign up!")    