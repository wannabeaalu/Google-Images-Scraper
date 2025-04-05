import cv2
from tensorflow import keras
import tensorflow as tf
import numpy as np
import os

#  oneDNN warnings nn not important
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

# pre-trained model jypt one replaceable
model = keras.models.load_model("faceRM.h5")

# Haar cascade for face detection wala
haar_file = cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
face_cascade = cv2.CascadeClassifier(haar_file)


def extract_features(image):
    """Preprocess the image for the model."""
    feature = np.array(image)
    feature = feature.reshape(1, 48, 48, 1)
    return feature / 255.0


webcam = cv2.VideoCapture(0)
labels = {0: 'angry', 1: 'disgust', 2: 'fear', 3: 'happy', 4: 'neutral', 5: 'sad', 6: 'surprise'}

while True:
    i, im = webcam.read()
    if not i:
        print("Failed to capture image")
        break

    gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)  # Use gray image
    try:
        for (p, q, r, s) in faces:
            image = gray[q:q + s, p:p + r]
            cv2.rectangle(im, (p, q), (p + r, q + s), (255, 0, 0), 2)
            image = cv2.resize(image, (48, 48))
            img = extract_features(image)
            pred = model.predict(img)
            prediction_label = labels[pred.argmax()]
            cv2.putText(im, '% s' % (prediction_label), (p - 10, q - 10), cv2.FONT_HERSHEY_COMPLEX_SMALL, 2,
                        (0, 0, 255))

        cv2.imshow("Output", im)
        if cv2.waitKey(27) & 0xFF == ord('x'):
            break
    except cv2.error as e:
        print("Error in processing:", e)

webcam.release()
cv2.destroyAllWindows()
