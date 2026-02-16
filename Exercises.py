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