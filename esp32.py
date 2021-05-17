from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def aaa():
    return "dwqewqew"

@app.route('/data', methods = ['POST'])
def post():

    print(request.data)
    return ''

if __name__ == '__main__':
    app.run()