"""
Python Development Techdegree
Project 1 - The Number Guessing Game
--------------------------------
"""

import random
import sys
import time

def select_user():
    return input("Select user name: ").strip()

def start_game(player_name):
    print("#"*10 + " "*10 + "#"*10)
    print("#"*10 + f" Welcome {player_name}! " + "#"*10)
    print("#"*20)
    time.sleep(1)

    random_number = random.randint(1, 10)
    guesses = 0
    user_guess = None

    while user_guess != random_number:
        try:
            user_guess = int(input("Guess a number between 1 and 10: "))
            if user_guess < 1 or user_guess > 10:
                print("Only numbers between 1 and 10. Try again...")
                continue

            guesses += 1

            if user_guess < random_number:
                print("Wrong. It's higher. Try again...")
            elif user_guess > random_number:
                print("Wrong. It's lower. Try again...")

        except ValueError as err:
            print("Enter a valid number from 1 to 10.")
            print(f"({err})")

    print(f"Congratulations! It took you {guesses} attempts. The number was {random_number}.")

def continue_game(player_name):
    while True:
        answer = input("Play again? (Yes/No): ").strip().lower()
        if answer in ["yes","y"]:
            start_game(player_name)
        elif answer in ["no","n"]:
            print("Game over.")
            sys.exit()
        else:
            print("Enter Yes or No only.")

def main():
    player_name = select_user()
    start_game(player_name)
    continue_game(player_name)

if __name__ == "__main__":
    main()