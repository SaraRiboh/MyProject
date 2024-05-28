
from packeg import *



def extract_feature(file_name, mfcc=True, chroma=True, mel=True):
    global observed_emotions
    with soundfile.SoundFile(file_name) as sound_file:
        sample_rate = sound_file.samplerate
        X = sound_file.read(dtype="float32")

    result = None  # Initialize result as None

    if chroma:
        stft = np.abs(librosa.stft(X))
        chroma = np.mean(librosa.feature.chroma_stft(S=stft, sr=sample_rate).T, axis=0)
        result = chroma if result is None else np.hstack((result, chroma))

    if mfcc:
        mfccs = np.mean(librosa.feature.mfcc(y=X, sr=sample_rate, n_mfcc=40).T, axis=0)
        result = mfccs if result is None else np.hstack((result, mfccs))

    if mel:
        mel = np.mean(librosa.feature.melspectrogram(y=X, sr=sample_rate).T, axis=0)
        result = mel if result is None else np.hstack((result, mel))

    if result is not None:
        result = result.reshape(1, -1)  # Reshape the result to 2D array

    return result
    #DataFlair - Emotions in the RAVDESS dataset
emotions={
  '01':'neutral',
  '02':'calm',
  '03':'happy',
  '04':'sad',
  '05':'angry',
  '06':'fearful',
  '07':'disgust',
  '08':'surprised'
}
#DataFlair - Emotions to observe
observed_emotions=['calm','fearful']
#DataFlair - Load the data and extract features for each sound file

def load_data(test_size=0.1):
    x, y = [], []
    for file in glob.glob("D:\\Users\\שרי\\Desktop\\DataSetFeel\\Actor_*\\*.wav"):
        file_name = os.path.basename(file)
        emotion = emotions[file_name.split("-")[2]]
        if emotion not in observed_emotions:
            continue
        feature = extract_feature(file, mfcc=True, chroma=True, mel=True)

        if feature is not None:
            x.append(feature.flatten())
            y.append(emotion)

    x = np.array(x)
    y = np.array(y)

    return train_test_split(x, y, test_size=test_size, random_state=9)
    #DataFlair - Split the dataset
x_train,x_test,y_train,y_test=load_data(test_size=0.25)
print((x_train.shape[0], x_test.shape[0]))
model=MLPClassifier(alpha=0.01, batch_size=256, epsilon=1e-08, hidden_layer_sizes=(300,), learning_rate='adaptive', max_iter=500)
model.fit(x_train,y_train)
y_pred=model.predict(x_test)
accuracy=accuracy_score(y_true=y_test, y_pred=y_pred)
print("Accuracy: {:.2f}%".format(accuracy*100))



