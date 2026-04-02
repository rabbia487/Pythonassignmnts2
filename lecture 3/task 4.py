import random


secret_number = random.randint(1, 10)

print("Welcome to the Number Guessing Game!")

print("I have picked a number between 1 and 10. Try to guess it!")


while True:

    user_guess = int(input("Enter your guess between 1 to 10: "))

    if user_guess < secret_number:
        print("Too low!")
    elif user_guess > secret_number:
        print("Too high!")
    else:
        print("Correct! You guessed the number!")