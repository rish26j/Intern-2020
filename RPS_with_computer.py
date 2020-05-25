import random

option1="rock"
option2="paper"
option3="scissors"

player_wins = 0
computer_wins = 0
while player_wins<2 and computer_wins<2:
    print(f"Your Score : {player_wins} ---- Computer Score : {computer_wins}")
    player = input("Enter your move : ").lower()
    computer = ""
    rand_num = random.randint(0,2)
    if rand_num == 0:
        computer = "rock"
    elif rand_num == 1:
        computer = "paper"
    else:
        computer = "scissors"
    print("Computer plays : " + computer)
    if (player and computer):
        if (player==option1 and computer==option3) or (player==option2 and computer==option1) or(player==option3 and computer==option2):
                print("You win!")
                player_wins+=1
        elif (player==computer):
                print("It's a draw.")
        elif(computer==option1 and player==option3) or (computer==option2 and player==option1) or(computer==option3 and player==option2):
                print("Computer wins! :(")
                computer_wins+=1
        else:
            print("This is not an option")
    else:
        print("Something went wrong")

print(f"Final Score : You : {player_wins}   Computer : {computer_wins}")