# =================================================================
# PYTHON PROJECTS (SEQUENTIAL)
# =================================================================

# ⭐ Madlibs Game
# ---------------------------------------------------------
print("--- Madlibs Game ---")
adjective1 = input("Enter an adjective: ")
noun = input("Enter a noun: ")
adjective2 = input("Enter an adjective: ")
verb = input("Enter a verb: ")

print(f"Today I went to a {adjective1} zoo.")
print(f"In an exhibit, I saw a {noun}.")
print(f"{noun} was {adjective2} and {verb}ing.")


# ⭐ Compound Interest Calculator
# ---------------------------------------------------------
print("--- Compound Interest Calculator ---")
principle = float(input("Enter the principle amount: "))
rate = float(input("Enter the interest rate (in %): "))
time = int(input("Enter the time in years: "))

# Formula: A = P(1 + r/n)^nt (Simplified here for annual)
total_amount = principle * pow((1 + rate / 100), time)

print(f"Balance after {time} year/s: ${total_amount:.2f}")


# ⭐ Countdown Timer Program
# ---------------------------------------------------------
import time

print("--- Countdown Timer ---")
seconds = int(input("Enter the time in seconds: "))

for x in range(seconds, 0, -1):
    secs = x % 60
    mins = int(x / 60) % 60
    hours = int(x / 3600)
    print(f"{hours:02}:{mins:02}:{secs:02}")
    time.sleep(1)

print("TIME'S UP!")


# ⭐ Shopping Cart Program (Advanced)
# ---------------------------------------------------------
foods = []
prices = []
total = 0

while True:
    food = input("Enter a food to buy (q to quit): ")
    if food.lower() == "q":
        break
    else:
        price = float(input(f"Enter the price of {food}: "))
        foods.append(food)
        prices.append(price)

print("----- YOUR CART -----")
for food in foods:
    print(food, end=" ")

for price in prices:
    total += price

print(f"\nYour total is: ${total:.2f}")


# ⭐ Quiz Game
# ---------------------------------------------------------
questions = ("How many elements are in the periodic table?: ",
             "Which animal lays the largest eggs?: ",
             "What is the most abundant gas in Earth's atmosphere?: ")

options = (("A. 116", "B. 117", "C. 118", "D. 119"),
           ("A. Whale", "B. Crocodile", "C. Elephant", "D. Ostrich"),
           ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"))

answers = ("C", "D", "A")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("----------------------")
    print(question)
    for option in options[question_num]:
        print(option)

    guess = input("Enter (A, B, C, D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("INCORRECT!")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print(f"Your score is: {int(score / len(questions) * 100)}%")


# ⭐ Concession Stand Program
# ---------------------------------------------------------
menu = {"pizza": 3.00, "nachos": 4.50, "popcorn": 6.00, "soda": 2.00}
cart = []
total = 0

print("--------- MENU ---------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")

while True:
    food = input("Select an item (q to quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

for food in cart:
    total += menu.get(food)
    print(food, end=" ")

print(f"\nTotal is: ${total:.2f}")


# ⭐ Number Guessing Game
# ---------------------------------------------------------
import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num, highest_num)
guesses = 0
is_running = True

print("--- Python Number Guessing Game ---")

while is_running:
    guess = input(f"Enter a guess between {lowest_num}-{highest_num}: ")
    if guess.isdigit():
        guess = int(guess)
        guesses += 1
        if guess < answer:
            print("Too low! Try again")
        elif guess > answer:
            print("Too high! Try again")
        else:
            print(f"CORRECT! The answer was {answer}")
            print(f"Number of guesses: {guesses}")
            is_running = False
    else:
        print("Invalid guess")


# ⭐ Banking Program
# ---------------------------------------------------------
def show_balance(balance):
    print(f"Your balance is ${balance:.2f}")

def deposit():
    amount = float(input("Enter an amount to be deposited: "))
    return amount if amount > 0 else 0

def withdraw(balance):
    amount = float(input("Enter amount to be withdrawn: "))
    if amount > balance:
        print("Insufficient funds")
        return 0
    else:
        return amount

def main():
    balance = 0
    is_running = True
    while is_running:
        print("Banking Program")
        print("1.Show Balance\n2.Deposit\n3.Withdraw\n4.Exit")
        choice = input("Enter choice: ")
        if choice == '1': show_balance(balance)
        elif choice == '2': balance += deposit()
        elif choice == '3': balance -= withdraw(balance)
        elif choice == '4': is_running = False
    print("Have a nice day!")

if __name__ == '__main__':
    main()