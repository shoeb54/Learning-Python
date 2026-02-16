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