## importing necessary libraries
# importing our os
import os
#cv stands for computer vision which helps us to recognise the images
import cv2
#pandas is used to deal with data frames (whatever a/cs we are creating will be stored in a table)
import pandas as pd
#numpy is used for creating arrays
import numpy as np
#in order to read images in python environment we use pil(python image library) package
from PIL import Image, ImageEnhance
#the below function deals with importing details like name, account number & amount entered in the web server
#and store it in the user database folder
def storing_data(name,account_number,amount):
    List = [name,account_number,amount]
    df = pd.DataFrame(List)
    directory = "user_database/"
    os.mkdir("user_database/"+name)
    file = os.path.join(directory,name)
    save = df.to_csv(file+"/account_details.csv")
    return save

#function to detect face in the given image/ uploaded image
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

def detect_faces(our_image):
    new_img = np.array(our_image.convert('RGB'))
    img = cv2.cvtColor(new_img, 1)
    gray = cv2.cvtColor(new_img, cv2.COLOR_BGR2GRAY)
    # Detect faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    # Draw rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    return img, faces

#it is used to store the image in the respective folder when face is recognised
def store_image(image,x):
    image1 = Image.open(image)
    directory = "user_database/"
    file = os.path.join(directory, x)
    save1 = image1.save(file+"/"+x+".png")
    return save1

# the function is for recording and storing audio of the user
def record_audio(name):
    import pyaudio
    import wave

    # the file name output you want to record into
    filename = "user_database/"+name+"/"+name+".wav"
    # set the chunk size of 1024 samples
    chunk = 1024
    # sample format
    FORMAT = pyaudio.paInt16
    # mono, change to 2 if you want stereo
    channels = 1
    # 44100 samples per second
    sample_rate = 44100
    record_seconds = 5
    # initialize PyAudio object
    p = pyaudio.PyAudio()
    # open stream object as input & output
    stream = p.open(format=FORMAT,
                    channels=channels,
                    rate=sample_rate,
                    input=True,
                    output=True,
                    frames_per_buffer=chunk)
    frames = []
    print("Recording...")
    for i in range(int(44100 / chunk * record_seconds)):
        data = stream.read(chunk)
        # if you want to hear your voice while recording
        # stream.write(data)
        frames.append(data)
    print("Finished recording.")
    # stop and close stream
    stream.stop_stream()
    stream.close()
    # terminate pyaudio object
    p.terminate()
    # save audio file
    # open the file in 'write bytes' mode
    wf = wave.open(filename, "wb")
    # set the channels
    wf.setnchannels(channels)
    # set the sample format (amplitude(peak of the sound wave))
    wf.setsampwidth(p.get_sample_size(FORMAT))
    # set the sample rate (setting the frequency)
    wf.setframerate(sample_rate)
    # write the frames as bytes (for joining
    wf.writeframes(b"".join(frames))
    # close the file
    wf.close()



import streamlit as st
def main():
    st.title("Bank Assist System : Super Admin Panel")
    template = """
    <div style = "background-color : black; padding : 0.1px;">
    <h1 style = "color:white;text-align:center;"> Create New Account</h1>
    </div>
        """
    st.markdown(template, unsafe_allow_html=True)
    name = st.text_input("Name of the Account Holder", "typehere")
    account_number = st.text_input("Account Number", "typehere")
    Amount = st.text_input("Amount deposit", "typehere")
    if st.button("Create Account"):
        storing_data(name, account_number, Amount)
        st.success("Account created successfully")
        st.balloons()

    if st.button("Face Authentication"):
        import io
        image_file = st.file_uploader("Upload Image for face Authentication", type=['jpg', 'png', 'jpeg'])
        text_io = io.TextIOWrapper(image_file)
        st.set_option('deprecation.showfileUploaderEncoding', False)
        our_image = Image.open(image_file)
        result_img, result_faces = detect_faces(our_image)
        st.image(result_img)
        st.success("Found {} faces".format(len(result_faces)))
        store_image(image_file, name)
        st.success("Face stored successfully")

    if st.button("Record Voice note"):
        with st.spinner("Now record"):
            st.write("Record a voice note")
            record_audio(name)

if __name__ == "__main__":
    main()