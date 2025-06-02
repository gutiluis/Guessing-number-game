"""
Python Development Techdegree
Project 1 - The Number Guessing Game
--------------------------------
"""
import random
import sys
import time



def select_user():
	a = input("Select user name: ").strip()
	return a


def start_game(player_name):
	print("#"*10 + " "*10 + "#"*10)
	print("#"*10 + " " + f"Welcome {player_name}!" + " " + "#"*10)
	print("#"*20)
	print("#"*20)
	time.sleep(1)
	random_number = random.randint(1,10)
	guesses = 0
	secret_number = True
	while secret_number != random_number:
		try:
			secret_number = int(input("Guess a number between 1 and 10: "))
			if secret_number > 10 or secret_number < 1:
				print("Only numbers between 1 and 10. Try again...")
				continue
			if secret_number < random_number:
				print("Wrong. It's higher. Try again...")
				guesses += 1
			if secret_number > random_number:
				print("Wrong. It's lower. Try again...")
				guesses += 1
		except ValueError as err:
			print("Enter a number from 1 to 10.")
			print("({})".format(err))
	else:
		secret_number = random_number
		guesses += 1
		print("Congratulations it took you",str(guesses),"attempts. The random number is",(secret_number),)


def continue_game():
    while True:
        any_var = input("Play again? ").strip()
        if any_var.isdigit():
            print("Enter Yes or No only.")
            continue
        if any_var in ["Yes","Y","y","YES", "yes"]:
            start_game()
        else:
            any_var in ["No","N","NO","no","n"]
            print("Game over.")
            sys.exit()
        

def main():
	a = select_user()
	start_game(a)
	continue_game()



if __name__ == "__main__":
	main()

