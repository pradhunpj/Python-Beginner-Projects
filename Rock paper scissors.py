import random

computer_score = 0
user_score = 0

options = ["rock","paper","scissors"]

print("Welcome to Rock Paper Scissors Game\n")


while True:
    user_input = input("Type Rock/Paper/Scissors or type Q to quit: ").lower()
    if user_input == "q":
        break

    if user_input not in options:
        continue

    rand = random.randrange(0,3)
    computer_input = options[rand]
    print("Computer chose",computer_input)
    if user_input == "scissors" and computer_input == "paper":
        print("You win\n")
        user_score += 1
    
    
    elif user_input == "rock" and computer_input == "scissors":
        print("You win\n")
        user_score += 1

    
    elif user_input == "paper" and computer_input == "rock":
        print("You win\n")
        user_score += 1

    else:
        print("Computer Win\n")
        computer_score +=1

print("Your score:",user_score)
print("Computer's score:",computer_score)
print("Goodbye")
