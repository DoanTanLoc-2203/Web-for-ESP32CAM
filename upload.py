import os
from flask import Flask, request, render_template

UPLOAD_FOLDER = './image'

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    return render_template('test.html')
if __name__ == '__main__':
    app.run()