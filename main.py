import random

HighLow = random.randint(1,100)

def luck_of_the_draw(input):
    while input != HighLow:
        x = input("Your Guess? ")
        y = int(x)
        if y < HighLow:
            print("Higher")
        if y > HighLow:
            print("Lower")
        if y == HighLow:
            return print("Correct!")
            
            
luck_of_the_draw(input)
