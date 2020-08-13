import os
import pickle
import numpy as np
from scipy.io.wavfile import read
#from speakerfeatures import extract_features
from Training_speakervoice.speakerfeatures import extract_features
import warnings

warnings.filterwarnings("ignore")
import time

# path to training data
source = "Training_speakervoice/development_sets/Viswanath.wav"
modelpath = "Training_speakervoice/speaker_models/"
gmm_files = [os.path.join(modelpath, fname) for fname in os.listdir(modelpath) if fname.endswith('.gmm')]
# Load the Gaussian gender Models
models = [pickle.load(open(fname, 'rb')) for fname in gmm_files]
names = [fname.split(".gmm")[0] for fname in gmm_files]
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
print ("\tdetected as - ",names[winner])
time.sleep(1.0)