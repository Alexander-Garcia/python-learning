from flask import Flask
import random

app = Flask(__name__)

winning_number = random.randint(1,9)

def check_number(num):
    if num > winning_number:
        return "<h4>Guess was too high</h4>"
    elif num < winning_number:
        return "<h4>Guess was too low</h4>"
    elif num == winning_number:
        return "<h4>Bingo</h4>"
    else:
        return "Shouldn't get here"

@app.route("/")
def game_intro():
    return "<h1 style='text-align: center'>Welcome to higher or lower.</h1>" \
            "<h2 style='text-align: center'>Guess a number in the URL route for some reason</h2>"


@app.route("/<int:user_number>")
def user_guess(user_number):
    result = check_number(user_number)
    return result


if __name__ == "__main__":
    app.run(debug=True)

