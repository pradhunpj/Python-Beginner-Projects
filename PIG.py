import random
print("Welcome to PIG\n")
def roll():
    return random.randint(1, 6)

while True:
    players = input("Enter no of players (2-4): ")
    if  players.isdigit() and 2 <= int(players) <= 4:
        players = int(players)
        break
    else:
        print("Invalid input! Number of players must be between 2 and 4.\n")

score = [0 for _ in range(players)]
max_score= 20

while max(score) < max_score:
    for player_idx in range(players):
        print(f"\nPlayer {player_idx+1}'s turn\n")
        current_score = 0
        print("Your current score is",current_score)
        while True:
            ask_roll = input("Do you want to roll (y/n)?\n")
            if ask_roll.lower() != "y":
                break
            dice_roll = roll()
            if dice_roll == 1:
                print("You rolled a 1, your score has been reset to 0.")
                current_score = 0
                break
            else:
                current_score += dice_roll
                print(f"You rolled a {dice_roll}. Your new score is {current_score}.")
        score[player_idx] = current_score

max_score= max(score)
win_idx = score.index(max_score)
print(f"Player {win_idx +1} has won the game with highest score of {max_score}")
