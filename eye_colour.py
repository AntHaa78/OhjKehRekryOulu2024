import cv2 as cv
import sys
import numpy as np
from mtcnn.mtcnn import MTCNN

# The detector returns a list of JSON objects. Each JSON object contains three main keys: 
#'box', 'confidence' and 'keypoints'
detector = MTCNN()

def choosepic(color, number):
    try: 
        img = cv.imread(cv.samples.findFile(f"kuvat/eye_{color}{number}.jpg"))
        print("Image loaded")
        h, w, _ = img.shape
        print(f"\nSize of image h:{h} w:{w}") 
        return img
    except cv.error:
        print("\n-----File not found-----")
        sys.exit(0) 

def eye_detection(img):
    #imgHSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    h, w, _ = img.shape
    imgMask = np.zeros((img.shape[0], img.shape[1], 1))
    
    result = detector.detect_faces(img)
    if result == []:
        print('Warning: Can not detect any face in the input img!')
        return

    bounding_box = result[0]['box']
    left_eye = result[0]['keypoints']['left_eye']
    right_eye = result[0]['keypoints']['right_eye']

    eye_distance = np.linalg.norm(np.array(left_eye)-np.array(right_eye))
    eye_radius = eye_distance/15 # approximate
   
    cv.circle(imgMask, left_eye, int(eye_radius), (255,255,255), -1)
    cv.circle(imgMask, right_eye, int(eye_radius), (255,255,255), -1)

    cv.rectangle(img,
              (bounding_box[0], bounding_box[1]),
              (bounding_box[0]+bounding_box[2], bounding_box[1] + bounding_box[3]),
              (255,155,255),
              2)

    cv.circle(img, left_eye, int(eye_radius), (0, 155, 255), 1)
    cv.circle(img, right_eye, int(eye_radius), (0, 155, 255), 1)

    cv.imshow('EYE-COLOR-DETECTION', img)


def show_blue(img):
    lower_blue = np.array([0, 0, 0], dtype = "uint8")
    upper_blue= np.array([255, 100, 100], dtype = "uint8")
    mask = cv.inRange(img, lower_blue, upper_blue)
    detected_output = cv.bitwise_and(img, img, mask = mask)
    cv.imshow("blue color detection", detected_output)
    cv.waitKey(4000)

def show_green(img):
    lower_green = np.array([0, 0, 0], dtype = "uint8")
    upper_green = np.array([100, 255, 100], dtype = "uint8")
    mask = cv.inRange(img, lower_green, upper_green)
    detected_output = cv.bitwise_and(img, img, mask = mask)
    cv.imshow("green color detection", detected_output)
    cv.waitKey(4000)

""" def show_white(img):
    lower_white = np.array([180, 180, 180], dtype = "uint8")
    upper_white = np.array([255, 255, 255], dtype = "uint8")
    mask = cv.inRange(img, lower_white, upper_white)
    detected_output = cv.bitwise_and(img, img, mask = mask)
    cv.imshow("white color detection", detected_output)
    cv.waitKey(4000) """



if __name__ == '__main__':
    #color, number = input("\nChose a color and number: ").split()
    #choosepic(color, number)
    img = choosepic('blue', 1)
    #cv.rectangle(img,(220,190),(380,220),(200,0,0),3)

    eye_detection(img)
    cv.imwrite('result.jpg', img)    
    cv.waitKey(0)

    #show_blue(img)
    #show_green(img)