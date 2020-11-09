# -*- coding: utf-8 -*-
import urllib.request
import cv2
import numpy as np
import time
print(cv2.__version__)

##################
url='http://192.168.1.100:8080/shot.jpg'

cascade_src = 'cars.xml'
car_cascade = cv2.CascadeClassifier(cascade_src)

while True:
    imgResp = urllib.request.urlopen(url)

    imgNp = np.array(bytearray(imgResp.read()),dtype=np.uint8)
     
    img = cv2.imdecode(imgNp,-1)
	    
    # Quit if q is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#video_src = 'dataset/video2.avi'

    if (type(img) == type(None)):
        break
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    cars = car_cascade.detectMultiScale(gray, 1.1, 1)

    for (x,y,w,h) in cars:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)      
    
    cv2.imshow('IPWebcam',img)
    
    if cv2.waitKey(33) == 27:
        break

cv2.destroyAllWindows()