from flask import Flask, render_template, request
import random
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
    return game.calcRep(request.form['score'])
@app.route("/question")
def question():
    question = game.questions[random.randrange(len(game.questions))]
    return { "question": question }
@app.route("/shop", methods=['GET', 'POST'])
def shop():
    if request.method == "GET":
        return game.items
    elif request.method == "POST":
        game.items.pop(request.args.get('bought'))
        game.bought.append(request.args.get('bought'))
@app.route("/eod")
def eod():
    return {
        "Day": game.day,
        "Money": game.money,
        "Protesters": game.size,
        "Items Bought": game.bought
    }