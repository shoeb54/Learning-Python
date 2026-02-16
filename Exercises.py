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


# Ex03 Build a calculator

operator = input("Select an operator: + - * / %: ")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

if operator == "+":
    print(num1 + num2)

elif operator == "-":
    print(num1 - num2)

elif operator == "*":
    print(num1 * num2)

elif operator == "/":
    print(num1 / num2)

elif operator == "%":
    print(num1 % num2)

else:
    print("Go liitle monkey, jump on the bed!")

# Python Weight Converter

def kg_to_pounds(kg):
    return kg * 2.20462

def pounds_to_kg(pounds):
    return pounds / 2.20462

print("Weight Conversion Program 🏋️")
print("1. Kilograms to Pounds")
print("2. Pounds to Kilograms")

choice = input("Enter choice (1 or 2): ")

if choice == "1":
    kg = float(input("Enter weight in kilograms: "))
    print(f"{kg} kg = {kg_to_pounds(kg):.2f} lbs")
elif choice == "2":
    pounds = float(input("Enter weight in pounds: "))
    print(f"{pounds} lbs = {pounds_to_kg(pounds):.2f} kg")
else:
    print("Invalid choice. Please enter 1 or 2.")


# Temperature mapping Code 

def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def celsius_to_kelvin(c):
    return c + 273.15

print("Temperature Conversion Program 🌡️")
print("1. Celsius to Fahrenheit")
print("2. Fahrenheit to Celsius")
print("3. Celsius to Kelvin")

choice = input("Enter choice (1, 2, or 3): ")

if choice == "1":
    c = float(input("Enter temperature in Celsius: "))
    print(f"{c}°C = {celsius_to_fahrenheit(c):.2f}°F")
elif choice == "2":
    f = float(input("Enter temperature in Fahrenheit: "))
    print(f"{f}°F = {fahrenheit_to_celsius(f):.2f}°C")
elif choice == "3":
    c = float(input("Enter temperature in Celsius: "))
    print(f"{c}°C = {celsius_to_kelvin(c):.2f} K")
else:
    print("Invalid choice. Please enter 1, 2, or 3.")
