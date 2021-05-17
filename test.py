from flask import Flask
from flask import render_template
from flask import Response

import face_recognition
import cv2
import numpy as np
import os

import cv2

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

app.run(host='0.0.0.0', port = '8000')