import random

def coin_toss():
    if random.random() > 0.5:
        print("Heads")
    else:
        print("Tails")

coin_toss()

