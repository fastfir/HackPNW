from flask import Flask, render_template, request
import random
import logic
app = Flask(__name__)
game = logic.Game()
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/game", methods=['POST'])
def backend():
    game.log(request.form['day'],request.form['money'],request.form['size'])
@app.route("/question")
def question():
    return game.questions[random.range(0,len(game.questions))]