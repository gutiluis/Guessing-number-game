## How it works:

Within the terminal run:
- python3 -m venv venv
- source venv/bin/activate
- pip install -r requirements.txt
- python3 app.py


import random module to generate the winning number.
provides a welcome message.
store a random number within the games range and store it within a variable.
continous guess prompting using a while loop until the user guesses correctly.
Provide Correct Feedback
Using conditional statements, checks if the player provides an incorrect guess. 
They should be told if their guess is higher or lower than the answer. This is so they can narrow down their guesses.

Display the Score.
displays the amount of guesses it takes the player to guess correctly.
Increase this value whenever the player provides an incorrect guess.
After the game ends, show the number of attempts it took.
Display a Goodbye Message
Handle Errors and Exceptions
catch exceptions and report the errors to the user in a meaningful way. For example, non-number and floating-point number guesses should be handled with an exception to make sure the app won't crash.


Pick and make a guess of a number between 1 and 10. 
Reply whether the guess is too high or too low. 
Their next guess is based on previous input. T
he game ends when the player guesses the correct number. 
Try to do this in the lowest number of possible attempts. 

# Flask API
app.py handles the random number, guesses, and session(cookies) tracking per player with flask

session is a special dictionary that lets you store data per user across multiple requests

Session HTTP is stateless: every request is independent. If you reload the page or make a new Ajax request, the server has no memory of previous requests.

Receives user input from the frontend via Ajax (/guess endpoint)

Keeps track of game state in Flask session (random_number, guesses, player_name) must be stored

Sends responses back to the frontend as JSON

The frontend displays messages in the browser instead of the terminal

# jquery frontend
User enters name. clicks Start Game. Flask creates session with random number & guess count.
User enters a guess. jQuery sends it via Ajax. Flask checks and returns feedback.
If correct session resets new number generated automatically.
Page updates dynamically, no reloads needed.

-----

#####

-----


## Features:

- Generates a random number between a specified range (default 1–100).
- Prompts the player to guess the number.
- Provides feedback if the guess is too high or too low.
- Tracks the number of attempts.
- Congratulates the player if they guess correctly.
- Ends the game if the player exceeds the maximum number of guesses.

-----

####

-----

## Technologies:

- Python
- jQuery
- JavaScript
- Flask

-----

###

-----

## Skills Learned:

How to use the random library and import modules

-----

###

Clone the repository:

```bash
git clone https://github.com/gutiluis/Techdegree-project-1.git
```
