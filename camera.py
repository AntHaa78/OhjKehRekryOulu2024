from picamera import PiCamera, Color
import time
import sys

res_max = (2592, 1944) # max camera resolution
res_1440 = (2560, 1440)
res_1080 = (1920, 1080)


camera = PiCamera()
camera.rotation = 180 # camera upside down -> rotate
camera.resolution = res_1440
#camera.framerate = 15 #To use for res_max
camera.annotate_text_size = 150

def main():
	camera.start_preview()
	time.sleep(10)
	camera.resolution = res_max
	camera.framerate = 15 #To use for res_max
	for i in range(10):
		time.sleep(1)
		camera.annotate_text = "Eye %s" % i
		camera.capture('/home/pi/cam_project/eye%s.jpg' % i)
	camera.stop_preview()
	sys.exit(0)

# ~ def main2():
	# ~ camera.start_preview() #(alpha=200 to make the picture transparent during tests)
	# ~ camera.annotate_background = Color("white")
	# ~ camera.annotate_foreground = Color("black")
	# ~ for i in range(6):
		# ~ time.sleep(1)
		# ~ camera.annotate_text = "Eye %s" % i
		# ~ camera.capture('/home/pi/cam_project/eye%s.jpg' % i)
	# ~ #time.sleep(6)
	# ~ #camera.brightness = 60     0:100 brightness
	# ~ # camera.image_effect = 'colorswap'
	# ~ #for effect in camera.IMAGE_EFFECTS:
	# ~ #	camera.image_effect = effect
	# ~ #	camera.annotate_text = "Effect is: %s" % effect
	# ~ #	time.sleep(2)
	# ~ #camera.capture('/home/pi/cam_project/eye1.jpg')
	# ~ camera.stop_preview()
	# ~ sys.exit(0)
	

#-> Otetaan kuvaa 3 6 7

if __name__ == "__main__":
	main()
