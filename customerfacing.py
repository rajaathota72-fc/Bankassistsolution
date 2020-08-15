def audio_record():
    import pyaudio
    import wave
    # the file name output you want to record into
    filename = "new.wav"
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
    return "audio recorded"
def confirm_speaker():
    import os
    import pickle
    import numpy as np
    from scipy.io.wavfile import read
    from Training_speakervoice.speakerfeatures import extract_features
    import warnings
    warnings.filterwarnings("ignore")
    import time
    # path to training data
    source = "/Users/rajaathota72/PycharmProjects/Bankassistsolution/Training_speakervoice/development_sets/puja.wav"
    modelpath = "Training_speakervoice/speaker_models/"
    gmm_files = [os.path.join(modelpath, fname) for fname in os.listdir(modelpath) if fname.endswith('.gmm')]
    # Load the Gaussian gender Models
    models = [pickle.load(open(fname, 'rb')) for fname in gmm_files]
    names = ['puja', 'Jamuna Kumari', 'CHVS Rama Krishna', 'Uma', 'Vishwanath', 'Uday Kumar', 'unknown', 'Teja']
    # Read the test directory and get the list of test audio files
    sr, audio = read(source)
    vector = extract_features(audio, sr)
    print(vector)
    log_likelihood = np.zeros(len(models))
    for i in range(len(models)):
        gmm = models[i]  # checking with each model one by one
        scores = np.array(gmm.score(vector))
        log_likelihood[i] = scores.sum()
        print(log_likelihood[i])
    winner = np.argmax(log_likelihood)
    print(winner)

    print("\tdetected as - ", names[winner])
    time.sleep(1.0)
    x = names[winner]
    return "Speaker identified as "+x
def capture_pic():
    import cv2
    videoCaptureObject = cv2.VideoCapture(0)
    # result = True
    while True:
        ret, frame = videoCaptureObject.read()
        write = cv2.imwrite("NewPicture.jpg", frame)
        cv2.waitKey(1)
        videoCaptureObject.release()
        cv2.destroyAllWindows()
        return write
def compare_pic():
    import requests

    url = "https://biometricvisionapi.com/v1/compare"

    payload = {}
    path = '/Users/rajaathota72/PycharmProjects/Bankassistsolution/user_database/puja/puja.png'
    files = [
        ('image1', open('/Users/rajaathota72/PycharmProjects/Bankassistsolution/NewPic.jpg', 'rb')),
        ('image2', open(path, 'rb'))
    ]
    headers = {
        'X-Authentication-Token': '7qiLDY2QQAfRuxH3xsoAmfSSYojjC4KQpoOkgRokTFrxcYnAunmMG5iJ1qiFZoN7',
        'Content': 'application/json',
    }
    response = requests.request("POST", url, headers=headers, data=payload, files=files)
    print(response.text.encode('utf8'))
    m = str(response.text.encode('utf8'))
    m_extract = m.split("'")[1]
    m_extract1 = m_extract[15:20]
    if m_extract1 == "Match":
        x = path.split("/")
        return x[6]
def show_account(m,x):
    import pandas as pd
    if m == "Match":
        path = "/Users/rajaathota72/PycharmProjects/Bankassistsolution/user_database/"+x+"/account_details.csv"
        df = pd.read_csv(path)
        return df
import streamlit as st
st.title("Next Gen Cognitive Banking Services - v1")
template = """
    <div style = "background-color : black; padding : 0.1px;">
    <h1 style = "color:white;text-align:center;"> Make your Transactions hassle free</h1>
    </div>
        """
st.markdown(template, unsafe_allow_html=True)
import sounddevice as sd
import soundfile as sf
filename = '/Users/rajaathota72/PycharmProjects/Bankassistsolution/audiofiles/Welcomenote.wav'
data, fs = sf.read(filename, dtype='float32')
sd.play(data, fs)
#status = sd.wait()
if st.button("Start Process"):
    import sounddevice as sd
    import soundfile as sf
    filename = '/Users/rajaathota72/PycharmProjects/Bankassistsolution/audiofiles/voicenoterequest.wav'
    data, fs = sf.read(filename, dtype='float32')
    sd.play(data, fs)
    status = sd.wait()
    st.write("Start with a voice note for authentication")
    audio_record()
    #st.success("Voice received ... Wait for confirmation")
    filename = '/Users/rajaathota72/PycharmProjects/Bankassistsolution/audiofiles/confirmation.wav'
    data, fs = sf.read(filename, dtype='float32')
    sd.play(data, fs)
    status = sd.wait()
    result = confirm_speaker()
    st.success("Voice identified as {}".format(result))
    #st.write("Now authenticate your Face Id")
    filename = '/Users/rajaathota72/PycharmProjects/Bankassistsolution/audiofiles/faceauthrequest.wav'
    data, fs = sf.read(filename, dtype='float32')
    sd.play(data, fs)
    status = sd.wait()
    #img = capture_pic()
    st.image("/Users/rajaathota72/PycharmProjects/Bankassistsolution/NewPic.jpg",width = 300)
    st.success("Pic captured ... Wait for confirmation")
    r = compare_pic()
    st.success("The image matched with {}".format(r))







