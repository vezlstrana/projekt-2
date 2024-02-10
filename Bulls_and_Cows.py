import random

## Generate number

def generate_number(n_of_numbers):
    rnum = random.sample("0123456789", n_of_numbers)
    rnum = "".join(rnum)
    return rnum



## count cows

def count_cows(number, guess):
    cows = 0
    for numnum in guess:
        if numnum in number:
            cows +=1
    return cows
    

## Count bulls

def count_bulls(number, guess):
    bulls = 0
    for i in range(len(guess)):
        if guess[i] == number[i]:
            bulls +=1
    return bulls
## Winer

def winner(number,guess):
    if guess == number:
        return True
    return False


## Print state

def print_state(bulls, cows):
    print(f"There are {bulls} bulls and {cows} cows")
    #dodelat grafiku

def guess_valid(number:str):
    for i in number:
        rep = number.replace(i,"")
        if len(rep) != len(number) - 1:
            return False
    return True
        
## Game engine

def game_engine(n_of_numbers):
    guess = generate_number(n_of_numbers)
    while True:
        guess_input = input("Write your guess number: ")
        if not guess_valid(guess_input):
            continue
        if winner(guess, guess_input):
            break
        bulls = count_bulls(guess, guess_input)
        cows = count_cows(guess, guess_input)
        cows -= bulls
        print_state(bulls,cows)
    print()
    print("!!!!you won!!!!")            

print("******WELCOME TO THE GAME BULLS AND COWS!******")
print()
print("Try to guess the secret 4-digit number with unique digits.")


game_engine(4)



