import unittest
import requests
from test_fibonachi import fibonachi
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    t = [1,2,3]
    print(*t, sep='\n')
    a = list(map(int,fibonachi(10)))
    return a

@app.route('/testik222')
def fib_1():
    cnt = 17
    return f'<h1>{str(list(fibonachi(cnt)))[1:-1]}<h1>'

@app.route('/testik321')
def number(n):
    fibgen = fibonachi(n)
    res = [next(fibgen) for i in range(n)]
    return res

@app.errorhandler(404)
def not_found_error(error):
    return "Необходимо ввести елое число"


if __name__ == "__main__":
    app.run(debug = True)
