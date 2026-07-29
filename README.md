>![WARNING]
>CURRENTLY UNDER DEVELOPMENT


# Guessing Number Game in python

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


## How it works:
```
python3 guessing_game.py
```

---

## Features

- Generates a random number between 1 through 10.
- Prompts the player to guess the number.
- Provides feedback if the guess is too high or too low.
- Tracks the number of attempts.
- Congratulates the player if they guess correctly.
- Ends the game if the player exceeds the maximum number of guesses.

---

## Tech-Stack

- Python

---

## Skills

- How to use the random library and import modules

---

## Web-Version Branch

There is a Web-Version branch with a Flask web interace for this game.

The web-version branch has:
A web interface for guessing the number
Flask-based routes api, templates with jQuery and JavaScript
Browser-based gameplay

To acces switch branches:
- git checkout web-version

---

## Contributing

If you are interested in reporting/fixing issues and contributing directly to the code base, please see CONTRIBUTING.md for more information on what we're looking for and how to get started.

---

## Community

Info on reporting bugs, getting help, finding third-party tools and sample apps, and more can be found on the Community page.

---

## License

[MIT LICENSE](LICENSE)
