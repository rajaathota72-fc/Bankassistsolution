import os
import cv2
import pandas as pd
def storing_data():
    name = entry1.get()
    account_number=entry2.get()
    amount = entry3.get()
    List = [name,account_number,amount]
    df = pd.DataFrame(List)
    directory = "user_database/"
    file = os.path.join(directory,name)
    save = df.to_csv(file+"/account_details.csv")
    return save
def capturing_pics():
    faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    video_capture = cv2.VideoCapture(0)
    while True:
        ref, frame = video_capture.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    video_capture.release()
    cv2.destroyAllWindows()
import tkinter as tk
window = tk.Tk()
label = tk.Label(text = "Bank Assist System - Super Admin Panel")
label.config(font=("Courier",16))
label.grid(row=0,column=0)
frame1 = tk.Frame()
label1 = tk.Label(master = frame1,text =  "Name").grid(row=1,column=0,pady=10)
entry1 = tk.Entry(master=frame1)
entry1.grid(row=1,column=1)
label2 = tk.Label(master = frame1,text =  "Account Number").grid(row=2,column=0,pady=10)
entry2 = tk.Entry(master=frame1)
entry2.grid(row=2,column=1)
label3 = tk.Label(master = frame1,text =  "Amount").grid(row=3,column=0,pady=10)
entry3 = tk.Entry(master=frame1)
entry3.grid(row=3,column=1)
button1=tk.Button(frame1,text = "Create Account",command=storing_data())
button1.grid(row=4,column=0,pady=10)
frame1.grid(column=0)
window.mainloop()