import cv2
import numpy as np
from PIL import Image
import os

path='dataset'
recognizer=cv2.face.LBPHFaceRecognizer_create()
detector=cv2.CascadeClassifier("harrcascade_frontalface_default.xml")

def getImagesAndLabels(path):
    imagePaths=[os.path.join(path,f) for in os.listdir(path)]
    facesamples=[]
    ids=[]
    

    for imagePath in imagePaths:
        PIL_image=Image.open(imagePath) 
