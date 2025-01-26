from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello, world!!!!!!!"

@app.route('/about')
def about():
    a = 10
    b = 1
    return '<h1>We are programmers {}</h1>'.format(a/b)

@app.route('/error')
def error():
    a = 10
    b = 0
    return '<h1>We are programmers {}</h1>'.format(a/b)

@app.route("/cantor/<string:currency>/<int:amount>")
def cantor(currency, amount):
    message =f"<h1>You selected {currency} and {amount}</h1>"
    return message

if __name__ == '__main__':
    app.run(debug=True)