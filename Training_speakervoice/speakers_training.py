import pickle
import numpy as np
from scipy.io.wavfile import read
from sklearn.mixture import GaussianMixture
from speakerfeatures import extract_features
import warnings
warnings.filterwarnings("ignore")
import os
files=os.listdir("./Training_speakervoice/development_sets")
files.remove(".DS_Store")
print(files)
names = []
for j in range(len(files)):
    x = files[j].split(".")
    names.append(x[0])
print(names)
for i in range(len(names)):
    source = "Training_speakervoice/development_sets/"+names[i]+".wav"
    dest = "Training_speakervoice/speaker_models/"
    features = np.asarray(())

    # read the audio
    sr, audio = read(source)

    # extract 40 dimensional MFCC & delta MFCC features
    vector = extract_features(audio, sr)
    print(vector)

    if features.size == 0:
        features = vector
    else:
        features = np.vstack((features, vector))
        # when features of 5 files of speaker are concatenated, then do model training

    gmm = GaussianMixture(n_components=16, covariance_type='diag', n_init=3)
    gmm.fit(features)

        # dumping the trained gaussian model
    picklefile = names[i]+".gmm"
    pickle.dump(gmm, open(dest + picklefile, 'wb'))
    print('+ modeling completed for speaker:', picklefile, " with data point = ", features.shape)
    features = np.asarray(())


