import cv2 as cv
import sys
import numpy as np
import json
from mtcnn.mtcnn import MTCNN

# The detector returns a list of JSON objects. Each JSON object contains three main keys: 
#'box', 'confidence' and 'keypoints'
detector = MTCNN()

# Writes into a json file the result of the MTCNN detector.detect_faces method -> list of JSON objects
""" #img = cv.imread(cv.samples.findFile(f"kuvat/eye_blue1.jpg")) #Open way 1
img = cv.cvtColor(cv.imread(f"kuvat/eye_blue1.jpg"), cv.COLOR_BGR2RGB) #Open way2
data = detector.detect_faces(img)
with open ('data2.json', 'w') as f:
    json.dump(data, f, indent=4)
 """

# Function to choose image, return error message if pic not found then close.
def choosepic(color, number):
    try: 
        img = cv.imread(cv.samples.findFile(f"kuvat/eye_{color}{number}.jpg"))
        #img = cv.cvtColor(cv.imread(f"kuvat/eye_{color}{number}.jpg"), cv.COLOR_BGR2RGB)
        print("Image loaded")
        h, w, _ = img.shape
        print(f"\nSize of image h:{h} w:{w}") 
        return img
    except cv.error:
        print("\n-----File not found-----")
        sys.exit(0) 

# Function to detect face and eyes (using mtcnn), and draw a rectangle and circles
def eye_detection(img):
    #imgHSV = cv.cvtColor(img, cv.COLOR_BGR2HSV)
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

    cv.imshow('FACE_EYES_DETECTION', img)

# Function that apply a "blue filter", everything not blue will be blacked out
def blue_filter(img):
    lower_blue = np.array([0, 0, 0], dtype = "uint8")
    upper_blue= np.array([255, 100, 100], dtype = "uint8")
    mask = cv.inRange(img, lower_blue, upper_blue)
    img_filtered = cv.bitwise_and(img, img, mask = mask)
    return img_filtered

# Function that apply a "green filter", everything not green will be blacked out
def green_filter(img):
    lower_green = np.array([0, 0, 0], dtype = "uint8")
    upper_green = np.array([100, 255, 100], dtype = "uint8")
    mask = cv.inRange(img, lower_green, upper_green)
    img_filtered = cv.bitwise_and(img, img, mask = mask)
    return img_filtered


if __name__ == '__main__':
    color, number = input("\nChose a color and number: ").split()
    choosepic(color, number)
    img = choosepic(color, number)

    eye_detection(img)
    cv.imwrite(f"results/resultpic_{color}{number}.jpg", img)    
    cv.waitKey(0)

    
    #img_filtered = blue_filter(img)
    #cv.imshow("blue color detection", img_filtered) 
    #cv.imwrite(f"results/resultbluefilter_{color}{number}.jpg", img_filtered)    
    #cv.waitKey(0)

    #img_filtered = green_filter(img)
    #cv.imshow("green color detection", img_filtered) 
    #cv.imwrite(f"results/resultgreenfilter_{color}{number}.jpg", img_filtered)    
    #cv.waitKey(0) 