'''
projekt_2.py: druhý projekt do Engeto Online Python Akademie
author: Lukáš Smejkal
email: smejklukas@gmail.com
discord: Razee #6106
'''

import random

## Generate number

def generate_number(n_of_numbers:int)->str:
    """
    Generate a random number with the specified number of digits.

    Args:
        n_of_numbers (int): Number of digits in the generated number.

    Returns:
        str: Random number with the specified number of digits.
    """
    rnum = random.sample("0123456789", n_of_numbers)
    rnum = "".join(rnum)
    if rnum[0] == "0":
        rnum = generate_number(n_of_numbers)
    return rnum



## count cows

def count_cows(number: str, guess: str) -> int:
    """
    Count the number of cows in the guessed number.

    Args:
        number (str): The secret number to compare against.
        guess (str): The guessed number.

    Returns:
        int: The number of cows in the guessed number.
    """
    cows = 0
    for numnum in guess:
        if numnum in number:
            cows += 1
    return cows
    

## Count bulls

def count_bulls(number: str, guess: str) -> int:
    """
    Count the number of bulls in the guessed number.

    Args:
        number (str): The secret number to compare against.
        guess (str): The guessed number.

    Returns:
        int: The number of bulls in the guessed number.
    """
    bulls = 0
    for i in range(len(guess)):
        if guess[i] == number[i]:
            bulls +=1
    return bulls

## Winer

def winner(number: str, guess: str) -> bool:
    """
    Check if the guess matches the secret number.

    Args:
        number (str): The secret number.
        guess (str): The guessed number.

    Returns:
        bool: True if the guess matches the secret number, False otherwise.
    """
    if guess == number:
        return True
    return False


## Print state

def print_state(bulls: int, cows: int) -> None:
    """
    Print the current state of the game with the number of bulls and cows.

    Args:
        bulls (int): The number of bulls.
        cows (int): The number of cows.

    Returns:
        None
    """
    print(f"There are {bulls} bulls and {cows} cows")



def guess_valid(number: str, txtlen: int) -> bool:
    """
    Check if the guessed number is valid.

    Args:
        number (str): The guessed number.
        txtlen (int): The expected length of the guessed number.

    Returns:
        bool: True if the guessed number is valid, False otherwise.
    """
    if len(number) != txtlen:
        print(f"text must have {txtlen} digits")
        return False
    if number[0] == "0":
        print("text cant contain a 0 number on first position")
        return False
    if not number.isdigit():
        print("text must contain only digits not a letters")
        return False
    for i in number:
        rep = number.replace(i,"")
        if len(rep) != len(number) - 1:
            print("text cant containt two same digits")
            return False
    return True
        
## Game engine

def game_engine(n_of_numbers: int) -> None:
    """
    Main game engine function for playing the bulls and cows game.

    Args:
        n_of_numbers (int): The number of digits in the secret number.

    Returns:
        None
    """
    guess = generate_number(n_of_numbers)
    while True:
        guess_input = input("Write your guess number: ")
        if not guess_valid(guess_input, n_of_numbers):
            continue
        if winner(guess, guess_input):
            break
        bulls = count_bulls(guess, guess_input)
        cows = count_cows(guess, guess_input)
        cows -= bulls
        print_state(bulls,cows)
    print()
    print("♫ ♫ ♫ ♫ ♫ YOU WON ♫ ♫ ♫ ♫ ♫")    

       
def main() -> None:
    """
    Main function to start the Bulls and Cows game.
    
    Returns:
        None
    """
    print("******WELCOME TO THE GAME BULLS AND COWS!******")
    print()
    print("Try to guess the secret 4-digit number with unique digits.")


    game_engine(4)

if __name__ == "__main__":
    main()


