import cv2
import numpy as np
import matplotlib.pyplot as plt
from camera_stream import opencam
from stack_image import stackImages 


framewidth=1280
frameheight=1000
cap=cv2.VideoCapture(0)
if not (cap.isOpened()):
        print('Could not open video device')
cap.set(3,framewidth)
cap.set(4,frameheight)


my_colors=[[45,82,96,121,255,255],
           [0,119,159,47,248,255]]
my_colour_values=[[255,0,0],
                  [51,153,255]]
all_points=[]
def find_col(img):
    new_points=[]
    imgHSV=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    i=0;
    for colors in my_colors:
        lower=np.array(colors[0:3])
        upper=np.array(colors[3:6])
        mask=cv2.inRange(imgHSV,lower,upper)
        x,y=get_contours(mask)
        cv2.circle(imgResult,(x,y),15,my_colour_values[i],cv2.FILLED)
        if(x!=0 and y!=0) :
            new_points.append([x,y,i])
        i+=1
        #cv2.imshow(str(colors[0]),mask)
    return new_points

def get_contours(img):
    contours,hei=cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    x,y,w,h=0,0,0,0
    for cnt in contours:
        area=cv2.contourArea(cnt)
        if(area>1000):
            #cv2.drawContours(imgResult,cnt,-1,(255,0,0),3)
            peri = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.2*peri,True)
            x, y, w, h = cv2.boundingRect(approx)
    return x+w//2,y

def Draw_line(points):
    tot=len(points)
    if(tot>1000):
        points=points[-1000:]
    for point in points:
        cv2.circle(imgResult,(point[0],point[1]),10,my_colour_values[point[2]],cv2.FILLED)
        
        
        
while True:
    success,img=cap.read()
    img = cv2.flip(img,1)
    imgResult=img.copy()
    new_points=find_col(img)
    for points in new_points:
        all_points.append(points)
    if(len(all_points)!=0) :
        Draw_line(all_points)

    cv2.imshow('Result',imgResult)
    if cv2.waitKey(1) == ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()
