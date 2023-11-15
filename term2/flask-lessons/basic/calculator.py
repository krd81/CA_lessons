from flask import Flask, request
import json

# calculator commands: add, subtract, multiply, divide

app = Flask(__name__)

@app.route('/')
def index():
    return '<h3>Hello, World!</h3>'


@app.route('/<int:num1>/add/<int:num2>')
def add(num1, num2):
    result = {'operation': f'{num1} plus {num2}', 'result': num1 + num2}
    return json.dumps(result)


@app.route('/<int:num1>/subtract/<int:num2>')
def subtract(num1, num2):
    result = {'operation': f'{num1} minus {num2}', 'result': num1 - num2}
    return json.dumps(result)

    
@app.route('/<int:num1>/multiply/<int:num2>')
def multiply(num1, num2):
    result = {'operation': f'{num1} multiplied by {num2}', 'result': num1 * num2}
    return json.dumps(result)

    
@app.route('/<int:num1>/divide/<int:num2>')
def divide(num1, num2):
    result = {'operation': f'{num1} divided by {num2}', 'result': num1 / num2}
    return json.dumps(result)








@app.errorhandler(404)
def not_found(error):
    return {'error': str(error)}, 404


if __name__ == '__main__':
    app.run(debug=True)

