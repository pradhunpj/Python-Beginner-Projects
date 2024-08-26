import random
print("Welcome to Number Guessing Game :)\n")

top_range = input("Type a number: ")

if top_range.isdigit():
    top_range = int(top_range)
    if top_range <=0:
        print("Invalid input! Number must be greater than 0.")
        exit
else:
    print("Invalid input! Number must be a digit.")
    exit

number = random.randint(0,top_range)
guesses = 0
print(f"Make a guess from 0 to {top_range}\n")
while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
        
        if user_guess == number:
            print(f"Congratulations! You guessed the number correctly in {guesses} attempts.")
            break
        elif user_guess < number:
            print("Too low! Try again.\n")
        else:
            print("Too high! Try again.\n")
    else:
        print("Invalid input! Number must be a digit.")