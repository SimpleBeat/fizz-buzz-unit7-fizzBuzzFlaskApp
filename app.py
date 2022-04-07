import flask


from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def start():
    answers = []
    for n in range(1, 101):
        s = ""
        if n % 3 == 0:
            s = "Fizz"
        if n % 5 == 0:
            s += "Buzz"
        if s == "":
            s = str(n)
        answers.append(s)

    return render_template('fizzBuzz.html', answers=answers)