import cv2
import os

# Initialize the webcam
cam = cv2.VideoCapture(0)
cam.set(3, 640)  # Set video width
cam.set(4, 480)  # Set video height

# Load the pre-trained face detector (make sure the path is correct)
face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Prompt user for their ID
face_id = input('\n Enter user id and press enter: ')
print("\n [INFO] Initializing face capture. ")

count = 0

while(True):
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_detector.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)  # Draw rectangle around face
        count += 1

        # Save the captured image to the dataset
        cv2.imwrite("Dataset/User." + str(face_id) + '.' + str(count) + ".jpeg", gray[y:y + h, x:x + w])

    # Display the image
    cv2.imshow('image', img)

    k = cv2.waitKey(100) & 0xff  # Wait for keypress
    if k == 27:  # ESC key
        break
    elif count >= 30:  # Capture 30 images
        break

print("\n [INFO] Exiting program")

# Release the camera and close any OpenCV windows
cam.release()
cv2.destroyAllWindows()
