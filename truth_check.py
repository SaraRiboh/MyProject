
from packeg import *
from fun_camera import *
from  lie_check import  *






#בדיקה על  שאלת האמת


sentence = "my name is Sarah"
numTruth=0

def fun_truth_check(choice):

    Blood_Pressure1 = random.randint(140, 159)
    Pulse_Pressure1 = random.randint(170, 189)
    print("השלב הראשון הוא בדיקת האמת")


    engine = pyttsx3.init()

    question = input("בוחן יקר אנא הכנס שאלה לשאול את הנבחן")

    engine.say(question)
    engine.runAndWait()

    print("עכשיו תפתח מצלמה ועל הנבחן לענות אמת על השאלה")



    # יצירת תהליך נפרד עבור קליטת שמע
    audio_queue = queue.Queue()
    thread = threading.Thread(target = listen_and_print, args=(sentence, choice,audio_queue))
    thread.start()
    # הפעלת פונקציית המצלמה
    #numTruth = show_camera()# שחוזר מספר נגיעות מהYOLO
    show_camera()


    # המתנה לסיום
    thread.join()

    audio1 = audio_queue.get()
    raw_audio = audio1.get_raw_data()
    audio2 = bytes(raw_audio)
    with wave.open('output_audio.wav', 'wb') as audio_file:
          audio_file.setnchannels(1)
          audio_file.setsampwidth(2)
          audio_file.setframerate(44100)
          audio_file.writeframes(audio2)


    # חישוב תכונות
    features = extract_feature('output_audio.wav', mfcc=True, chroma=True, mel=True)
    # חיזוי רגש
    predicted_emotion = model.predict(features)
    # פירוש התוצאה
    emotion_label1 = predicted_emotion[0]
    print(emotion_label1)


    choice1=2
    print("השלב השני הוא בדיקת השקר")
    fun_lie_check(choice1)




















