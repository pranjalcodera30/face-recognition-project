import cv2
import os

cam=cv2.VideoCapture(0)
cam.set(3,640)#width
cam.set(4,480)#height

face_detector=cv2.CascadeClassifier('harrcascade_frontalface_default.xml')
face_id=input('\n Enter user id and press enter')
print("\n [INFO] Initializing face capture. ")

