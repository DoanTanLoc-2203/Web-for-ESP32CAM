from flask import Flask, render_template, request
import requests
import os

app = Flask(__name__)
UPLOAD_FOLDER = './static/image'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
img_url = "https://i0.wp.com/media.giphy.com/media/nsHjVgedX9KoM/giphy.gif"

@app.route('/')
def login():
	return render_template('loginsite.html')
	
@app.route("/main")
def home():
	return render_template('index.html', imgURL = img_url)

@app.route('/main', methods=['POST'])
def get_url():
	global img_url
	status = 200
	text =  request.form['url']
	print(text)
	if(text == ""):	
		img_url = "https://i0.wp.com/media.giphy.com/media/nsHjVgedX9KoM/giphy.gif"
		return render_template('index.html', imgURL = img_url)
	else:
		# try:
		# 	req = requests.get(text)
		# except:
  # 			print("Page not found!")
  # 			status = 404
		if(status != 200):
			img_url = "https://freefrontend.com/assets/img/html-css-404-page-templates/HTML-404-Typed-Message.gif"
			return render_template('index.html', imgURL = img_url)
		else:
			img_url = text;
			return render_template('index.html', imgURL = img_url)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
	if request.method == 'POST' and 'files' in request.files:
		for f in request.files.getlist('files'):
			print(f.filename)
			f.save(os.path.join(app.config['UPLOAD_FOLDER'], f.filename))
		return 'Upload completed.'
	return render_template('upload_image.html')

if __name__ == "__main__": 
    app.run(port=8001) 
