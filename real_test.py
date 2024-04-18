

from packeg import *
from feelsModel import *
from fun_camera import *


#הבחינה האמיתית
def fun_real_test(choice):
     Blood_Pressure = random.randint(160, 179)
     Pulse_Pressure = random.randint(190, 200)
     person = ["David", "Levy", "Jerusalem"]
     i=1

     question = input("בוחן יקר אנא הכנס שאלה לשאול את הנבחן,אם אינך חפץ לשאול הקש A")

     while(question!='A'):

       engine = pyttsx3.init()
       engine.say(question)
       engine.runAndWait()

       print("עכשיו תפתח מצלמה ועל הנבחן לענות תשובה")



       # יצירת תהליך נפרד עבור קליטת שמע
       audio_queue = queue.Queue()
       thread = threading.Thread(target = listen_and_print, args=(person, i,choice, audio_queue))
       thread.start()
       # הפעלת פונקציית המצלמה
       #num = show_camera()# שחוזר מספר נגיעות מהYOLO
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
       emotion_label = predicted_emotion[0]
       print(f"Predicted emotion: {emotion_label}")
       question = input("בוחן יקר אנא הכנס שאלה לשאול את הנבחן,אם אינך חפץ לשאול הקש A")

