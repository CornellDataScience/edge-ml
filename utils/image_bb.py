import cv2
import os
from datetime import datetime


img_folder = "images" # assume images are in here
os.makedirs('cropped', exist_ok=True)
haar_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

image_idx = 0

for filename in os.listdir(img_folder):
    if filename.endswith(('.jpeg', '.jpg', '.png')):
        imgPath = os.path.join(img_folder, filename)
        img = cv2.imread(imgPath)
        g_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        faces_rect = haar_cascade.detectMultiScale(g_img, scaleFactor=1.1, minNeighbors=6) 

        # time = datetime.now().strftime('%Y-%m-%d-%H-%M-%S')

        # output_dir = 'cropped/{}'.format(time) # write bounding boxes to here
        output_dir = 'cropped/{}'.format(filename[:filename.index(".")])
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        for (x, y, w, h) in faces_rect: 
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), thickness=3) 
            face = img[y:y+h, x:x+w]
            cv2.imwrite('{}/face{}.jpg'.format(output_dir, image_idx), face)
            image_idx += 1

cv2.imshow('bounding-boxes', img) 
cv2.waitKey(0)
