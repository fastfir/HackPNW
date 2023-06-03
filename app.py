from flask import Flask, render_template, request
import logic
app = Flask(__name__)
game = logic.Game()
@app.route("/")
def game():
    return "Hello World!"
@app.route("/game", methods=['POST'])
def backend():
    game.evan(request.form['day'],request.form['money'],request.form['size'])