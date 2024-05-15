

from packeg import *
from feelsModel import *
from fun_camera import *
from truth_check import *
from lie_check import *


Blood_Pressure1_Low=160
Blood_Pressure1_High=179

Pulse_Pressure1_Low=190
Pulse_Pressure1_High=200
len=4
res=[]
percents=[]
def read_file_to_array(filename):
  with open(filename, 'r') as file:
    for line in file:
      percents.append(line.rstrip())
#הבחינה האמיתית

#הפונקציה סופרת כמה נגיעות בפנים יש ומחשבת אם זה אמת או שקר
def check_touches_in_face():
    num=0

    # הפעלת פונקציית המצלמה
    # num = show_camera()# שחוזר מספר נגיעות מהYOLO
    show_camera()
    # המתנה לסיום


    res.append((num>0))

#בדיקת רגש בקול
def checkSentiment(choice):
    # יצירת תהליך נפרד עבור קליטת שמע
    audio_queue = queue.Queue()
    thread = threading.Thread(target=listen_and_print, args=(sentence, choice, audio_queue))
    thread.start()
    check_touches_in_face()
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
    emotion_label2 = predicted_emotion[0]
    #אם הרגש הוא חיובי - יחזיר 1*4 אם שלילי יחזיר 4*0
    res.append((emotion_label2 == observed_emotions[2] or emotion_label2 == observed_emotions[3]))

def Blood():
    blood_Pressure3 = random.randint(140, 179)
    res.append((blood_Pressure3>Blood_Pressure1_Low and blood_Pressure3<=Blood_Pressure1_High))

def Pulse():
    Pulse_Pressure2 = random.randint(170, 200)
    res.append((Pulse_Pressure2>Pulse_Pressure1_Low and Pulse_Pressure2<=Pulse_Pressure1_High))

sentence = "My Name Is Sara"
def fun_real_test(choice):


     question = input("בוחן יקר אנא הכנס שאלה לשאול את הנבחן,אם אינך חפץ לשאול הקש A")

     while(question!='A'):
        engine = pyttsx3.init()
        engine.say(question)
        engine.runAndWait()

        checkSentiment(choice)
        Blood()
        Pulse()

        result=0
        for i in range(len):
            result+=percents[i]*res[i]
        str_p = str(result)
        print("הנבחן שיקר בוודאות של "+str_p+"%")
        question = input("בוחן יקר אנא הכנס שאלה לשאול את הנבחן,אם אינך חפץ לשאול הקש A")

