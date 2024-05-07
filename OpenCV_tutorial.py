import cv2 as cv
import sys
import numpy as np
from math import sqrt

try: 
    img = cv.imread(cv.samples.findFile("eye_colour_blue_test.jpg"))
except cv.error:
    print("\n-----File not found-----")
    sys.exit(0) 

# Create a black image and a window 
#img = np.zeros((512,512,3), np.uint8)
#cv.namedWindow('image')

h,w,_ = img.shape    #img is a ndarray
print(f"\nSize of image h:{h} w:{w}") 

""" cv.line(img,(0,0),(w,h),(255,0,0),5) # Draw a diagonal blue line with thickness of 5 px
cv.line(img,(w,0),(0,h),(0,0,255),3)

cv.rectangle(img,(220,190),(380,220),(0,255,0),3) #draw rectangle. top left corner, bottom right corner

cv.circle(img,(450,100), 30, (0,0,255), 2) # circle: center, radius, colour, thickness (-1=full). 
 """

font = cv.FONT_HERSHEY_SIMPLEX # write text
cv.putText(img,'test text',(10,350), font, 3,(0,0,0),2,cv.LINE_AA)

#cv.imshow("image", img)

""" print("\nPress 's' to save picture as .png")
k = cv.waitKey(0)
if k == ord("s"):
    cv.imwrite("eye_colour_blue_test.png", img)
    print("-> Pic saved!")
else:
    print("-> Pic not saved")  """

# mouse callback function to draw a circle when left click
""" def draw_circle(event,x,y,flags,param):
    if event == cv.EVENT_LBUTTONDBLCLK:
        cv.circle(img,(x,y),30,(255,0,0),-1) """


# ------------------- MOUSE AS PAINT BRUSH ------------------------------

mode = True # alternate mode rectange/circle for following function
ix,iy=-1,1
drawing = False
print_once = True
def draw_circle_or_rectangle(event,x,y,flags,param):
    global ix, iy, mode, drawing, print_once
    if print_once:
        print("Press 'm' to change mode")
        print_once = False
    if event == cv.EVENT_LBUTTONDOWN:
        drawing=True
        ix,iy=x,y

    elif event == cv.EVENT_MOUSEMOVE:
        if drawing==True:
            if mode == True:
                cv.rectangle(img,(ix,iy),(x,y),(0,255,0),-1)
            else:
                cv.circle(img,(ix,iy),int(sqrt(pow((ix-x),2)+pow((iy-y),2))),(0,0,255),-1)

    elif event == cv.EVENT_LBUTTONUP:
        drawing = False


# name window and bind function to it
cv.namedWindow('image')
cv.setMouseCallback('image',draw_circle_or_rectangle)

while True:
    cv.imshow("image", img)
    #if cv.waitKey(20) & 0xFF == 27: # if press 'esc' after 20ms
    #    break
    k = cv.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break
cv.destroyAllWindows()

# ------------------    TRACKBAR ------------------------

