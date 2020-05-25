import random

rand_num = random.randint(1,10)
print("\nWelcome to the Guessing game!")
guess = None
while True:
    guess = input("\nEnter a number from 1 to 10 : ")
    guess = int(guess)
    if guess<rand_num:
        print("Too low! Try a bigger number.")
    elif guess>rand_num:
        print("Too high! Try a smaller number.")
    else:
        print("You are correct!")
        play_again = input("Do you want to play again? (y/n) ")
        if play_again == "y":
            rand_num = random.randint(1, 10)
            guess = None
        else:
            print("Thank you for playing!")
            break





