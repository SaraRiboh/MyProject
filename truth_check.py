
from packeg import *
from fun_camera import *



#בדיקה על 3 שאלות האמת


person = ["David","Levy","Jerusalem"]

def fun_truth_check(choice):

    Blood_Pressure = random.randint(140, 159)
    Pulse_Pressure = random.randint(170, 189)
    for i in range(3):

        engine = pyttsx3.init()

        question = input("בוחן יקר אנא הכנס שאלה לשאול את הנבחן")

        engine.say(question)
        engine.runAndWait()

        print("עכשיו תפתח מצלמה ועל הנבחן לענות תשובה")

        # יצירת תהליך נפרד עבור קליטת שמע
        thread = threading.Thread(target = listen_and_print, args=(person, i, choice))
        thread.start()
        # הפעלת פונקציית המצלמה
        #num = show_camera()# שחוזר מספר נגיעות מהYOLO

        show_camera()

        # המתנה לסיום תהליך קליטת השמע
        audio1=thread.join()

        # חישוב תכונות
        features = extract_feature(audio1, mfcc=True, chroma=True, mel=True)
        # חיזוי רגש
        predicted_emotion = model.predict(features)
        # פירוש התוצאה
        emotion_label = predicted_emotion[0]
        print(f"Predicted emotion: {emotion_label}")
























