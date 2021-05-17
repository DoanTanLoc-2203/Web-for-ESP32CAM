import MySQLManage as SQL
from flask import Flask
from flask import render_template
from flask import Response, redirect, url_for, request
import urllib.request

import face_recognition
import cv2
import numpy as np
import os
from os import path

app = Flask(__name__)
# UPLOAD_FOLDER = './static/DataFace'
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
img_url = "https://i0.wp.com/media.giphy.com/media/nsHjVgedX9KoM/giphy.gif"
Uname = 'Unknow'


@app.route('/')
def login():
    return render_template('loginsite.html')


@app.route('/', methods=['POST'])
def checking():
    if request.method == 'POST':
        username = request.form['user']
        passw = request.form['pass']
        # print(username)
        # print(passw)
        global Uname
        Uname = username
        check = SQL.checkLogin(username, passw, "Manage_user")
        if(check):
            return redirect('/mainpage')
    return render_template('loginsite.html')


@app.route('/mainpage')
def mainpage():
    return render_template('index.html', imgURL="https://i.pinimg.com/originals/62/05/52/620552f745617c4e1314859463318630.gif", Uname=Uname)

@app.route("/request")
def abc():
    r = urllib.request.urlopen('http://172.20.10.3/open') 
    if(r.getcode() == 200):
        return redirect("/mainpage")


@app.route("/main")
def home():
    return render_template('stream.html', imgURL="https://i.pinimg.com/originals/62/05/52/620552f745617c4e1314859463318630.gif", Uname=Uname)


@app.route('/main/video_feed')
def video_feed():
    return Response(gen(), mimetype='multipart/x-mixed-replace; boundary=frame')


def gen():
    userdir = 'static/DataFace/' + Uname + '/'
    # video_capture = cv2.VideoCapture("https://172.20.10.2/cam.mjpeg")
    imgResp=urllib.request.urlopen("http://172.20.10.2/cam-hi.jpg")
    imgNp=np.array(bytearray(imgResp.read()),dtype=np.uint8)
    video_capture=cv2.imdecode(imgNp,-1)
    known_face_encodings = [


    ]
    known_face_names = [


    ]
    entries = os.listdir(userdir)
    for i in entries:
        print(i)
    if(len(entries) == 0):
        print("No data!")
        return 
    for im in entries:
        file_path = os.path.abspath(os.path.join(userdir, im))
        image = face_recognition.load_image_file(file_path)
        face_encoding = face_recognition.face_encodings(image)[0]
        known_face_encodings.append(face_encoding)
        known_face_names.append(im[0:im.find(".")])

        # img = face_recognition.load_image_file(im)
        # # Assume the whole image is the location of the face
        # height, width, _ = img.shape
        # # location is in css order - top, right, bottom, left
        # face_location = (0, width, height, 0)
        # encodings = face_recognition.face_encodings(img, known_face_locations=[face_location])

    # Initialize some variables
    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True

    while True:
        # Grab a single frame of video
        # ret, frame = video_capture.read()
        frame =  video_capture
        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]

        # Only process every other frame of video to save time
        if process_this_frame:
            # Find all the faces and face encodings in the current frame of video
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(
                rgb_small_frame, face_locations)

            face_names = []
            for face_encoding in face_encodings:
                # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces(
                    known_face_encodings, face_encoding)
                name = "Unknown"

                # # If a match was found in known_face_encodings, just use the first one.
                # if True in matches:
                #     first_match_index = matches.index(True)
                #     name = known_face_names[first_match_index]

                # Or instead, use the known face with the smallest distance to the new face
                face_distances = face_recognition.face_distance(
                    known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]

                face_names.append(name)

        process_this_frame = not process_this_frame

        # Display the results
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35),
                          (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6),
                        font, 1.0, (255, 255, 255), 1)
        im = cv2.imencode('.jpg', frame)[1].tobytes()
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + im + b'\r\n')


@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST' and 'files' in request.files:
        userdir = 'static/DataFace/' + Uname + "/"
        app.config['UPLOAD_FOLDER'] = userdir
        name = request.form['name']
        print(name)
        for f in request.files.getlist('files'):
            print(f.filename)
            f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
        os.rename(userdir + f.filename,
                  userdir + name + ".png")
        return 'Up load data face complete!'
    return render_template('upload_image.html')


@app.route('/remove')
def remove_render():
    userdir = 'static/DataFace/' + Uname + "/"
    entries = os.listdir(userdir)
    print(Uname)
    return render_template('remove_image.html', itemList=entries, Uname=Uname)


@app.route('/remove/<filename>', methods=['GET', 'POST'])
def submit(filename):
    userdir = 'static/DataFace/' + Uname + "/"
    os.remove(userdir + filename)
    res = "remove " + filename + " success!"
    return res


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8001)
