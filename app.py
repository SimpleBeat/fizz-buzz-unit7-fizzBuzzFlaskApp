import flask

app = flask.Flask(__name__)

@app.route("/")
@app.route("/fizzbuzz/<int:max_number>")
def start(max_number=20):
    answers = []
    for n in range(1, max_number+1):
        s = ""
        if n % 3 == 0:
            s = "Fizz"
        if n % 5 == 0:
            s += "Buzz"
        if s == "":
            s = str(n)
        answers.append(s)
    count = len(answers)

    return flask.render_template('fizzBuzz.html', answers=answers, count=count)