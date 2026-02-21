from flask import Flask, request, jsonify, session, render_template
import random

app = Flask(__name__)
app.secret_key = "supersecretkey"  # required for session

@app.route("/")
def index():
    return render_template("index.html")


@app.route("/start", methods=["POST"])
def start_game():
    data = request.get_json()
    player_name = data.get("player_name", "Player")
    session["player_name"] = player_name
    session["random_number"] = random.randint(1, 10)
    session["guesses"] = 0
    return jsonify(message=f"Welcome {player_name}! Guess a number between 1 and 10.")


@app.route("/guess", methods=["POST"])
def guess_number():
    data = request.get_json()
    user_guess = int(data.get("guess", 0))
    random_number = session.get("random_number")
    session["guesses"] += 1

    if user_guess < 1 or user_guess > 10:
        return jsonify(result="Only numbers between 1 and 10.")
    elif user_guess < random_number:
        return jsonify(result="Wrong. It's higher.")
    elif user_guess > random_number:
        return jsonify(result="Wrong. It's lower.")
    else:
        attempts = session["guesses"]
        session["random_number"] = random.randint(1, 10)  # reset game
        session["guesses"] = 0
        return jsonify(result=f"Correct! It took you {attempts} attempts. 🎉 New number generated.")

if __name__ == "__main__":
    app.run(debug=True)