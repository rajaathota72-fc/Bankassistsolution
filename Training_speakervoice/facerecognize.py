import cv2
import numpy as np
import os
from PIL import Image
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("/Users/rajaathota72/PycharmProjects/Bankassistsolution/Training_speakervoice/trainer.yml")
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)
font = cv2.FONT_HERSHEY_SIMPLEX
# iniciate id counter
id = 0
# names related to ids: example ==> Marcelo: id=1,  etc
names = [1,2,3,4,5,6,7,8]
img = cv2.imread("/Users/rajaathota72/Downloads/WhatsApp Image 2020-08-10 at 15.35.39.jpeg")
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
faces = faceCascade.detectMultiScale(img,scaleFactor=1.2,minNeighbors=5,minSize=(300,300))
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
    id, confidence = recognizer.predict(gray[y:y + h, x:x + w])
    # Check if confidence is less them 100 ==> "0" is perfect match
    if (confidence < 100):
        id = names[id]
        confidence = "  {0}%".format(round(100 - confidence))
    else:
        id = "unknown"
        confidence = "  {0}%".format(round(100 - confidence))
    cv2.putText(img, str(id), (x + 5, y - 5), font, 1, (255, 255, 255), 2)
    cv2.putText(img, str(confidence), (x + 5, y + h - 5), font, 1, (255, 255, 0), 1)
    print(id,confidence)


# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
cv2.destroyAllWindows()