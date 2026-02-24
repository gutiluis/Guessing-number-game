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


# tests implementation
# .github workflows actions
github actions for pytest within a .yml file

- Any push to testing branch runs tests automatically.
- PRs to main or web-version branches must pass python-tests.yml jobs test before merging.
- Flask tests will only run if Flask is installed — no need to separate workflows.

- Always push testing branch first to run pytest. then merge into main or web-version to ensure CI pases first
- CI(Continous Integration)
Use CI for:
- pushing code to GitHub
- opening a pull request
And CI wil automatically:
- Download your repo
- Install dependencies
- Runs tests (like pytest)
- Reports pass / fail



# setup.py


# Flask API
app.py handles the random number, guesses, and session(cookies) tracking per player with flask

session is a special dictionary that lets you store data per user across multiple requests

A Flask session is client-side (in browser cookies). Not private-readable per user. Less secure. Size limitation smaller than Redis. Not for production apps, not for scalability.

With cookies can query by key and the key will be on the client side.

You may just keep the identifier in the cookie but store the rest in redis and you get the details by that identifier.

Session HTTP is stateless: every request is independent. If you reload the page or make a new Ajax request, the server has no memory of previous requests.

why is less secure a session cookie?
Even if the cookie session data is encrypted, the user could still roll back their cookie to a previous state (unless you start encoding one-time IDs etc)

the cookie stores the user state

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

## Skills:

How to use the random library and import modules.
How to get a function value out of its inner local scope to use in another function.
How to run flask WSGI and use cookie sessions.

-----

###

-----


Clone the repository:

```bash
git clone https://github.com/gutiluis/Guessing-number-game.git
```
