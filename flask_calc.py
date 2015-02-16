from flask import Flask, render_template, request

calc_app = Flask(__name__)

@calc_app.route('/')
def form():
    return render_template('calculator.html')


@calc_app.route('/calculator', methods=["POST"])
def calculate():
    first = str(request.form['first'])
    operator = str(request.form['operator'])
    second = str(request.form['second'])
    result = eval(first+operator+second)
    return render_template("calc_result.html", result=result)


if __name__ == "__main__":
    calc_app.run(debug=True)
