# **Face Recognition Project**
##  **An AI-powered real-time face detection and recognition system!** 🤖📸

### About the Project
This project is a ***Face Recognition System*** that uses OpenCV's ***LBPH (Local Binary Patterns Histograms)*** algorithm for real-time face detection and recognition. The system detects faces using a ***Haar Cascade Classifier*** and then identifies them based on a pre-trained model.

## Features
-***Real-time face detection***m using OpenCV.

-***Face recognition*** with ***LBPHFaceRecognizer***.

-***Customizable dataset*** for training.

-***Displays confidence level*** of predictions.

-***Simple and easy-to-use interface***.

## Technologies Used
### Python:
Used as the core language for developing the face recognition system.

### OpenCV:
For image processing, face detection, and recognition.

### NumPy:
For handling array operations and numerical computations.

## Getting Started


## Clone the Repository

To clone this repository, run the following command in your terminal:

```bash
 git clone https://github.com/pranjalcodera30/face-recognition-project.git
 cd face-recognition-project
```
### Installation
1. #### Install dependencies:
```bash
pip install opencv-python numpy
```
2. #### Download the Haar Cascade file for face detection:
```bash
wget https://github.com/opencv/opencv/raw/master/data/haarcascades/haarcascade_frontalface_default.xml
```
3. #### Ensure you have a trained face dataset in:
   ```bash
   trainer/trainer.yml
   ```
   If not, train your model first (see below).

## Usage
### 1. Training the Face Recognition Model
Before recognizing faces, you need to train the model:
```bash
python train_model.py
```
This will generate the trainer/trainer.yml file, which will be used for recognition.

Press **Esc** to exit the program.
### 2. Running the Face Recognition System
To start the ***real-time face recognition:***

## File Structure
~ ***face_recognition.py:*** Main script for real-time face detection and recognition.

~ ***train_model.py:*** Script to train the face recognition model.

~ ***trainer/trainer.yml:*** File that stores the trained model data.

~ ***haarcascade_frontalface_default.xml:*** Haar Cascade file for face detection.

## Troubleshooting
~ ***Error: 'faceCascade' not defined***
Make sure you correctly initialize the Haar cascade:
```bash
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
```
~ ***Camera not opening?***
Ensure your ***webcam is connected*** and accessible.
Try changing 
```bash
cv2.VideoCapture(0)
```
to 
```bash
cv2.VideoCapture(1)
```
if using an ***external webcam.***

## About the Developer
Hi, I'm ***Pranjal Singh***, an aspiring full-stack developer and AI enthusiast. I’m currently pursuing my undergraduate studies at ***,JIIT Noida, India.***, Combining my love for coding and artificial intelligence, I created this ***,Face Recognition System***, to explore the possibilities of computer vision and deep learning.

🚀 GitHub: pranjalcodera30✉️ Email: pranjaljaypee@gmail.com










