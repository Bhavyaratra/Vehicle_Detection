
import urllib.request
import cv2
import numpy as np
import time

# Replace the URL with your own IPwebcam shot.jpg IP:port
url='http://192.168.1.100:8080/shot.jpg'


while True:
    imgResp = urllib.request.urlopen(url)

    imgNp = np.array(bytearray(imgResp.read()),dtype=np.uint8)
     
    img = cv2.imdecode(imgNp,-1)
	
    cv2.imshow('IPWebcam',img)

    # Quit if q is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break