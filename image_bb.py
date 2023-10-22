import cv2
import os
from datetime import datetime

imgPath = "test.jpeg"
img = cv2.imread(imgPath)
g_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

haar_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
faces_rect = haar_cascade.detectMultiScale(g_img, scaleFactor=1.1, minNeighbors=6) 

os.makedirs('images', exist_ok=True)

name = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
os.makedirs('images/{}'.format(name))

for i, (x, y, w, h) in enumerate(faces_rect): 
    cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), thickness=3) 
    roi = img[y:y+h, x:x+w]
    cv2.imwrite('images/{}/roi{}.jpg'.format(name, i), roi)

cv2.imshow('bounding-boxes', img) 
cv2.waitKey(0)
