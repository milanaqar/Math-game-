from flask import Flask, render_template, request, redirect, url_for, session
from game_logic import generate_question

app = Flask(__name__)
app.secret_key = "odyssey_secret"

@app.route("/choose_difficulty")
def choose_difficulty():
    return render_template("choose_difficulty.html")

@app.route ("/battle/<difficulty>")
def start_battle(difficulty):
    session["difficulty"] = difficulty
    session["round"] = 1
    session["score"]= 0 

    num1, num2, op, correct = generate_question(difficulty)
    session["correct"] = correct

    return render_template(
        "battle.html",
        round=session["round"],
        num1=num1,
        num2=num2,
        operation=op
    )

@app.route("/result")
def result():
    return render_template("result.html", score=session["score"])