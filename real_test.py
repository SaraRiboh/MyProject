

from packeg import *
from feelsModel import *
from fun_camera import *
from truth_check import *
from lie_check import *

#הבחינה האמיתית

sentence = "My Name Is Sara"
def fun_real_test(choice,Blood_Pressure2, Pulse_Pressure2,emotion_label):
     Blood_Pressure3 = random.randint(140, 179)
     Pulse_Pressure3 = random.randint(170, 200)


     question = input("בוחן יקר אנא הכנס שאלה לשאול את הנבחן,אם אינך חפץ לשאול הקש A")

     while(question!='A'):

       engine = pyttsx3.init()
       engine.say(question)
       engine.runAndWait()

       print("עכשיו תפתח מצלמה ועל הנבחן לענות תשובה")



       # יצירת תהליך נפרד עבור קליטת שמע
       audio_queue = queue.Queue()
       thread = threading.Thread(target = listen_and_print, args=(sentence,choice, audio_queue))
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
       emotion_label2 = predicted_emotion[0]
       percent=0
       if(emotion_label2==emotion_label):
          percent+=30
       if(Blood_Pressure3>159):
           percent+=5
       if(Pulse_Pressure3>179):
           percent += 5
       str_p = str(percent)
       print("הנבחן שיקר בוודאות של "+str_p+"%")
       question = input("בוחן יקר אנא הכנס שאלה לשאול את הנבחן,אם אינך חפץ לשאול הקש A")

