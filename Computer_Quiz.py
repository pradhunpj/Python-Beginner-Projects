print("Welcome to my Computer Quiz\n")
print("-------------------------------\n")

playing = input("Do you wanna play? ").lower()
if playing != "yes":
    quit()
    
score = 0

print("You are about to start the quiz. Good luck!\n")

ans= input("What deos GUI stands for ? ").title()
if ans == "Graphical User Interface":
    score += 1
    print("Correct!")
else:
    print("Wrong! The correct answer is Graphical User Interface.")

ans= input("What deos CPU stands for ? ").title()
if ans == "Central Processing Unit":
    score += 1
    print("Correct!")
else:
    print("Wrong! The correct answer is Central Processing Unit.")

ans= input("What deos RAM stands for ? ").title()
if ans == "Random Access Memory":
    score += 1
    print("Correct!")
else:
    print("Wrong! The correct answer is Random Access Memory.")

ans= input("What deos ROM stands for ? ").title()
if ans == "Read Only Memory":
    score += 1
    print("Correct!")
else:
    print("Wrong! The correct answer is Read Only Memory.")

print(f"Your final score is {score}")
#to print percentage

percentage = (score/4) * 100
print(f"Your percentage score is {percentage}%")