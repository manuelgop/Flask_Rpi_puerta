from flask import Flask, render_template
import pyimgur
import picamera
import time

# name and dimentsions of snapshot image
IMG_WIDTH = 800
IMG_HEIGHT = 600

# imgur client setup
CLIENT_SECRET = "35bbaad924b810b11834b3f1ecd2d8a9bae70001"
CLIENT_ID = "f62c298b228cb53"
#image DIR
IMAGE_DIR = "/home/pi/"
#Image name
IMG = "foto.jpg"
# text message to send with photo
TXT_MSG = "Foto prueba!"
app = Flask(__name__)

@app.route("/")
def hello():
	# initialize imgur client
	im = pyimgur.Imgur(CLIENT_ID)
	with picamera.PiCamera() as camera:
			camera.resolution = (IMG_WIDTH, IMG_HEIGHT)
			camera.start_preview()
			time.sleep(2)
			camera.capture(IMAGE_DIR + IMG)
	uploaded_image = im.upload_image(IMAGE_DIR + IMG, title=TXT_MSG)
	link = (uploaded_image.link)
	user = {'nickname': 'Miguel'}  # fake user
	return render_template('index.html')

@app.route("/hola")
def hola():
	return "Estas en un /hola"

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=50, debug=True)
