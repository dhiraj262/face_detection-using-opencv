import cv2
import sqlite3
import os

conn  = sqlite3.connect('database.db')
if not os.path.exists('./dataset'):
    os.makedirs('./dataset')

c= conn.cursor()

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

username = input("Enter your name: ")
c.execute('INSERT INTO users (name) VALUES (?)', (username,))

userid = c.lastrowid

sampleNum = 0

cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret,img = cap.read()
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        sampleNum = sampleNum+1

        cv2.imwrite("dataset/User."+ str(userid)+"."+str(sampleNum)+".jpg", gray[y:y+h, x:x+w])
        cv2.rectangle(img, (x,y), (x+w, y+h), (255,0,0),2)
        cv2.waitKey(10)
    cv2.imshow('img', img)
    cv2.waitKey(1)
    if sampleNum > 200:
        break
cap.release()
conn.commit()
conn.close()
cv2.destroyAllWindows()



