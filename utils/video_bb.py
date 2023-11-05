import cv2
import os 
from datetime import datetime

# video doesnt' work

webcam = cv2.VideoCapture(0)
haar_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")


os.makedirs('images', exist_ok=True)

name = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
os.makedirs('images/{}'.format(name))

image_idx = 0

while True:
    (_, img) = webcam.read()
    g_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces_rect = haar_cascade.detectMultiScale(g_img, scaleFactor=1.1, minNeighbors=6) 
    for (x, y, w, h) in faces_rect: 
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), thickness=3) 
        face = img[y:y + h, x:x + w] 
        cv2.imwrite('images/{}/face{}.jpg'.format(name, image_idx), face)
        image_idx += 1

    cv2.imshow('bounding-boxes', img)
    cv2.waitKey(0)
    
