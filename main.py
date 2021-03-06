import cv2
import numpy as np
from keras.models import model_from_json
from keras.preprocessing import image
import winsound as ws
import threading
import time

json_file = open('fer.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
model = model_from_json(loaded_model_json)

model.load_weights('fer.h5')

face_haar_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(1)

r_image = None
flag = True

curr_time = time.time()

while True:
  ret, img = cap.read()
  if not ret:
    break
  if flag:
    r_image = img
    flag = False
  # cv2.namedWindow('image', cv2.WINDOW_NORMAL)

  gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  faces_detected = face_haar_cascade.detectMultiScale(gray_img, 1.1, 6, minSize=(150, 150))

  if len(faces_detected) != 0:
    for (x, y, w, h) in faces_detected:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)
        cv2.putText(img, 'Press q to exit', (0,15), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 2)
        roi_gray = gray_img[y:y + w, x:x + h]
        roi_gray = cv2.resize(roi_gray, (48, 48))
        img_pixels = image.img_to_array(roi_gray)
        img_pixels = np.expand_dims(img_pixels, axis=0)
        img_pixels /= 255.0

        predictions = model.predict(img_pixels)
        max_index = int(np.argmax(predictions))

        emotions = ['neutral', 'happiness', 'surprise', 'sadness', 'anger', 'disgust', 'fear']
        predicted_emotion = emotions[max_index]

        if max_index in {3, 4, 5, 6}:
          c_time= time.time()
          print(predicted_emotion)
          if c_time - curr_time > 5.0:
            threading.Thread(target=ws.PlaySound, args=('alert.wav', ws.SND_FILENAME), daemon=True).start()
            curr_time = c_time
        cv2.putText(img, predicted_emotion, (int(x), int(y)), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 2)
      
        resized_img = cv2.resize(img, (1000, 700))
        cv2.imshow('Facial Emotion Recognition', resized_img)

  else:
    gray_img = cv2.resize(gray_img, (48, 48))
    img_pixels = image.img_to_array(gray_img)
    img_pixels = np.expand_dims(img_pixels, axis=0)
    img_pixels /= 255.0
    cv2.putText(img, 'Press q to exit', (0,15), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 2)

    predictions = model.predict(img_pixels)
    max_index = int(np.argmax(predictions))

    emotions = ['neutral', 'happiness', 'surprise', 'sadness', 'anger', 'disgust', 'fear']
    predicted_emotion = emotions[max_index]

    if max_index == 4:
      c_time= time.time()
      print(predicted_emotion)
      if c_time - curr_time > 10.0:
        threading.Thread(target=ws.PlaySound, args=('alert.wav', ws.SND_FILENAME), daemon=True).start()
        curr_time = c_time

    resized_img = cv2.resize(img, (1000, 700))
    cv2.imshow('Facial Emotion Recognition', resized_img) 
      
  if cv2.waitKey(1) & 0xFF == ord('q'):
    break

cap.release()
cv2.destroyAllWindows()