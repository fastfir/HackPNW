from flask import Flask, render_template, request
import random
import json
import logic
app = Flask(__name__)
game = logic.Game()
@app.route("/")
def home():
    return render_template("game menu.html")
@app.route("/city")
def city():
    return render_template("city.html")
@app.route("/log", methods=['POST'])
def log():
    game.log(request.form['day'], request.form['money'], request.form['size'])
@app.route("/question")
def question():
    question = game.questions[random.randrange(len(game.questions))]
    return {
        "question": question
    }
@app.route("/shop")
def shop():
    itemList = []
    for item in game.items:
        itemList.append(item)
    return {

    }